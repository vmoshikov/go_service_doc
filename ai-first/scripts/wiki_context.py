#!/usr/bin/env python3
"""Находит страницы wiki, которые нужно прочитать перед задачей.

Использование:
    python scripts/wiki_context.py [слова ...] [-c компонент] [--here] [--section l2|l3|code]

Примеры:
    python scripts/wiki_context.py --here retention
    python scripts/wiki_context.py -c etcd-backup s3
    python scripts/wiki_context.py --section l3 бэкап

--here определяет компонент по git remote текущего каталога и реестру wiki/code/components.toml.

Скил: skills/wiki-context/SKILL.md
"""
import argparse
import sys
from pathlib import Path

from _wiki import SECTIONS, git, iter_pages, load_registry, normalize_repo


def component_here() -> list:
    remote = git("remote", "get-url", "origin", cwd=Path.cwd())
    if not remote:
        return []
    registry = load_registry()
    entries = {**registry["components"], **registry["modules"]}
    return [name for name, entry in entries.items() if normalize_repo(entry["repo"]) == normalize_repo(remote)]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Находит страницы wiki для задачи.")
    parser.add_argument("words", nargs="*", help="ключевые слова задачи")
    parser.add_argument("-c", "--component", action="append", default=[])
    parser.add_argument("--here", action="store_true", help="компонент текущего git-репозитория")
    parser.add_argument("--section", choices=SECTIONS)
    parser.add_argument("--limit", type=int, default=15)
    args = parser.parse_args(argv)

    components = set(args.component)
    if args.here:
        found = component_here()
        if not found:
            print("Текущий репозиторий не найден в wiki/code/components.toml.", file=sys.stderr)
        components.update(found)
    if not (args.words or components):
        parser.error("укажи слова, компонент (-c) или --here")

    words = [w.lower() for w in args.words]
    results = []
    for page in iter_pages():
        if args.section and page.section != args.section:
            continue
        score = 5 * len(components & set(page.values("components")))
        title = str(page.meta.get("title", "")).lower()
        body = page.body.lower()
        for word in words:
            if word in title:
                score += 3
            elif word in body:
                score += 1
        if page.meta.get("type") == "release":
            score -= 2  # страница релиза перечисляет все компоненты; она нужна реже
        if score > 0:
            results.append((score, page))

    if components:
        print(f"Компоненты: {', '.join(sorted(components))}")
    if not results:
        print("Страниц не найдено. Прочитай wiki/index.md.")
        return 0

    results.sort(key=lambda item: (-item[0], item[1].rel))
    for score, page in results[: args.limit]:
        kind = page.meta.get("type") or page.section
        print(f"{score:3d}  {kind:15s} wiki/{page.rel}  — {page.meta.get('title') or page.path.stem}")
    if len(results) > args.limit:
        print(f"... ещё {len(results) - args.limit}. Увеличь --limit или уточни запрос.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
