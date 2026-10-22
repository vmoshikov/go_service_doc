#!/usr/bin/env python3
"""Создаёт документацию компонента или модуля в wiki/code/<имя>/ из репозитория на теге.

Использование:
    python scripts/code_docs.py <имя|URL репозитория> <тег> [--repo <путь>] [--since <тег>]

Запуск: CI wiki-репозитория по тегу компонента. Без --repo скрипт клонирует компонент по реестру.
Если wiki уже описывает этот тег или более новый, скрипт ничего не меняет.

Факты (сигнатуры, API, CRD, метрики, конфигурация, CHANGELOG) извлекает tree-sitter и парсеры.
Текст (обзор, описания без комментария) пишет LLM через OpenAI-совместимый API: см. _enrich.py.
Без ключа или с --no-llm скрипт пишет только факты.

Скил: skills/code-docs/SKILL.md
"""
import argparse
import re
import shutil
import sys
import tomllib
from pathlib import Path

import _enrich
import _go
import _helm
import _llm
import _proto
import wiki_index
from _wiki import CODE, ROOT, append_log, frontmatter, git, load_registry, normalize_repo, read_page, today

TASK_KEY = re.compile(r"[A-Z][A-Z0-9]+-\d+")
VERSION_RE = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)")
PSEUDO_HASH = re.compile(r"-([0-9a-f]{12})$")
MERGE_RE = re.compile(r"Merge branch '([^']+)'")
DEFAULT_CATEGORIES = {
    "feature/": "Добавлено", "feat/": "Добавлено",
    "fix/": "Исправлено", "bugfix/": "Исправлено", "hotfix/": "Исправлено",
    "refactor/": "Изменено", "release/": "Изменено",
    "remove/": "Удалено", "revert/": "Удалено",
}
CATEGORY_ORDER = ["Добавлено", "Изменено", "Исправлено", "Удалено"]
IMPACT_PREFIX = "Влияние на L2/L3:"


# ---------- Общие части страницы ----------

def page_header(name, title, page_type, ctx, **extra) -> str:
    llm = ctx["llm"].model if ctx.get("llm") and ctx["llm"].used else None
    return frontmatter(
        title=f"{name} — {title}", type=page_type, components=[name], repo=ctx["repo"],
        version=ctx["version"], commit=ctx["commit"], **extra, llm=llm, generated="true",
    ) + f"\n# {name} — {title}\n"


LLM_MARK = "_(LLM)_"


def comment_or_stub(text: str, generated: str = "") -> str:
    """Комментарий автора; без него — текст LLM с пометкой; без обоих — заглушка."""
    if text:
        return text
    return f"{generated} {LLM_MARK}" if generated else "_Нет описания в коде._"


# ---------- README ----------

def short_doc(pkg) -> str:
    """Первое предложение комментария пакета без вступления «Package <имя>»."""
    text = re.sub(rf"^Package\s+{re.escape(pkg.name)}\s+", "", pkg.doc).split(". ")[0].rstrip(".")
    return text[:1].upper() + text[1:]


def package_graph(packages: dict, module: str) -> str:
    """Mermaid: импорты между пакетами репозитория, сгруппированные до 2 уровней пути."""
    def group(path):
        return "/".join(path.split("/")[:2]) if path != "." else "."
    by_import = {f"{module}/{p}" if p != "." else module: group(p) for p in packages}
    edges = set()
    for path, package in packages.items():
        for imp in package.imports:
            target = by_import.get(imp)
            if target and target != group(path):
                edges.add((group(path), target))
    if not edges:
        return ""
    ids = {g: f"n{i}" for i, g in enumerate(sorted({g for e in edges for g in e}))}
    lines = ["```mermaid", "graph LR"]
    lines += [f'  {ids[g]}["{g}"]' for g in ids]
    lines += [f"  {ids[a]} --> {ids[b]}" for a, b in sorted(edges)]
    return "\n".join(lines + ["```"])


