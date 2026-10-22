#!/usr/bin/env python3
"""Проверка MR в master-spec: каждая роль меняет только свои файлы своего change.

Использование (CI master-spec или локально):
    python scripts/spec_guard.py --repo <путь к master-spec> [--branch <ветка>] [--base <ветка>]

Роль определяет префикс ветки:
    intent/<KEY>    — аналитик: только <intents_dir>/<id>/discovery.md и intent.md; оба проходят проверку
    change/<KEY>    — разработчик: только openspec/changes/<id>/ (specs/, design.md, tasks.md, .openspec.yaml);
                      intents не меняются; openspec validate --strict
    platform/<имя>  — сопровождение: только openspec/schemas/, openspec/config.yaml и файлы вне openspec/ и intents

Другие ветки и прямые изменения openspec/specs/ отклоняются: main-спеки меняет только openspec archive (этап QA).

Скил: skills/spec-guard/SKILL.md
"""
import argparse
import os
import sys
from pathlib import Path

from _flow import (Stop, changed_files, check_intent, check_key, check_locked_meta, check_ownership,
                   check_spec, find_change, find_intent, gate, git, intent_files, intents_rel, load_all)


def guard_platform(files, intents: str) -> list:
    errors = []
    for _, path in files:
        if path.startswith(intents + "/") or (path.startswith("openspec/") and not (
                path.startswith("openspec/schemas/") or path == "openspec/config.yaml")):
            errors.append(f"{path}: ветка platform/ не меняет intents, change и спеки")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Проверка MR в master-spec по роли ветки.")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--branch", default=os.environ.get("CI_MERGE_REQUEST_SOURCE_BRANCH_NAME"))
    parser.add_argument("--base", default=os.environ.get("CI_MERGE_REQUEST_TARGET_BRANCH_NAME"))
    args = parser.parse_args(argv)

    cfg, registry = load_all()
    ms = args.repo.resolve()
    branch = args.branch or git(ms, "rev-parse", "--abbrev-ref", "HEAD")
    base_ref = f"origin/{args.base or cfg['gitlab']['default_branch']}"
    files = changed_files(ms, base_ref)
    kind, _, name = branch.partition("/")
    print(f"Ветка {branch} → {base_ref}. Изменено файлов: {len(files)}.")

    if kind == "platform":
        gate(guard_platform(files, intents_rel(cfg)))
    elif kind in ("intent", "change"):
        key = check_key(name)
        role = "analyst" if kind == "intent" else "developer"
        change = find_intent(ms, cfg, key) if role == "analyst" else find_change(ms, key)
        if not change:
            raise Stop(f"в ветке нет {'intent' if role == 'analyst' else 'OpenSpec change'} для {key}")
        errors = check_ownership(files, role, cfg, change)
        if role == "analyst":
            intent, discovery = intent_files(ms, cfg, change)
            errors += check_intent(intent, key, registry, discovery)
        else:
            errors += check_locked_meta(ms, base_ref, change, key, cfg)
            spec_errors, warnings, _ = check_spec(ms, change, key, cfg, registry)
            errors += spec_errors
            for w in warnings:
                print(f"ВНИМАНИЕ  {w}")
        gate(errors)
    else:
        raise Stop(f"ветка «{branch}» не разрешена. Префиксы: intent/<KEY>, change/<KEY>, platform/<имя>")
    print("Проверка пройдена.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
