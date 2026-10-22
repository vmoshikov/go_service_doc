"""Общий код flow ролей: конфиг, роль, master-spec, проверки артефактов, план действий.

Главное правило модуля: команда сначала выполняет все проверки (гейты) и только потом
меняет Jira, GitLab или git. Если гейт не пройден, ничего не меняется.
"""
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

import _config
from _scan import scan
from _wiki import ROOT, load_registry, normalize_repo

ROLES = ("analyst", "developer", "qa")
KEY_RE = re.compile(r"^[A-Z][A-Z0-9]+-\d+$")

INTENT_SECTIONS = ["Источник", "Проблема", "Цель", "Границы", "Компоненты",
                   "Критерии приёмки", "Влияние на L2/L3", "Ограничения", "Открытые вопросы"]

DISCOVERY_CONTEXT = ["Нужная функциональность", "Заказчик и пользователи", "Критичные условия"]
QUESTION_STATUSES = ("открыт", "закрыт", "снят")
SOURCE_REF = re.compile(r"`[^`]*[/.][^`]*`")  # `internal/x.go:12` или `wiki/code/x/api.md`

# Какие файлы может менять каждая роль: аналитик — в папке intent, разработчик — в папке OpenSpec change.
OWNERS = {
    "analyst": ("discovery.md", "intent.md"),
    "developer": ("specs/", "design.md", "tasks.md", ".openspec.yaml"),
}
LOCKED_META = ("schema", "x-jira", "x-intent")  # поля .openspec.yaml, которые разработчик не меняет


class Stop(SystemExit):
    """Гейт не пройден. Скрипт завершается с кодом 1, изменений нет."""

    def __init__(self, *reasons):
        lines = [r for r in reasons if r]
        super().__init__("СТОП. Изменения не выполнены.\n" + "\n".join(f"  - {r}" for r in lines))


def gate(errors: list) -> None:
    if errors:
        raise Stop(*errors)


# ---------- Конфиг и роль ----------

def load_config() -> dict:
    """config.example.json, перекрытый личным config.json."""
    return _config.load()


def local_role():
    return _config.get("role")


def set_role(role: str) -> None:
    data = dict(_config.init_personal())
    data["role"] = role
    _config.save(data)


def require_role(role: str, cfg: dict, gitlab=None) -> None:
    """Роль из config.json. Если задан gitlab.role_groups, роль подтверждает членство в группе GitLab."""
    current = local_role()
    if current is None:
        raise Stop("роль не задана в config.json. Запусти: python scripts/tracker.py setup --role <analyst|developer|qa>")
    if current != role:
        raise Stop(f"команда для роли {role}, а твоя роль — {current}. Агент не выполняет действия другой роли.")
    group = cfg.get("gitlab", {}).get("role_groups", {}).get(role)
    if group and gitlab is not None:
        user = gitlab.user()
        if not gitlab.in_group(group, user["id"]):
            raise Stop(f"пользователь {user['username']} не состоит в группе GitLab {group} (роль {role})")


FRESH_PATHS = ("scripts", "rules", "config.example.json", "templates")
FETCH_EVERY = 30 * 60  # секунд между git fetch ai-first


def require_fresh(cfg: dict) -> None:
    """Стоп, если локальный ai-first отстаёт от origin в скриптах или правилах. У всей команды одна версия flow."""
    if os.environ.get("MK8S_SKIP_FRESHNESS") or git(ROOT, "rev-parse", "--is-inside-work-tree", check=False) != "true":
        return
    stamp = _config.cache_dir() / "ai-first-fetch"
    if not stamp.is_file() or time.time() - stamp.stat().st_mtime > FETCH_EVERY:
        git(ROOT, "fetch", "-q", "origin", check=False)
        stamp.parent.mkdir(parents=True, exist_ok=True)
        stamp.touch()
    base = f"origin/{cfg['gitlab']['default_branch']}"
    if not branch_exists(ROOT, base):
        return
    behind = git(ROOT, "rev-list", "--count", f"HEAD..{base}", "--", *FRESH_PATHS, check=False)
    if behind not in ("", "0"):
        raise Stop(f"ai-first отстаёт от {base}: коммитов со скриптами или правилами — {behind}. "
                   f"Выполни: git -C {ROOT} pull")


