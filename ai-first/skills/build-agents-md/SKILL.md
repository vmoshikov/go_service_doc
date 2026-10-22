---
name: build-agents-md
description: Используй после любого изменения файлов в rules/. Скил собирает AGENTS.md из файлов rules/ в порядке списка RULES.
---

# build-agents-md

Скил собирает `AGENTS.md` из файлов в `rules/`. Не редактируй `AGENTS.md` вручную.

## Запуск

1. Измени нужный файл в `rules/`.
2. Запусти сборку:

   ```bash
   python scripts/build_agents_md.py
   ```

3. Добавь в коммит файл из `rules/` и `AGENTS.md`.

## Проверка в CI

```bash
python scripts/build_agents_md.py --check
```

Код 1 — `AGENTS.md` не совпадает с `rules/`. Запусти сборку и сделай коммит.

## Новый раздел

1. Создай файл `rules/<раздел>.md` с заголовком первого уровня.
2. Добавь имя файла в список `RULES` в `scripts/build_agents_md.py`.
3. Запусти сборку.
