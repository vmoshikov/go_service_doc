"""Разбор Go-кода через tree-sitter. Только факты из исходников, без догадок.

Если tree-sitter не установлен, модуль падает с ошибкой. Тихой замены на regex нет:
неточная документация хуже, чем отсутствие документации.
"""
import re
from dataclasses import dataclass, field
from pathlib import Path

try:
    import tree_sitter_go
    from tree_sitter import Language, Parser
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Ошибка: нет tree-sitter. Установи: pip install -r requirements.txt") from exc

_PARSER = Parser(Language(tree_sitter_go.language()))

METRIC_FUNC = re.compile(r"New(Counter|Gauge|Histogram|Summary)(Vec)?$")
TEST_FUNC = re.compile(r"^(Test|Benchmark|Fuzz|Example)")
MAX_TYPE_LINES = 30
MAX_SOURCE_LINES = 60


def _source(node) -> str:
    lines = _text(node).splitlines()
    return "\n".join(lines[:MAX_SOURCE_LINES] + (["// ... сокращено"] if len(lines) > MAX_SOURCE_LINES else []))


@dataclass
class Decl:
    kind: str          # func, method, type
    name: str
    receiver: str      # тип получателя для method, иначе ""
    signature: str
    comment: str
    file: str
    line: int
    source: str = ""  # исходный текст объявления, сокращённый: контекст для LLM


@dataclass
class Metric:
    name: str
    type: str
    help: str
    labels: list
    file: str
    line: int


@dataclass
class Package:
    path: str                    # путь от корня репозитория, "." для корня
    name: str = ""
    doc: str = ""
    imports: set = field(default_factory=set)
    decls: list = field(default_factory=list)
    metrics: list = field(default_factory=list)
    tests: int = 0
    is_main: bool = False
    consts: dict = field(default_factory=dict)  # строковые константы для имён метрик


# ---------- go.mod ----------

def parse_go_mod(path: Path) -> dict:
    """module, go и прямые зависимости (без // indirect)."""
    result = {"module": "", "go": "", "require": {}}
    if not path.is_file():
        return result
    in_block = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("//")[0].strip()
        indirect = "// indirect" in raw
        if line.startswith("module "):
            result["module"] = line.split()[1]
        elif line.startswith("go "):
            result["go"] = line.split()[1]
        elif line.startswith("require ("):
            in_block = True
        elif in_block and line == ")":
            in_block = False
        elif (in_block or line.startswith("require ")) and line and not indirect:
            parts = line.removeprefix("require ").split()
            if len(parts) >= 2:
                result["require"][parts[0]] = parts[1]
    return result


# ---------- Разбор файлов ----------

def _text(node) -> str:
    return node.text.decode("utf-8") if node is not None else ""


def _clean_comment(nodes) -> str:
    lines = []
    for node in nodes:
        text = _text(node)
        if text.startswith("//"):
            lines.append(text[2:].strip())
        else:  # /* */ — тоже комментарий Go
            lines.extend(l.strip(" *") for l in text[2:-2].splitlines())
    return " ".join(l for l in lines if l).strip()


def _leading_comment(siblings, index) -> str:
    """Комментарии подряд прямо над узлом siblings[index]."""
    collected, expected_row = [], siblings[index].start_point[0] - 1
    i = index - 1
    while i >= 0 and siblings[i].type == "comment" and siblings[i].end_point[0] == expected_row:
        collected.insert(0, siblings[i])
        expected_row = siblings[i].start_point[0] - 1
        i -= 1
    return _clean_comment(collected)


def _signature(node) -> str:
    body = node.child_by_field_name("body")
    end = body.start_byte if body is not None else node.end_byte
    return node.text[: end - node.start_byte].decode("utf-8").strip()


def _receiver_type(node) -> str:
    text = _text(node.child_by_field_name("receiver")).strip("()")
    text = text.split()[-1] if text.split() else ""
    return re.sub(r"\[.*\]$", "", text.lstrip("*"))


def _type_specs(decl):
    """(type_spec, комментарий) для одиночного и группового type (...)."""
    children = decl.children
    specs = [i for i, c in enumerate(children) if c.type == "type_spec"]
    for i in specs:
        yield children[i], _leading_comment(children, i)


def _walk(node):
    yield node
    for child in node.children:
        yield from _walk(child)


def _string_value(node) -> str:
    text = _text(node)
    if node.type in ("interpreted_string_literal", "raw_string_literal") or text[:1] in "\"`":
        return text[1:-1]
    return "{" + text + "}"  # константа или выражение: показываем как есть


