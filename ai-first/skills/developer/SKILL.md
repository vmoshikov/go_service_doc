---
name: developer
description: Используй, если роль — developer. Скил ведёт задачу из Ready for Dev до Ready for QA — change-спека OpenSpec, реализация агентом, MR, страница wiki для QA.
---

# developer

Файлы разработчика: `openspec/changes/<key>-<slug>/` в master-spec: `specs/`, `design.md`, `tasks.md`.
Intent и discovery аналитика (`openspec/changes/intents/<key>-<slug>/`) только для чтения.

## Порядок

| Шаг | Команда | Гейт |
|-----|---------|------|
| 1 | `developer.py queue` | — |
| 2 | `developer.py start <KEY>` | статус Ready for Dev; intent и discovery влиты и проходят проверку |
| 3 | разработчик с агентом пишет `specs/`, `design.md`, `tasks.md` | — |
| 4 | `developer.py check <KEY>` | статус In Progress; файлы своей роли; intent не изменён; `openspec validate --strict`; задачи по компонентам |
| 5 | `developer.py apply <KEY> --repo <компонент>` | спека прошла проверку; репозиторий из реестра; чистая рабочая копия |
| 6 | агент реализует задачи компонента и отмечает `[x]` после проверки | — |
| 7 | `developer.py submit <KEY> --repo <компонент>` | все задачи компонента выполнены; есть коммиты |
| 8 | лид проверяет и вливает MR спецификации и MR кода | CI `spec_guard.py` |
| 9 | `developer.py done <KEY>` | MR спецификации влит; MR кода влит (`gates.qa_requires`) |

`--repo` принимает имя из `repos` в `config.json` или путь.

## Если intent неясен

```bash
python scripts/developer.py reject MK8S-101 --reason "Не указан лимит по умолчанию и поведение при превышении."
```

Задача уходит аналитику (Analysis). Не исправляй intent и discovery сам.

## Результат done

- Статус Jira — Ready for QA, комментарий для QA.
- Страницу `wiki/changes/<KEY>.md` создаёт CI wiki после merge спецификации (скил `changes-sync`). Разработчик wiki не пишет.

## Ревьюеры

`submit` назначает ревьюерами MR логины из поля `reviewers` компонента в `wiki/code/components.toml`.
MR спецификации получает ревьюеров всех компонентов из `tasks.md` и `review.spec_reviewers`.

## Команды, которые меняют Jira, GitLab или git

`start`, `apply`, `submit`, `done`, `reject`. Сначала запусти с `--dry-run` и покажи план человеку.