def reviewers(gitlab, usernames, exclude: str = "") -> list:
    """ID ревьюеров без автора MR."""
    return gitlab.user_ids([u for u in usernames if u and u != exclude])


def check_key(key: str) -> str:
    if not KEY_RE.match(key):
        raise Stop(f"«{key}» — не ключ Jira. Формат: MK8S-123")
    return key


# ---------- Git ----------

def run(args: list, cwd: Path, check: bool = True) -> str:
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise Stop(f"{' '.join(args[:3])} в {cwd.name}: {result.stderr.strip() or result.stdout.strip()}")
    return result.stdout.strip()


def git(repo: Path, *args, check=True) -> str:
    return run(["git", *args], repo, check)


def is_clean(repo: Path) -> bool:
    return git(repo, "status", "--porcelain") == ""


def foreign_changes(repo: Path, own_prefix: str) -> list:
    """Незакоммиченные файлы вне own_prefix. Свой черновик задачи не мешает повторному start."""
    paths = [line[3:].strip('"') for line in git(repo, "status", "--porcelain", "-uall").splitlines()]
    return [p for p in paths if not p.startswith(own_prefix)]


def current_branch(repo: Path) -> str:
    return git(repo, "rev-parse", "--abbrev-ref", "HEAD")


def remote_url(repo: Path) -> str:
    return git(repo, "remote", "get-url", "origin", check=False)


def branch_exists(repo: Path, ref: str) -> bool:
    return git(repo, "rev-parse", "--verify", "--quiet", ref, check=False) != ""


def switch_branch(repo: Path, branch: str, base: str) -> None:
    """Переключается на branch. Создаёт её от origin/base, если её нет ни локально, ни на сервере.

    Локальная ветка, которая уже влита в origin/base и удалена на сервере, создаётся заново от origin/base.
    """
    merged = branch_exists(repo, branch) and subprocess.run(
        ["git", "merge-base", "--is-ancestor", branch, f"origin/{base}"], cwd=repo).returncode == 0
    if branch_exists(repo, branch) and merged and not branch_exists(repo, f"origin/{branch}"):
        git(repo, "checkout", "-q", "-B", branch, f"origin/{base}")  # старая ветка уже влита: начинаем заново
    elif branch_exists(repo, branch):
        git(repo, "checkout", "-q", branch)
    elif branch_exists(repo, f"origin/{branch}"):
        git(repo, "checkout", "-q", "-b", branch, f"origin/{branch}")
    else:
        git(repo, "checkout", "-q", "-b", branch, f"origin/{base}")


def changed_files(repo: Path, base_ref: str) -> list:
    """[(статус, путь)] от merge-base с base_ref до рабочей копии, включая неотслеживаемые файлы."""
    base = git(repo, "merge-base", base_ref, "HEAD")
    rows = []
    for line in git(repo, "diff", "--name-status", "--no-renames", base).splitlines():
        status_code, _, path = line.partition("\t")
        rows.append((status_code[0], path))
    for path in git(repo, "ls-files", "--others", "--exclude-standard").splitlines():
        rows.append(("A", path))
    return rows


def show_file(repo: Path, ref: str, path: str):
    out = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=repo, capture_output=True, text=True)
    return out.stdout if out.returncode == 0 else None


# ---------- master-spec ----------

def master_spec(cfg: dict) -> Path:
    """Клон master-spec: MASTER_SPEC_DIR или repos.master-spec в config.json."""
    path = Path(os.environ["MASTER_SPEC_DIR"]).resolve() if os.environ.get("MASTER_SPEC_DIR") else _config.repo("master-spec")
    if path is None:
        raise Stop("нет пути к master-spec: заполни repos.master-spec в config.json")
    if not (path / "openspec").is_dir() or not (path / ".git").exists():
        raise Stop(f"нет клона master-spec в {path}. Выполни: git clone {cfg['master_spec']['clone_url']} {path}")
    return path


def resolve_repo(value: str) -> Path:
    """--repo: имя из repos в config.json или путь."""
    return _config.repo(value) or Path(os.path.expanduser(value)).resolve()


CHANGES_REL = "openspec/changes"


def changes_dir(ms: Path) -> Path:
    return ms / CHANGES_REL