def _metric(call, rel) -> Metric | None:
    func = _text(call.child_by_field_name("function"))
    match = METRIC_FUNC.search(func)
    if not match or "prom" not in func:
        return None
    args = [a for a in call.child_by_field_name("arguments").named_children]
    if not args:
        return None
    opts = {}
    for node in _walk(args[0]):
        if node.type == "keyed_element" and len(node.named_children) >= 2:
            key = _text(node.named_children[0])
            opts[key] = node.named_children[1]
    if "Name" not in opts:
        return None
    parts = [_string_value(_unwrap(opts[k])) for k in ("Namespace", "Subsystem", "Name") if k in opts]
    labels = []
    if len(args) > 1:
        labels = [_string_value(n) for n in _walk(args[1]) if n.type == "interpreted_string_literal"]
    help_text = _string_value(_unwrap(opts["Help"])) if "Help" in opts else ""
    kind = match.group(1).lower() + ("_vec" if match.group(2) else "")
    return Metric("_".join(p for p in parts if p), kind, help_text, labels, rel, call.start_point[0] + 1)


def _unwrap(node):
    """literal_element(x) → x."""
    while node.type == "literal_element" and node.named_children:
        node = node.named_children[0]
    return node


def parse_file(path: Path, rel: str, package: Package) -> None:
    tree = _PARSER.parse(path.read_bytes())
    root = tree.root_node
    children = root.children
    for i, node in enumerate(children):
        if node.type == "package_clause":
            package.name = _text(node.named_children[0])
            doc = _leading_comment(children, i)
            if doc and not package.doc:
                package.doc = doc
        elif node.type == "import_declaration":
            for spec in _walk(node):
                if spec.type == "import_spec":
                    package.imports.add(_text(spec.child_by_field_name("path")).strip('"`'))
        elif node.type == "function_declaration":
            name = _text(node.child_by_field_name("name"))
            if name == "main" and package.name == "main":
                package.is_main = True
            if name[:1].isupper():
                package.decls.append(Decl("func", name, "", _signature(node),
                                          _leading_comment(children, i), rel, node.start_point[0] + 1, _source(node)))
        elif node.type == "method_declaration":
            name = _text(node.child_by_field_name("name"))
            receiver = _receiver_type(node)
            if name[:1].isupper() and receiver[:1].isupper():
                package.decls.append(Decl("method", name, receiver, _signature(node),
                                          _leading_comment(children, i), rel, node.start_point[0] + 1, _source(node)))
        elif node.type == "type_declaration":
            for spec, comment in _type_specs(node):
                name = _text(spec.child_by_field_name("name"))
                if not name[:1].isupper():
                    continue
                lines = ("type " + _text(spec)).splitlines()
                if len(lines) > MAX_TYPE_LINES:
                    lines = lines[:MAX_TYPE_LINES] + ["\t// ... сокращено"]
                comment = comment or (_leading_comment(children, i) if len(list(_type_specs(node))) == 1 else "")
                package.decls.append(Decl("type", name, "", "\n".join(lines), comment, rel,
                                          spec.start_point[0] + 1))
    for node in _walk(root):
        if node.type == "const_spec":
            value = node.child_by_field_name("value")
            if value is not None and value.named_children and value.named_children[0].type == "interpreted_string_literal":
                for name in node.children_by_field_name("name"):
                    package.consts[_text(name)] = _text(value.named_children[0])[1:-1]
        if node.type == "call_expression":
            metric = _metric(node, rel)
            if metric:
                package.metrics.append(metric)


def count_tests(path: Path) -> int:
    root = _PARSER.parse(path.read_bytes()).root_node
    return sum(1 for n in root.children if n.type == "function_declaration"
               and TEST_FUNC.match(_text(n.child_by_field_name("name"))))


def parse_repo(repo: Path, exclude: list) -> dict:
    """Все пакеты репозитория: {путь_пакета: Package}."""
    result = {}
    for path in sorted(repo.rglob("*.go")):
        rel = path.relative_to(repo).as_posix()
        parts = rel.split("/")
        if any(p in ("vendor", "testdata") or p.startswith(".") for p in parts[:-1]):
            continue
        if any(rel == e or rel.startswith(e.rstrip("/") + "/") for e in exclude):
            continue
        pkg_path = "/".join(parts[:-1]) or "."
        package = result.setdefault(pkg_path, Package(pkg_path))
        if path.name.endswith("_test.go"):
            package.tests += count_tests(path)
        else:
            parse_file(path, rel, package)
    for package in result.values():
        for metric in package.metrics:
            metric.name = re.sub(r"\{(\w+)\}", lambda m: package.consts.get(m.group(1), m.group(0)), metric.name)
    # Пакеты только с тестами не документируем.
    return {k: v for k, v in result.items() if v.name}
