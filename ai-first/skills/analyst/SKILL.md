---
name: analyst
description: Используй, если роль — analyst. Скил ведёт CR из Jira до intent в master-spec — контекст аналитика, исследование агентом, интервью заказчика, выбор точки внедрения, intent, ревью.
---

# analyst

Файлы аналитика: `openspec/changes/intents/<key>-<slug>/discovery.md` и `intent.md` в master-spec.
Они приходят в master-spec через MR из ветки `intent/<KEY>`. Ревьюеры — `review.intent_reviewers` в конфиге.

## Порядок

| Шаг | Кто | Команда или действие | Гейт |
|-----|-----|----------------------|------|
| 1 | аналитик | `analyst.py inbox` | — |
| 2 | аналитик | `analyst.py start <KEY>` | тип CR, статус Open |
| 3 | **аналитик** | пишет «Контекст аналитика» в `discovery.md` | — |
| 4 | агент | `analyst.py research <KEY> -c <компонент>` → «Текущая реализация», вопросы, точки внедрения | контекст заполнен |
| 5 | **аналитик** | задаёт вопросы заказчику, пишет ответы и источник; `analyst.py interview <KEY>` | — |
| 6 | **аналитик** | выбирает вариант: «Вариант N. Причина: …» | — |
| 7 | агент | `analyst.py draft <KEY>` → intent из discovery | интервью закрыто, факты со ссылками, вариант выбран |
| 8 | аналитик | `analyst.py check <KEY>`, `analyst.py submit <KEY>` | intent полный, компоненты = выбранный вариант, нет ПДн |
| 9 | лид | ревью и merge MR intent в master-spec | CI `spec_guard.py` |
| 10 | аналитик | `analyst.py publish <KEY>` | MR влит |

## Что агент не делает

- Не пишет «Контекст аналитика», ответы интервью и «Решение аналитика».
- Не меняет код в клонах из `research`: они только для чтения.
- Не пишет факт о текущей реализации без ссылки `путь:строка` или `wiki/...`.
- Не добавляет в intent требований, которых нет в discovery и CR.

## Команды, которые меняют Jira, GitLab или git

`start`, `research`, `submit`, `publish`. Сначала запусти с `--dry-run` и покажи план человеку.

## Доработка

Если разработчик вернул intent (`developer.py reject`), задача снова в Analysis.
Запусти `analyst.py start <KEY>`: скрипт создаёт ветку `intent/<KEY>` от main и показывает причину возврата.
