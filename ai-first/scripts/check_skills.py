#!/usr/bin/env python3
"""Проверяет связь скилов и скриптов.

Правила:
  1. У каждого skills/<имя>/SKILL.md есть frontmatter с полями name и description.
  2. Поле name совпадает с именем папки.
  3. Для каждого скила есть scripts/<имя_в_snake_case>.py.
  4. Для каждого scripts/*.py есть скил. Файлы с префиксом «_» — общие модули, их не проверяем.

Использование:
    python scripts/check_skills.py    код 1, если есть ошибки

Скил: skills/check-skills/SKILL.md
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
SCRIPTS_DIR = ROOT / "scripts"


def read_frontmatter(path: Path) -> dict:
    """Читает поля «ключ: значение» между первыми двумя строками «---»."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return {}  # нет закрывающей строки «---»


def main() -> int:
    errors = []
    skill_modules = set()

    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        rel = skill_dir.relative_to(ROOT)
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{rel}: нет SKILL.md")
            continue

        meta = read_frontmatter(skill_file)
        for field in ("name", "description"):
            if not meta.get(field):
                errors.append(f"{rel}/SKILL.md: нет поля {field} во frontmatter")
        if meta.get("name") and meta["name"] != skill_dir.name:
            errors.append(f"{rel}/SKILL.md: name «{meta['name']}» не совпадает с папкой «{skill_dir.name}»")

        module = skill_dir.name.replace("-", "_")
        skill_modules.add(module)
        if not (SCRIPTS_DIR / f"{module}.py").is_file():
            errors.append(f"{rel}: нет скрипта scripts/{module}.py")

    for script in sorted(SCRIPTS_DIR.glob("*.py")):
        if script.stem.startswith("_"):
            continue
        if script.stem not in skill_modules:
            skill_name = script.stem.replace("_", "-")
            errors.append(f"scripts/{script.name}: нет скила skills/{skill_name}/SKILL.md")

    for error in errors:
        print(f"ОШИБКА  {error}")
    if errors:
        return 1
    print(f"Скилы в порядке: {len(skill_modules)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
