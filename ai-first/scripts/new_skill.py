#!/usr/bin/env python3
"""Создаёт заготовку нового скила: skills/<имя>/SKILL.md и scripts/<имя>.py.

Использование:
    python scripts/new_skill.py <имя> "<когда использовать>"

Имя — kebab-case, например `export-report`. Файл скрипта получает имя в snake_case: `export_report.py`.

Скил: skills/new-skill/SKILL.md
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")

SKILL_TEMPLATE = """\
---
name: {name}
description: {description}
---

# {name}

{description}

## Запуск

```bash
python scripts/{module}.py --help
```

## Результат

TODO: опиши, что скрипт создаёт или выводит. Код возврата 0 — успех.
"""

SCRIPT_TEMPLATE = '''\
#!/usr/bin/env python3
"""{description}

Скил: skills/{name}/SKILL.md
"""
import argparse
import sys


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.parse_args(argv)
    print("TODO: реализуй скил {name}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
'''


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Создаёт заготовку нового скила.")
    parser.add_argument("name", help="имя скила в kebab-case")
    parser.add_argument("description", help="одно предложение: когда использовать скил")
    args = parser.parse_args(argv)

    if not NAME_RE.match(args.name):
        print(f"Ошибка: имя «{args.name}» не в kebab-case. Пример: export-report", file=sys.stderr)
        return 1

    module = args.name.replace("-", "_")
    skill_file = ROOT / "skills" / args.name / "SKILL.md"
    script_file = ROOT / "scripts" / f"{module}.py"

    for path in (skill_file, script_file):
        if path.exists():
            print(f"Ошибка: {path.relative_to(ROOT)} уже существует.", file=sys.stderr)
            return 1

    values = {"name": args.name, "module": module, "description": args.description.strip()}
    skill_file.parent.mkdir(parents=True)
    skill_file.write_text(SKILL_TEMPLATE.format(**values), encoding="utf-8")
    script_file.write_text(SCRIPT_TEMPLATE.format(**values), encoding="utf-8")
    script_file.chmod(0o755)

    print(f"Создан {skill_file.relative_to(ROOT)}")
    print(f"Создан {script_file.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
