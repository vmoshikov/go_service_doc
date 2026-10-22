---
name: spec-guard
description: Используй в CI master-spec и перед отправкой MR. Скил проверяет, что ветка меняет только файлы своей роли и что intent и спека проходят проверку.
---

# spec-guard

## Запуск

```bash
python scripts/spec_guard.py --repo <путь к master-spec>
python scripts/spec_guard.py --repo . --branch change/MK8S-101 --base main
```

В CI GitLab ветки берутся из `CI_MERGE_REQUEST_SOURCE_BRANCH_NAME` и `CI_MERGE_REQUEST_TARGET_BRANCH_NAME`.
Готовый job — `templates/master-spec/.gitlab-ci.yml`.

## Правила по веткам

| Ветка | Роль | Можно менять | Проверка |
|-------|------|--------------|----------|
| `intent/<KEY>` | аналитик | `openspec/changes/intents/<id>/discovery.md`, `intent.md` | discovery и intent полные, нет ПДн |
| `change/<KEY>` | разработчик | `openspec/changes/<id>/` | intent не изменён, `x-jira` и `x-intent` верны, `openspec validate --strict` |
| `platform/<имя>` | сопровождение | `openspec/schemas/`, `openspec/config.yaml`, файлы вне `openspec/` | — |

Служебный файл `openspec/changes/intents/.openspec.yaml` не может менять ни одна ветка.

Другие ветки отклоняются. `openspec/specs/` меняет только `openspec archive` на этапе QA.

## Результат

Код 0 — проверка пройдена. Код 1 — скрипт выводит причины.
