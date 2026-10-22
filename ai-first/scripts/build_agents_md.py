#!/usr/bin/env python3
"""Собирает AGENTS.md из файлов в rules/.

Использование:
    python scripts/build_agents_md.py           записать AGENTS.md
    python scripts/build_agents_md.py --check   код 1, если AGENTS.md устарел

Скил: skills/build-agents-md/SKILL.md
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = ROOT / "rules"
OUTPUT = ROOT / "AGENTS.md"

# Порядок разделов в AGENTS.md.
RULES = ["karpathy.md", "flow.md", "wiki.md", "pii.md", "writing.md"]

HEADER = """\
<!-- Файл создан scripts/build_agents_md.py из rules/*.md. Не редактируй вручную. -->

# AGENTS.md

Правила для AI-агентов в этом репозитории.

- В начале сессии узнай роль: `python scripts/tracker.py whoami`. Действуй только в рамках своей роли.
- Перед каждой задачей найди контекст в wiki: `python scripts/wiki_context.py --here <слова>`.
- Скилы лежат в `skills/<имя>/SKILL.md`. Каждый скил выполняет скрипт `scripts/<имя>.py`.
- Перед задачей проверь, есть ли подходящий скил. Если есть, используй его скрипт.
- Чтобы изменить правила, измени файл в `rules/` и запусти `python scripts/build_agents_md.py`.
"""

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^#{1,5} ")


def demote_headings(text: str) -> str:
    """Понижает каждый заголовок на один уровень. Код в блоках ``` не меняет."""
    lines, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and HEADING.match(line):
            line = "#" + line
        lines.append(line)
    return "\n".join(lines).strip()


def build() -> str:
    parts = [HEADER.strip()]
    for name in RULES:
        path = RULES_DIR / name
        if not path.is_file():
            sys.exit(f"Ошибка: нет файла {path.relative_to(ROOT)}")
        parts.append(demote_headings(path.read_text(encoding="utf-8")))
    return "\n\n---\n\n".join(parts) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Собирает AGENTS.md из rules/.")
    parser.add_argument("--check", action="store_true",
                        help="не записывать файл; код 1, если AGENTS.md устарел")
    args = parser.parse_args(argv)

    content = build()
    current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.is_file() else None

    if args.check:
        if content != current:
            print("AGENTS.md устарел. Запусти: python scripts/build_agents_md.py")
            return 1
        print("AGENTS.md актуален.")
        return 0

    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Записан {OUTPUT.relative_to(ROOT)}. Разделов: {len(RULES)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
