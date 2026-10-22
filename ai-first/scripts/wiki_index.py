#!/usr/bin/env python3
"""Создаёт wiki/index.md: компоненты, модули, покрытие L2/L3, релизы, страницы L2 и L3.

Использование:
    python scripts/wiki_index.py           записать wiki/index.md
    python scripts/wiki_index.py --check   код 1, если wiki/index.md устарел

Скил: skills/wiki-index/SKILL.md
"""
import argparse
import sys

from _wiki import CHANGES, CODE, INDEX, RAW, RELEASES, iter_pages, load_registry, read_page

CODE_PAGES = [("api.md", "API"), ("config.md", "конфигурация"), ("metrics.md", "метрики"),
              ("packages.md", "пакеты"), ("CHANGELOG.md", "изменения")]


def code_links(name: str) -> str:
    links = [f"[обзор](code/{name}/README.md)"] if (CODE / name / "README.md").is_file() else []
    links += [f"[{title}](code/{name}/{file})" for file, title in CODE_PAGES if (CODE / name / file).is_file()]
    return " · ".join(links) or "нет документации"


def build() -> str:
    registry = load_registry()
    mirror = list(iter_pages(("l2", "l3")))
    lines = [
        "<!-- Файл создан scripts/wiki_index.py. Не редактируй вручную. -->",
        "",
        "# Wiki: каталог",
        "",
        "Начни поиск с `python scripts/wiki_context.py`. Правила — в разделе «LLM Wiki» файла `AGENTS.md`.",
        "",
        "## Компоненты",
        "",
        "Версия — тег, по которому создана документация кода. L2 и L3 — число страниц из Confluence.",
        "",
        "| Компонент | Версия | L2 | L3 | Документация |",
        "|-----------|--------|----|----|--------------|",
    ]
    for name in sorted(registry["components"]):
        readme = CODE / name / "README.md"
        version = read_page(readme).meta.get("version", "—") if readme.is_file() else "—"
        l2 = sum(1 for p in mirror if p.section == "l2" and name in p.values("components")) or "—"
        l3 = sum(1 for p in mirror if p.section == "l3" and name in p.values("components")) or "—"
        lines.append(f"| {name} | `{version}` | {l2} | {l3} | {code_links(name)} |")

    if registry["modules"]:
        lines += ["", "## Общие модули", "", "| Модуль | Версия | Документация |",
                  "|--------|--------|--------------|"]
        for name in sorted(registry["modules"]):
            readme = CODE / name / "README.md"
            version = read_page(readme).meta.get("version", "—") if readme.is_file() else "—"
            lines.append(f"| {name} | `{version}` | {code_links(name)} |")

    changes = sorted(CHANGES.glob("*.md")) if CHANGES.is_dir() else []
    lines += ["", "## Изменения в работе", "",
              "Страницы создаёт CI: `changes_sync.py` после merge спецификации и по расписанию.", ""]
    for path in changes:
        page = read_page(path)
        comps = ", ".join(page.values("components"))
        lines.append(f"- [{page.meta.get('title', path.stem)}](changes/{path.name}) — {comps} · {page.meta.get('status', '?')}")
    if not changes:
        lines.append("Изменений нет.")

    releases = sorted(RELEASES.glob("*.md"), reverse=True) if RELEASES.is_dir() else []
    lines += ["", "## Релизы платформы", ""]
    lines += [f"- [{p.stem}](code/releases/{p.name})" for p in releases] or ["Релизов нет."]

    titles = {"l2": "L2 — линия поддержки", "l3": "L3 — пользовательская документация"}
    for section, title in titles.items():
        pages = [p for p in mirror if p.section == section]
        lines += ["", f"## {title}", ""]
        if not pages:
            lines.append("Страниц нет.")
        for page in pages:
            comps = ", ".join(page.values("components")) or "без компонента"
            lines.append(f"- [{page.meta.get('title', page.path.stem)}]({page.rel}) — {comps}")

    raw_count = sum(1 for _ in RAW.rglob("*.md")) if RAW.is_dir() else 0
    lines += ["", "## Источники", "", f"В `raw/` {raw_count} файлов. Источники не редактируют."]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Создаёт wiki/index.md.")
    parser.add_argument("--check", action="store_true", help="код 1, если index.md устарел")
    args = parser.parse_args(argv)

    content = build()
    current = INDEX.read_text(encoding="utf-8") if INDEX.is_file() else None
    if args.check:
        if content != current:
            print("wiki/index.md устарел. Запусти: python scripts/wiki_index.py")
            return 1
        print("wiki/index.md актуален.")
        return 0

    INDEX.write_text(content, encoding="utf-8")
    print("Записан wiki/index.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
