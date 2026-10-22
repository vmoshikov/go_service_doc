"""Общий код для скриптов wiki и генераторов.

Это модуль, а не скил: префикс «_» исключает его из проверки check_skills.py.
"""
import os
import re
import subprocess
import tomllib
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# WIKI_DIR позволяет работать с wiki из репозитория сервиса, например с подмодулем.
WIKI = Path(os.environ.get("WIKI_DIR", ROOT / "wiki")).resolve()
RAW = WIKI / "raw"
CODE = WIKI / "code"
RELEASES = CODE / "releases"
INDEX = WIKI / "index.md"
LOG = WIKI / "log.md"
REGISTRY = CODE / "components.toml"

CHANGES = WIKI / "changes"
SECTIONS = ("l2", "l3", "code", "changes")
LOG_OPS = ("sync", "code", "release", "change", "query", "lint")

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


# ---------- Страницы ----------

@dataclass
class Page:
    path: Path
    meta: dict
    body: str

    @property
    def rel(self) -> str:
        """Путь от корня wiki/, например code/etcd-backup/api.md."""
        return self.path.relative_to(WIKI).as_posix()

    @property
    def section(self) -> str:
        return self.path.relative_to(WIKI).parts[0]

    def values(self, key: str) -> list:
        value = self.meta.get(key)
        if not value:
            return []
        return value if isinstance(value, list) else [value]


def _parse_value(raw: str):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [item.strip().strip("'\"") for item in raw[1:-1].split(",") if item.strip()]
    return raw.strip("'\"")


def read_page(path: Path, text: str = None) -> Page:
    """Читает страницу. Frontmatter — строки «ключ: значение» и списки [a, b]. text — содержимое из git."""
    text = path.read_text(encoding="utf-8") if text is None else text
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        meta = {}
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                return Page(path, meta, "\n".join(lines[i + 1:]))
            key, sep, value = line.partition(":")
            if sep:
                meta[key.strip()] = _parse_value(value)
    return Page(path, {}, text)


def frontmatter(**fields) -> str:
    """Frontmatter в формате, который читает read_page. Пустые поля пропускаются."""
    lines = ["---"]
    for key, value in fields.items():
        if value in (None, "", []):
            continue
        if isinstance(value, (list, tuple)):
            value = "[" + ", ".join(str(v) for v in value) + "]"
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def iter_pages(sections=SECTIONS):
    for section in sections:
        for path in sorted((WIKI / section).rglob("*.md")):
            yield read_page(path)


def local_links(page: Page):
    """Локальные ссылки страницы: (текст ссылки, абсолютный путь)."""
    for target in LINK_RE.findall(page.body):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        target = target.split("#")[0]
        if target:
            yield target, (page.path.parent / target).resolve()


# ---------- Реестр компонентов ----------

def load_registry(path: Path = REGISTRY) -> dict:
    """Читает реестр: разделы charts, components, modules, changelog."""
    if not path.is_file():
        raise SystemExit(f"Ошибка: нет реестра {path}")
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    return {
        "charts": data.get("charts", {}),
        "components": data.get("components", {}),
        "modules": data.get("modules", {}),
        "changelog": data.get("changelog", {}),
    }


def normalize_repo(url: str) -> str:
    """https://user:tok@host/a/b.git и git@host:a/b.git → host/a/b."""
    url = url.strip()
    url = re.sub(r"^[a-z+]+://", "", url)
    url = re.sub(r"^[^@/]+@", "", url)
    url = url.replace(":", "/", 1) if re.match(r"^[^/]+:[^/\d]", url) else url  # git@host:a/b
    url = re.sub(r"^([^/]+):\d+/", r"\1/", url)  # host:8443/a/b
    return url.removesuffix(".git").rstrip("/").lower()


# ---------- Git и прочее ----------

def git(*args: str, cwd: Path = ROOT):
    """Вывод команды git. None, если git недоступен или команда упала."""
    try:
        result = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                                text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def today() -> str:
    return date.today().isoformat()


def append_log(op: str, subject: str, pages: list, summary: str) -> None:
    """Добавляет запись в wiki/log.md. Формат заголовка: ## [ГГГГ-ММ-ДД] op | subject."""
    entry = [f"\n## [{today()}] {op} | {subject}"]
    if pages:
        entry.append("- Страницы: " + ", ".join(f"`{p}`" for p in pages))
    if summary:
        entry.append(f"- Итог: {summary}")
    with LOG.open("a", encoding="utf-8") as f:
        f.write("\n".join(entry) + "\n")
