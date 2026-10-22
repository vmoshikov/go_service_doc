---
name: wiki-log
description: Используй, когда меняешь wiki не скриптом релиза: синхронизация, разбор вопроса, ручная проверка. Скил добавляет запись в wiki/log.md.
---

# wiki-log

Журнал показывает, что и когда изменилось в wiki. Записи только добавляются в конец.

## Запуск

```bash
python scripts/wiki_log.py sync "Confluence: пространство SUPPORT" -p l2/etcd-quorum-loss.md -m "Обновлено 3 страницы."
```

Операции: `sync`, `release`, `query`, `lint`. Скрипт `release_docs.py` пишет `release` сам.

## Результат

```
## [2026-10-21] sync | Confluence: пространство SUPPORT
- Страницы: `l2/etcd-quorum-loss.md`
- Итог: Обновлено 3 страницы.
```

Последние записи: `grep "^## \[" wiki/log.md | tail -10`.