def write_readme(out, name, repo, ctx, gomod, packages, pages) -> None:
    rows = [
        ("Тип", "компонент" if ctx["kind"] == "component" else "общий модуль"),
        ("Репозиторий", ctx["repo"]),
        ("Версия", f"`{ctx['version']}` · коммит `{ctx['commit']}`"),
        ("Go", f"`{gomod['module']}` · go {gomod['go']}"),
    ]
    mains = [p for p, pkg in packages.items() if pkg.is_main]
    if mains:
        rows.append(("Точки входа", ", ".join(f"`{p}`" for p in mains)))
    tests = sum(p.tests for p in packages.values())
    untested = [p for p, pkg in packages.items() if not pkg.tests and not pkg.is_main]
    rows.append(("Тесты", f"тестовых функций: {tests}; пакетов без тестов: {len(untested)} из {len(packages)}"))

    uses = [f"{m}@{v}" for m, v in sorted(gomod["require"].items()) if m in ctx["platform_modules"]]
    if uses:
        rows.append(("Модули платформы", ", ".join(f"`{u}`" for u in uses)))
    # Поле uses читает release_docs.py, чтобы построить таблицу «кто использует модуль».
    body = [page_header(name, "обзор", "code-overview", ctx, uses=uses), "## Паспорт\n",
            "| Поле | Значение |", "|------|----------|"]
    body += [f"| {k} | {v} |" for k, v in rows]

    llm = ctx.get("llm")
    if llm and (llm.purpose or llm.how):
        body += ["\n## Обзор\n",
                 f"_Текст сгенерирован LLM `{llm.model}` по коду `{ctx['commit']}`. "
                 "Все имена проверены по коду. Комментарии в коде и раздел «Архитектура» важнее._\n"]
        if llm.purpose:
            body.append(llm.purpose + "\n")
        body += [f"- {item}" for item in llm.how]

    doc_dir = repo / "docs"
    arch = doc_dir / "architecture.md"
    body.append("\n## Архитектура\n")
    if arch.is_file():
        text = arch.read_text(encoding="utf-8").strip()
        text = re.sub(r"^# .*\n+", "", text)  # заголовок страницы уже есть
        body.append(re.sub(r"^(#+) ", r"#\1 ", text, flags=re.M))
    else:
        body.append("_Команда не описала архитектуру: нет файла `docs/architecture.md`._")

    team_docs = sorted(p for p in doc_dir.rglob("*.md") if p != arch) if doc_dir.is_dir() else []
    if team_docs:
        body.append("\n## Документы команды\n")
        for path in team_docs:
            rel = path.relative_to(doc_dir).as_posix()
            target = out / "docs" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            title = next((l[2:].strip() for l in path.read_text(encoding="utf-8").splitlines()
                          if l.startswith("# ")), rel)
            body.append(f"- [{title}](docs/{rel})")

    body.append("\n## Пакеты\n")
    body += ["| Пакет | Описание | Тесты |", "|-------|----------|-------|"]
    for path, pkg in sorted(packages.items()):
        generated = (ctx.get("llm").packages.get(path) if ctx.get("llm") else "") or ""
        doc = short_doc(pkg) or (f"{generated.split('. ')[0].rstrip('.')} {LLM_MARK}" if generated else "—")
        body.append(f"| `{path}` | {doc} | {pkg.tests or '—'} |")
    graph = package_graph(packages, gomod["module"])
    if graph:
        body += ["\n### Связи пакетов\n", graph]

    if pages:
        body.append("\n## Разделы\n")
        body += [f"- [{title}]({file})" for file, title in pages]
    (out / "README.md").write_text("\n".join(body) + "\n", encoding="utf-8")


# ---------- API ----------

def message_table(name, messages, llm=None) -> list:
    msg = messages.get(name.split(".")[-1])
    if not msg:
        return [f"`{name}` — определение вне репозитория."]
    about = msg.comment or (f"{llm.messages[msg.name]} {LLM_MARK}" if llm and msg.name in llm.messages else "")
    if not msg.fields:
        return [f"`{name}` — без полей." + (f" {about}" if about else "")]
    rows = ["| Поле | Тип | № | Описание |", "|------|-----|---|----------|"]
    rows += [f"| `{f}` | `{t}` | {n} | {c or '—'} |" for t, f, n, c in msg.fields]
    return [f"`{name}`" + (f" — {about}" if about else ""), ""] + rows


