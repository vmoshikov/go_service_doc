#!/usr/bin/env python3
"""Добавляет запись в журнал wiki/log.md.

Использование:
    python scripts/wiki_log.py <операция> "<тема>" -p <страница> [-p ...] [-m "<итог>"]

Операции: sync, release, query, lint. release_docs.py пишет release сам.
Страница — путь от wiki/, например code/etcd-backup/README.md.

Скил: skills/wiki-log/SKILL.md
"""
import argparse
import sys

from _wiki import LOG_OPS, WIKI, append_log


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Добавляет запись в wiki/log.md.")
    parser.add_argument("op", choices=LOG_OPS)
    parser.add_argument("subject", help="тема записи или путь к источнику")
    parser.add_argument("-p", "--page", action="append", default=[], help="изменённая страница")
    parser.add_argument("-m", "--summary", default="", help="итог в одном предложении")
    args = parser.parse_args(argv)

    missing = [p for p in args.page if not (WIKI / p).is_file()]
    if missing:
        print(f"Ошибка: нет страниц в wiki/: {', '.join(missing)}", file=sys.stderr)
        return 1

    append_log(args.op, args.subject, args.page, args.summary)
    print("Запись добавлена в wiki/log.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