def intents_rel(cfg: dict) -> str:
    """Каталог intents от корня master-spec. По умолчанию changes/intents."""
    return cfg["master_spec"]["intents_dir"].strip("/")


def intent_dir(ms: Path, cfg: dict, name: str) -> Path:
    return ms / intents_rel(cfg) / name


def _find(ms: Path, rel: str, key: str, ref, what: str):
    prefix = key.lower() + "-"
    if ref is None:
        folder = ms / rel
        names = [p.name for p in folder.iterdir() if p.is_dir()] if folder.is_dir() else []
    else:
        names = git(ms, "ls-tree", "--name-only", f"{ref}:{rel}", check=False).splitlines()
    found = sorted(n for n in names if n.startswith(prefix))
    if len(found) > 1:
        raise Stop(f"для {key} несколько {what}: {', '.join(found)}. Оставь один.")
    return found[0] if found else None


def find_intent(ms: Path, cfg: dict, key: str, ref=None):
    """Имя папки intent в changes/intents или None. ref=None — рабочая копия, иначе ветка git."""
    return _find(ms, intents_rel(cfg), key, ref, "intent")


RESERVED_CHANGES = ("intents", "archive")  # служебные папки в openspec/changes, не change


def find_change(ms: Path, key: str, ref=None):
    """Имя OpenSpec change в openspec/changes или None. Служебные папки intents и archive не считаются."""
    found = _find(ms, CHANGES_REL, key, ref, "change")
    return None if found in RESERVED_CHANGES else found


def intent_files(ms: Path, cfg: dict, name: str, ref=None):
    """(intent.md, discovery.md) как текст или None: из рабочей копии или из ветки ref."""
    rel = f"{intents_rel(cfg)}/{name}"
    if ref is not None:
        return show_file(ms, ref, f"{rel}/intent.md"), show_file(ms, ref, f"{rel}/discovery.md")
    read = lambda n: (ms / rel / n).read_text(encoding="utf-8") if (ms / rel / n).is_file() else None
    return read("intent.md"), read("discovery.md")


TRANSLIT = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                    ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p",
                     "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya"]))


def slugify(text: str, limit: int = 40) -> str:
    text = "".join(TRANSLIT.get(c, c) for c in text.lower())
    words = re.findall(r"[a-z0-9]+", text)
    slug = ""
    for word in words:
        if len(slug) + len(word) + 1 > limit:
            break
        slug = f"{slug}-{word}" if slug else word
    return slug or "change"


