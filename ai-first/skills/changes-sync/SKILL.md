---
name: changes-sync
description: Используй в CI ai-first после merge спецификации в master-spec и по расписанию. Скил создаёт страницы wiki/changes/<KEY>.md для QA.
---

# changes-sync

Скил пишет страницу изменения из трёх источников: master-spec (`main`), Jira и GitLab. Люди и агенты эти страницы не пишут.

## Запуск

```bash
python scripts/changes_sync.py --master-spec .master-spec --key MK8S-101   # событие: merge change/MK8S-101
python scripts/changes_sync.py --master-spec .master-spec                  # сверка по JQL
```

Без `--key` скрипт берёт задачи с первой меткой из `jira.labels` в статусах Code Review и Ready for QA.
Токены — переменные CI `JIRA_TOKEN`, `GITLAB_TOKEN` бота.

## Страница

- цель и критерии приёмки из intent;
- требования и сценарии из delta-спек — по ним QA проверяет изменение;
- MR спецификации и MR кода с состоянием;
- «Влияние на L2/L3».

Скрипт переписывает страницу, только если её содержание изменилось. Затем обновляет `wiki/index.md` и `wiki/log.md`.

## Результат

Код 0. Задачи, у которых intent или change ещё не влиты, скрипт пропускает и выводит причину.
