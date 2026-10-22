#!/usr/bin/env python3
"""Проверяет wiki: формат страниц, ссылки, границы разделов, секреты, реестр.

Использование:
    python scripts/wiki_lint.py

ОШИБКА даёт код 1. ВНИМАНИЕ код не меняет.

Скил: skills/wiki-lint/SKILL.md
"""
import re
import sys

from _scan import SECRET_PATTERNS
from _wiki import CODE, REGISTRY, ROOT, WIKI, iter_pages, load_registry, local_links

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MIRROR_REQUIRED = ("title", "url", "synced")

PRIVATE_IP = re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b")


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append(f"ОШИБКА    {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"ВНИМАНИЕ  {where}: {msg}")


def check_mirror(page, components, report):
    where = f"wiki/{page.rel}"
    for field in MIRROR_REQUIRED:
        if not page.meta.get(field):
            report.error(where, f"нет поля {field}")
    if page.meta.get("synced") and not DATE_RE.match(str(page.meta["synced"])):
        report.error(where, "synced не в формате ГГГГ-ММ-ДД")
    if not page.values("components"):
        report.warn(where, "нет компонентов: поставь метку component-<имя> в Confluence")
    for name in page.values("components"):
        if name not in components:
            report.warn(where, f"компонента «{name}» нет в реестре")
    if page.section == "l3":
        for target, resolved in local_links(page):
            if not resolved.is_relative_to(WIKI / "l3"):
                report.error(where, f"L3 ссылается за пределы L3: {target}")
        for number, line in enumerate(page.body.splitlines(), start=1):
            if PRIVATE_IP.search(line):
                report.warn(where, f"строка тела {number}: внутренний IP-адрес в L3")


def check_generated(page, report):
    where = f"wiki/{page.rel}"
    if page.section == "code" and "/docs/" in f"/{page.rel}":
        return  # документы команды копируются как есть
    if page.meta.get("generated") != "true":
        report.error(where, f"в {page.section}/ только сгенерированные страницы; правь источник")


def check_links(page, report):
    for target, resolved in local_links(page):
        if not resolved.exists():
            report.error(f"wiki/{page.rel}", f"битая ссылка: {target}")


def check_secrets(report):
    """Секреты ищем во всех .md внутри wiki/, включая raw/. Значение не выводим."""
    for path in sorted(WIKI.rglob("*.md")):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for kind, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    report.error(f"{path.relative_to(ROOT)}:{number}", f"похоже на секрет ({kind})")


def check_registry(registry, report):
    names = set(registry["components"]) | set(registry["modules"])
    where = f"{REGISTRY.relative_to(ROOT)}"
    for kind in ("components", "modules"):
        for name, entry in registry[kind].items():
            need = ("repo", "chart") if kind == "components" else ("repo", "module")
            for field in need + ("owner",):
                if not entry.get(field):
                    report.error(where, f"{name}: нет поля {field}")
    for folder in sorted(p for p in CODE.iterdir() if p.is_dir() and p.name != "releases"):
        if folder.name not in names:
            report.warn(f"wiki/code/{folder.name}", "компонента нет в реестре; удали каталог, если он выведен")


def main(argv=None) -> int:
    report = Report()
    registry = load_registry()
    components = set(registry["components"]) | set(registry["modules"])
    pages = list(iter_pages())
    for page in pages:
        if page.section in ("l2", "l3"):
            check_mirror(page, components, report)
        else:
            check_generated(page, report)
        check_links(page, report)
    check_secrets(report)
    check_registry(registry, report)

    for line in report.errors + report.warnings:
        print(line)
    print(f"Страниц: {len(pages)}. Ошибок: {len(report.errors)}. Предупреждений: {len(report.warnings)}.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