def openspec(ms: Path, *args) -> dict:
    """Вызов OpenSpec CLI с --json."""
    if shutil.which("openspec") is None:
        raise Stop("нет OpenSpec CLI. Установи: npm install -g @fission-ai/openspec")
    result = subprocess.run(["openspec", *args, "--json"], cwd=ms, capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        raise Stop(f"openspec {' '.join(args)}: {result.stderr.strip() or result.stdout.strip()}") from None


def read_meta(text: str) -> dict:
    """Ключи верхнего уровня .openspec.yaml в виде строк."""
    meta = {}
    for line in (text or "").splitlines():
        match = re.match(r"^([\w-]+):\s*(.*)$", line)
        if match:
            meta[match.group(1)] = match.group(2).strip().strip("'\"")
    return meta


# ---------- Разбор markdown ----------

def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def sections(text: str, level: int = 2) -> dict:
    """{заголовок: тело} для заголовков уровня level."""
    marker = "#" * level + " "
    result, title, body = {}, None, []
    for line in strip_comments(text).splitlines():
        if line.startswith(marker):
            if title is not None:
                result[title] = "\n".join(body).strip()
            title, body = line[len(marker):].strip(), []
        elif title is not None:
            body.append(line)
    if title is not None:
        result[title] = "\n".join(body).strip()
    return result


def list_items(text: str) -> list:
    return [m.group(1).strip() for m in re.finditer(r"^\s*(?:[-*]|\d+\.)\s+(.+)$", text, flags=re.M)]


def is_none(text: str) -> bool:
    return text.strip().rstrip(".").lower() in ("нет", "не требуется", "-", "—")


def first_line(text: str) -> str:
    return " ".join(text.split())


# ---------- Проверка discovery ----------

def parse_discovery(text: str) -> dict:
    parts = sections(text)
    questions = []
    for title, body in sections(parts.get("Интервью заказчика", ""), 3).items():
        fields = dict(re.findall(r"^(Ответ|Источник|Статус):[ \t]*(.*)$", body, flags=re.M))
        questions.append({"title": title, **{k: v.strip() for k, v in fields.items()}})
    variants = {}
    for title, body in sections(parts.get("Точки внедрения", ""), 3).items():
        if m := re.match(r"Вариант\s+(\d+)", title):
            line = re.search(r"^\s*-\s*Компоненты:\s*(.+)$", body, flags=re.M)
            names = [c.strip(" `") for c in line.group(1).split(",")] if line else []
            variants[m.group(1)] = {"title": title, "components": [n for n in names if n]}
    chosen = re.search(r"Вариант\s+(\d+)", parts.get("Решение аналитика", ""))
    return {"sections": parts, "context": sections(parts.get("Контекст аналитика", ""), 3),
            "questions": questions, "research": list_items(parts.get("Текущая реализация", "")),
            "variants": variants, "chosen": chosen.group(1) if chosen else None}


def check_context(text) -> list:
    """Гейт перед исследованием: аналитик дал агенту критичный контекст."""
    if text is None:
        return ["нет discovery.md"]
    context = parse_discovery(text)["context"]
    errors = []
    for name in DISCOVERY_CONTEXT:
        body = context.get(name)
        if body is None:
            errors.append(f"discovery.md: нет подраздела «### {name}» в «Контекст аналитика»")
        elif not body or "TODO" in body:
            errors.append(f"discovery.md: аналитик не заполнил «{name}». Агент не исследует без контекста.")
    return errors


def check_discovery(text, registry: dict) -> list:
    """Гейт перед intent: интервью закрыто, исследование со ссылками, вариант выбран."""
    errors = check_context(text)
    if text is None:
        return errors
    d = parse_discovery(text)
    known = set(registry["components"]) | set(registry["modules"])
    if not d["questions"]:
        errors.append("discovery.md: нет вопросов интервью «### В1. ...»")
    for q in d["questions"]:
        name = q["title"].split(".")[0]
        status = q.get("Статус", "").lower().rstrip(".")
        if "TODO" in q["title"]:
            errors.append(f"discovery.md: вопрос {name} не сформулирован")
        if status not in QUESTION_STATUSES:
            errors.append(f"discovery.md: {name}: статус «{q.get('Статус', '')}», нужен один из: {', '.join(QUESTION_STATUSES)}")
        elif status == "открыт":
            errors.append(f"discovery.md: {name} открыт. Аналитик задаёт вопрос заказчику и записывает ответ.")
        else:
            for field in ("Ответ", "Источник"):
                if not q.get(field) or "TODO" in q[field]:
                    errors.append(f"discovery.md: {name}: нет поля «{field}»")
    if not d["research"] or any("TODO" in r for r in d["research"]):
        errors.append("discovery.md: «Текущая реализация» не заполнена. Запусти: analyst.py research")
    for item in d["research"]:
        if "TODO" not in item and not SOURCE_REF.search(item):
            errors.append(f"discovery.md: факт без ссылки на код или wiki: «{item[:60]}»")
    if not d["variants"]:
        errors.append("discovery.md: нет вариантов «### Вариант N: ...» в «Точки внедрения»")
    for number, v in d["variants"].items():
        if not v["components"]:
            errors.append(f"discovery.md: вариант {number}: нет строки «- Компоненты: ...»")
        errors += [f"discovery.md: вариант {number}: компонента «{c}» нет в реестре" for c in v["components"] if c not in known]
    if d["chosen"] is None:
        errors.append("discovery.md: аналитик не выбрал вариант в «Решение аналитика»: «Вариант N. Причина: ...»")
    elif d["chosen"] not in d["variants"]:
        errors.append(f"discovery.md: выбран вариант {d['chosen']}, но его нет в «Точки внедрения»")
    if "TODO" in strip_comments(text):
        errors.append("discovery.md: остались TODO")
    errors += [f"discovery.md:{n}: похоже на {kind}. Удали или обезличь." for n, kind in scan(text)]
    return list(dict.fromkeys(errors))


def chosen_components(discovery_text) -> list:
    d = parse_discovery(discovery_text or "")
    return d["variants"].get(d["chosen"], {}).get("components", [])


# ---------- Проверка intent ----------

def parse_intent(text: str) -> dict:
    parts = sections(text)
    components = [re.split(r"[\s—:(]", c, maxsplit=1)[0].strip("`") for c in list_items(parts.get("Компоненты", ""))]
    return {"sections": parts, "components": components,
            "criteria": list_items(parts.get("Критерии приёмки", "")),
            "impact": parts.get("Влияние на L2/L3", "")}


def check_intent(text, key: str, registry: dict, discovery=None) -> list:
    """Проверка intent и discovery вместе: intent строится из discovery."""
    errors = check_discovery(discovery, registry)
    if text is None:
        return errors + ["нет intent.md. Запусти: analyst.py draft"]
    intent = parse_intent(text)
    parts = intent["sections"]
    for name in INTENT_SECTIONS:
        if name not in parts:
            errors.append(f"intent.md: нет раздела «## {name}»")
        elif not parts[name]:
            errors.append(f"intent.md: раздел «{name}» пуст")
    if "TODO" in strip_comments(text):
        errors.append("intent.md: остались TODO")
    if key not in parts.get("Источник", ""):
        errors.append(f"intent.md: в разделе «Источник» нет ключа {key}")
    known = set(registry["components"]) | set(registry["modules"])
    if "Компоненты" in parts and not intent["components"]:
        errors.append("intent.md: в разделе «Компоненты» нет списка")
    for name in intent["components"]:
        if name not in known:
            errors.append(f"intent.md: компонента «{name}» нет в wiki/code/components.toml")
    if "Критерии приёмки" in parts and not intent["criteria"]:
        errors.append("intent.md: в разделе «Критерии приёмки» нет списка")
    if parts.get("Открытые вопросы") and not is_none(parts["Открытые вопросы"]):
        errors.append("intent.md: есть открытые вопросы. Закрой их с заказчиком и напиши «Нет.»")
    chosen = chosen_components(discovery)
    if chosen and set(intent["components"]) != set(chosen):
        errors.append(f"intent.md: компоненты {', '.join(intent['components'])} не совпадают с выбранным "
                      f"вариантом discovery: {', '.join(chosen)}")
    errors += [f"intent.md:{n}: похоже на {kind}. Удали или обезличь." for n, kind in scan(text)]
    return errors


# ---------- Проверка владения файлами ----------

def owner_prefix(role: str, cfg: dict, name: str) -> str:
    return f"{intents_rel(cfg)}/{name}/" if role == "analyst" else f"{CHANGES_REL}/{name}/"


def check_ownership(files: list, role: str, cfg: dict, name: str) -> list:
    errors = []
    prefix = owner_prefix(role, cfg, name)
    allowed = OWNERS[role]
    for status_code, path in files:
        if not path.startswith(prefix):
            errors.append(f"{path}: роль {role} меняет только {prefix}")
            continue
        rel = path[len(prefix):]
        if not any(rel == a or (a.endswith("/") and rel.startswith(a)) for a in allowed):
            errors.append(f"{path}: файл не принадлежит роли {role}. Её файлы: {', '.join(allowed)}")
    return errors


def check_locked_meta(ms: Path, base_ref: str, change: str, key: str, cfg: dict) -> list:
    """Поля связи change с задачей и intent. Новый change сверяется с ожидаемыми значениями."""
    path = f"{CHANGES_REL}/{change}/.openspec.yaml"
    current = ms / path
    after = read_meta(current.read_text(encoding="utf-8") if current.is_file() else "")
    before = read_meta(show_file(ms, base_ref, path)) or {
        "schema": cfg["master_spec"]["schema"], "x-jira": key, "x-intent": f"{intents_rel(cfg)}/{change}/intent.md"}
    return [f"{path}: поле {k} = {after.get(k)}, ожидается {before.get(k)}"
            for k in LOCKED_META if before.get(k) != after.get(k)]


# ---------- Проверка спецификации разработчика ----------

TASK_GROUP = re.compile(r"^##\s+(?:\d+\.\s*)?(\S+)")
TASK_ITEM = re.compile(r"^\s*-\s+\[([ xX])\]\s+(.+)$")


def parse_tasks(text: str) -> dict:
    """{компонент: [(выполнено, текст)]} по группам «## 1. <компонент>»."""
    groups, current = {}, None
    for line in strip_comments(text).splitlines():
        if m := TASK_GROUP.match(line):
            current = m.group(1).strip("`")
            groups.setdefault(current, [])
        elif (m := TASK_ITEM.match(line)) and current:
            groups[current].append((m.group(1) != " ", m.group(2).strip()))
    return groups


def check_spec(ms: Path, change: str, key: str, cfg: dict, registry: dict):
    """(ошибки, предупреждения, задачи по компонентам)."""
    errors, warnings = [], []
    base = f"origin/{cfg['gitlab']['default_branch']}"
    folder = changes_dir(ms) / change
    main_intent, main_discovery = intent_files(ms, cfg, change, base)
    if main_intent is None:
        errors.append(f"intent нет в {base}:{intents_rel(cfg)}/{change}/. Intent должен быть влит до разработки.")
    if intent_files(ms, cfg, change) != (main_intent, main_discovery):
        errors.append(f"{intents_rel(cfg)}/{change}/ изменён. Intent и discovery меняет только аналитик: developer.py reject")
    intent = parse_intent(main_intent or "")

    result = openspec(ms, "validate", change, "--strict", "--no-interactive")
    for item in result.get("items", []):
        for issue in item.get("issues", []):
            target = errors if issue.get("level") == "ERROR" else warnings
            target.append(f"openspec: {issue.get('path', '')}: {issue.get('message', '')}"[:400])
    if not result.get("items"):
        errors.append(f"openspec validate не нашёл change {change}")
    if (meta := read_meta((folder / ".openspec.yaml").read_text(encoding="utf-8"))).get("x-jira") != key:
        errors.append(f".openspec.yaml: x-jira = {meta.get('x-jira')}, ожидается {key}")

    tasks = {}
    for name in ("design.md", "tasks.md"):
        path = folder / name
        if not path.is_file():
            errors.append(f"нет {name}")
        elif "TODO" in strip_comments(path.read_text(encoding="utf-8")):
            errors.append(f"{name}: остались TODO")
    if (folder / "tasks.md").is_file():
        tasks = parse_tasks((folder / "tasks.md").read_text(encoding="utf-8"))
        if not any(tasks.values()):
            errors.append("tasks.md: нет задач «- [ ] ...» в группах «## 1. <компонент>»")
        for name in tasks:
            if name not in intent["components"]:
                errors.append(f"tasks.md: группа «{name}» не входит в компоненты intent")
        for name in intent["components"]:
            if name not in tasks and name in registry["components"]:
                warnings.append(f"tasks.md: нет задач для компонента {name} из intent")
    for path in sorted(folder.rglob("*.md")):
        for number, kind in scan(path.read_text(encoding="utf-8")):
            errors.append(f"{path.relative_to(ms)}:{number}: похоже на {kind}")
    return errors, warnings, tasks


def component_by_repo(repo: Path, registry: dict):
    url = normalize_repo(remote_url(repo) or "")
    for name, entry in {**registry["components"], **registry["modules"]}.items():
        if normalize_repo(entry["repo"]) == url:
            return name
    return None


# ---------- Метки Jira ----------

def ensure_labels(plan, jira, cfg: dict, issue: dict) -> None:
    """Каждой задаче, которую обработал flow, ставятся метки jira.labels (по умолчанию SDD и TA)."""
    missing = [label for label in cfg["jira"].get("labels", []) if label not in issue.get("labels", [])]
    if missing:
        plan.add(f"Jira {issue['key']}: метки {', '.join(missing)}", lambda: jira.add_labels(issue["key"], missing))


# ---------- План действий ----------

class Plan:
    """Список изменений. Выполняется только после всех гейтов. --dry-run печатает план."""

    def __init__(self, dry_run: bool):
        self.dry_run, self.steps, self.state = dry_run, [], {}

    def add(self, text: str, action) -> None:
        self.steps.append((text, action))

    def run(self) -> None:
        if self.dry_run:
            print("План (--dry-run, изменений нет):")
            for i, (text, _) in enumerate(self.steps, 1):
                print(f"  {i}. {text}")
            return
        for text, action in self.steps:
            action()
            print(f"  ✓ {text}")


def load_all():
    """cfg, registry. Реестр нужен для проверки компонентов intent."""
    return load_config(), load_registry()