def write_api(out, name, ctx, services, messages, crds) -> bool:
    if not services and not crds:
        return False
    llm = ctx.get("llm")
    body = [page_header(name, "API", "code-api", ctx)]
    for package, svc in services:
        for rpc in svc.rpcs:
            req = ("stream " if rpc.client_stream else "") + rpc.request
            resp = ("stream " if rpc.server_stream else "") + rpc.response
            body.append(f"## gRPC: {svc.name}.{rpc.name}\n")
            body.append(f"`{svc.file}:{rpc.line}` · пакет `{package}` · `{req}` → `{resp}`\n")
            body.append(comment_or_stub(rpc.comment, llm.rpcs.get(f"{svc.name}.{rpc.name}", "") if llm else "") + "\n")
            for verb, url in rpc.http:
                body.append(f"HTTP: `{verb} {url}`\n")
            body += message_table(rpc.request, messages, llm) + [""]
            body += message_table(rpc.response, messages, llm) + [""]
    used = {r.request.split(".")[-1] for _, s in services for r in s.rpcs} | \
           {r.response.split(".")[-1] for _, s in services for r in s.rpcs}
    enums = [m for m in messages.values() if m.kind == "enum"]
    if enums:
        body.append("## Перечисления\n")
        for enum in enums:
            body.append(f"### {enum.name}\n\n`{enum.file}:{enum.line}`\n")
            body.append(", ".join(f"`{v}` = {n}" for _, v, n, _ in enum.fields) + "\n")
    other = [m for m in messages.values() if m.kind == "message" and m.name not in used]
    if other:
        body.append("## Другие сообщения\n")
        for msg in other:
            body.append(f"### {msg.name}\n\n`{msg.file}:{msg.line}`\n")
            body += message_table(msg.name, messages)[2:] + [""]
    for crd in crds:
        spec = crd.get("spec", {})
        kind = spec.get("names", {}).get("kind", "?")
        for version in spec.get("versions", []):
            schema = (version.get("schema") or {}).get("openAPIV3Schema") or {}
            body.append(f"## CRD: {kind} ({spec.get('group')}/{version.get('name')})\n")
            body.append(f"Область: `{spec.get('scope')}` · хранение: "
                        f"{'да' if version.get('storage') else 'нет'}\n")
            body += ["| Поле | Тип | Обязательно | По умолчанию | Описание |",
                     "|------|-----|-------------|--------------|----------|"]
            for path, ftype, req, default, desc in _helm.crd_fields(schema):
                body.append(f"| `{path}` | {ftype} | {'да' if req else ''} | "
                            f"{_helm.show(path, default) if default is not None else ''} | {desc or '—'} |")
            body.append("")
    (out / "api.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    return True


# ---------- Метрики и пакеты ----------

def write_metrics(out, name, ctx, packages) -> bool:
    metrics = [m for p in packages.values() for m in p.metrics]
    if not metrics:
        return False
    body = [page_header(name, "метрики", "code-metrics", ctx),
            "| Метрика | Тип | Labels | Описание | Код |", "|---------|-----|--------|----------|-----|"]
    for m in sorted(metrics, key=lambda m: m.name):
        labels = ", ".join(f"`{l}`" for l in m.labels) or "—"
        llm = ctx.get("llm")
        about = m.help or (f"{llm.metrics[m.name]} {LLM_MARK}" if llm and m.name in llm.metrics else "—")
        body.append(f"| `{m.name}` | {m.type} | {labels} | {about} | `{m.file}:{m.line}` |")
    (out / "metrics.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    return True


def write_packages(out, name, ctx, packages) -> bool:
    documented = {p: pkg for p, pkg in sorted(packages.items()) if pkg.decls and not pkg.is_main}
    if not documented:
        return False
    body = [page_header(name, "пакеты", "code-packages", ctx)]
    for path, pkg in documented.items():
        body.append(f"## {path}\n")
        body.append(f"`package {pkg.name}`\n")
        llm = ctx.get("llm")
        body.append(comment_or_stub(pkg.doc, llm.packages.get(path, "") if llm else "") + "\n")
        for d in pkg.decls:
            title = f"{d.receiver}.{d.name}" if d.receiver else d.name
            body.append(f"### {title}\n")
            body.append(f"`{d.file}:{d.line}` · {d.kind}\n")
            body.append(comment_or_stub(d.comment, llm.decls.get((path, title), "") if llm else "") + "\n")
            body.append(f"```go\n{d.signature}\n```\n")
    (out / "packages.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    return True


# ---------- CHANGELOG ----------

def changelog_section(repo, version, since, release, settings) -> str:
    date = git("log", "-1", "--format=%cs", version, cwd=repo) or today()
    head = f"## [{version}] — {date}" + (f" · платформа {release}" if release else "")
    if not since:
        return f"{head}\n\nПервая версия в документации. Изменения до неё не собраны.\n"
    log = git("log", "--merges", "--first-parent", "--format=%s%x1f%b%x1e", f"{since}..{version}", cwd=repo)
    if log is None:
        raise SystemExit(f"Ошибка: git log {since}..{version} не выполнен в {repo}")
    categories = {**DEFAULT_CATEGORIES, **settings.get("categories", {})}
    task_url = settings.get("task_url", "")
    entries = {}
    for record in filter(None, (r.strip() for r in log.split("\x1e"))):
        subject, _, body = record.partition("\x1f")
        match = MERGE_RE.search(subject)
        if not match:
            continue
        branch = match.group(1)
        category = next((c for p, c in categories.items() if branch.startswith(p)), "Изменено")
        key = TASK_KEY.search(branch)
        text = branch.split("/", 1)[-1]
        if key:
            text = text.split(key.group(), 1)[-1]
        text = text.strip("-_ ").replace("-", " ").replace("_", " ") or subject
        # Заголовок MR из тела merge-коммита GitLab точнее имени ветки.
        title = next((l.strip() for l in body.splitlines()
                      if l.strip() and not l.startswith(("See merge request", IMPACT_PREFIX))), "")
        text = TASK_KEY.sub("", title).strip(" :-[]") or text
        item = f"- {text[0].upper()}{text[1:]}"
        if key:
            ref = f"[{key.group()}]({task_url.format(key=key.group())})" if task_url else key.group()
            item += f" ({ref})"
        impact = next((l.split(":", 1)[1].strip() for l in body.splitlines() if l.startswith(IMPACT_PREFIX)), "")
        if impact:
            item += f"\n  - Влияние на L2/L3: {impact}"
        entries.setdefault(category, []).append(item)
    if not entries:
        return f"{head}\n\nНет merge-веток между `{since}` и `{version}`.\n"
    parts = [head, ""]
    for category in CATEGORY_ORDER + sorted(set(entries) - set(CATEGORY_ORDER)):
        if category in entries:
            parts += [f"### {category}", ""] + entries[category] + [""]
    return "\n".join(parts)


def write_changelog(out, name, ctx, repo, settings) -> None:
    path = out / "CHANGELOG.md"
    if path.is_file():
        text = path.read_text(encoding="utf-8")
        if f"## [{ctx['version']}]" in text:
            return  # версия уже описана; changelog не переписываем
        head, sep, rest = text.partition("\n## [")
        text = head.rstrip() + "\n\n" + changelog_section(repo, ctx["version"], ctx.get("since"),
                                                          ctx.get("release"), settings)
        text += ("\n## [" + rest) if sep else ""
    else:
        text = (frontmatter(title=f"{name} — изменения", type="code-changelog", components=[name],
                            repo=ctx["repo"], generated="true")
                + f"\n# {name} — изменения\n\nОдна merge-ветка — один пункт. Новые версии сверху.\n\n"
                + changelog_section(repo, ctx["version"], ctx.get("since"), ctx.get("release"), settings))
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


# ---------- Версии и клоны ----------

def checkout(repos_dir: Path, name, url, ref) -> Path:
    """Клон компонента в repos_dir/<name> на ref. Partial clone: история без содержимого старых файлов."""
    path = repos_dir / name
    repos_dir.mkdir(parents=True, exist_ok=True)
    if not (path / ".git").exists():
        if git("clone", "-q", "--filter=blob:none", url, str(path), cwd=repos_dir) is None:
            raise SystemExit(f"Ошибка: не удалось клонировать {url}")
    git("fetch", "-q", "--tags", "origin", cwd=path)
    if git("checkout", "-q", "--force", ref, cwd=path) is None:
        raise SystemExit(f"Ошибка: в {url} нет ref {ref}")
    return path


def version_key(version: str):
    match = VERSION_RE.match(version)
    return tuple(int(x) for x in match.groups()) if match else (0, 0, 0)


def git_ref(version: str) -> str:
    """Версия Go-модуля → ref git: псевдоверсия даёт хэш коммита."""
    match = PSEUDO_HASH.search(version)
    return match.group(1) if match else version


def documented_version(name):
    readme = CODE / name / "README.md"
    return read_page(readme).meta.get("version") if readme.is_file() else None


def resolve_name(value: str, registry: dict) -> str:
    """Имя из реестра или URL репозитория (его передаёт CI компонента)."""
    entries = {**registry["components"], **registry["modules"]}
    if value in entries:
        return value
    url = normalize_repo(value)
    for name, entry in entries.items():
        if normalize_repo(entry["repo"]) == url:
            return name
    raise SystemExit(f"Ошибка: «{value}» нет в wiki/code/components.toml")


# ---------- Точка входа ----------

def generate(repo: Path, name: str, version: str, since=None, release=None,
             crd_dirs=(), registry=None, llm=None) -> Path:
    """Создаёт wiki/code/<name>/. Возвращает путь к каталогу."""
    registry = registry or load_registry()
    if name in registry["components"]:
        kind, entry = "component", registry["components"][name]
    elif name in registry["modules"]:
        kind, entry = "module", registry["modules"][name]
    else:
        raise SystemExit(f"Ошибка: «{name}» нет в wiki/code/components.toml")

    config_path = repo / ".docgen.toml"
    config = tomllib.loads(config_path.read_text(encoding="utf-8")) if config_path.is_file() else {}
    exclude = config.get("exclude", [])

    ctx = {"kind": kind, "repo": entry["repo"], "version": version, "since": since, "release": release,
           "platform_modules": {m["module"] for m in registry["modules"].values()},
           "commit": git("rev-parse", "--short=12", "HEAD", cwd=repo) or "?"}
    gomod = _go.parse_go_mod(repo / "go.mod")
    packages = _go.parse_repo(repo, exclude)
    services, messages = _proto.parse_protos(repo, exclude)
    crds = _helm.find_crds([repo / d for d in ("config/crd", "crds", "deploy/crds")] + list(crd_dirs))
    arch = repo / "docs" / "architecture.md"
    ctx["llm"] = _enrich.run(llm, repo, name, kind, gomod["module"], packages, services, messages, crds,
                             arch.read_text(encoding="utf-8") if arch.is_file() else "")

    out = CODE / name
    for stale in ("README.md", "api.md", "metrics.md", "packages.md", "docs"):
        target = out / stale
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()
    out.mkdir(parents=True, exist_ok=True)

    pages = []
    if write_api(out, name, ctx, services, messages, crds):
        pages.append(("api.md", "API"))
    if (out / "config.md").is_file():
        pages.append(("config.md", "Конфигурация чарта"))
    if write_metrics(out, name, ctx, packages):
        pages.append(("metrics.md", "Метрики"))
    if kind == "module" and write_packages(out, name, ctx, packages):
        pages.append(("packages.md", "Пакеты и экспортируемый API"))
    write_changelog(out, name, ctx, repo, registry.get("changelog", {}))
    pages.append(("CHANGELOG.md", "Изменения"))
    write_readme(out, name, repo, ctx, gomod, packages, pages)
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Документация компонента или модуля по тегу.")
    parser.add_argument("name", help="имя из wiki/code/components.toml или URL репозитория")
    parser.add_argument("version", help="тег компонента")
    parser.add_argument("--repo", type=Path, help="локальный репозиторий на этом теге; без него скрипт клонирует сам")
    parser.add_argument("--repos-dir", type=Path, default=ROOT / ".repos", help="кэш клонов")
    parser.add_argument("--since", help="предыдущий тег для CHANGELOG; по умолчанию документированная версия")
    parser.add_argument("--no-llm", action="store_true", help="только факты tree-sitter, без текста LLM")
    args = parser.parse_args(argv)

    registry = load_registry()
    name = resolve_name(args.name, registry)
    entry = registry["components"].get(name) or registry["modules"][name]
    current = documented_version(name)
    if current and version_key(current) > version_key(args.version):
        print(f"Пропуск: wiki/code/{name}/ уже описывает {current}, тег {args.version} старше.")
        return 0
    if current == args.version:
        print(f"Пропуск: wiki/code/{name}/ уже описывает {args.version}.")
        return 0
    since = args.since or current
    repo = args.repo.resolve() if args.repo else checkout(args.repos_dir.resolve(), name, entry["repo"], git_ref(args.version))
    client = _llm.Client(enabled=not args.no_llm)
    out = generate(repo, name, args.version, since, registry=registry, llm=client)
    wiki_index.main([])
    pages = sorted(p.relative_to(CODE.parent).as_posix() for p in out.glob("*.md"))
    enrich = read_page(out / "README.md")
    append_log("code", f"{name} {args.version}", pages,
               f"Предыдущая версия: {since or 'нет'}. {client.summary()}.")
    print(f"Записан каталог wiki/code/{name}/ для {args.version}. {client.summary()}. "
          f"LLM в странице: {enrich.meta.get('llm', 'нет')}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
