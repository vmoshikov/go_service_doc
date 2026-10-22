#!/usr/bin/env python3
"""Создаёт страницы wiki/changes/<KEY>.md из master-spec, Jira и GitLab. Запускает только CI wiki-репозитория.

Использование:
    python scripts/changes_sync.py --master-spec <путь> [--key <KEY> ...]

Без --key скрипт обрабатывает задачи по JQL: метка flow и статусы Code Review и Ready for QA.
Страница переписывается, только если её содержание изменилось. Скрипт обновляет wiki/index.md и пишет wiki/log.md.

Скил: skills/changes-sync/SKILL.md
"""
import argparse
import os
import sys
from pathlib import Path

import _changes
import wiki_index
from _flow import check_key, git, load_all
from _tracker import GitLab, Jira
from _wiki import CHANGES, append_log, read_page


def default_jql(cfg) -> str:
    st = cfg["jira"]["status"]
    label = cfg["jira"]["labels"][0]
    return (f'project = {cfg["jira"]["project"]} AND labels = "{label}" '
            f'AND status in ("{st["code_review"]}", "{st["ready_for_qa"]}")')


def strip_updated(text: str) -> str:
    """Текст без строки updated: сравнение не реагирует на смену даты."""
    return "\n".join(line for line in text.splitlines() if not line.startswith("updated:"))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Страницы изменений в wiki/changes/.")
    parser.add_argument("--master-spec", type=Path, default=os.environ.get("MASTER_SPEC_DIR"), required=False,
                        help="клон master-spec; по умолчанию MASTER_SPEC_DIR")
    parser.add_argument("--key", action="append", default=[], help="ключ задачи; можно повторять")
    args = parser.parse_args(argv)
    if not args.master_spec:
        parser.error("укажи --master-spec или MASTER_SPEC_DIR")

    cfg, registry = load_all()
    jira, gitlab = Jira(cfg["jira"]), GitLab(cfg["gitlab"])
    ms = args.master_spec.resolve()
    git(ms, "fetch", "-q", "origin")
    keys = [check_key(k) for k in args.key] or [row["key"] for row in jira.search(default_jql(cfg), 200)]

    written, skipped = [], []
    CHANGES.mkdir(parents=True, exist_ok=True)
    for key in keys:
        text, reason = _changes.page(cfg, registry, jira, gitlab, ms, key)
        if text is None:
            skipped.append(reason)
            continue
        path = CHANGES / f"{key}.md"
        old = path.read_text(encoding="utf-8") if path.is_file() else ""
        if strip_updated(old) == strip_updated(text):
            continue
        path.write_text(text, encoding="utf-8")
        written.append(f"changes/{key}.md")
        append_log("change", key, [f"changes/{key}.md"], f"Статус Jira: {read_page(path).meta.get('status')}.")

    if written:
        wiki_index.main([])
    for reason in skipped:
        print(f"пропуск  {reason}")
    print(f"Задач: {len(keys)}. Обновлено страниц: {len(written)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
