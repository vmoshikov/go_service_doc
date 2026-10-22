<!-- Файл создан scripts/wiki_index.py. Не редактируй вручную. -->

# Wiki: каталог

Начни поиск с `python scripts/wiki_context.py`. Правила — в разделе «LLM Wiki» файла `AGENTS.md`.

## Компоненты

Версия — тег, по которому создана документация кода. L2 и L3 — число страниц из Confluence.

| Компонент | Версия | L2 | L3 | Документация |
|-----------|--------|----|----|--------------|
| api-gateway | `v2.0.0` | — | — | [обзор](code/api-gateway/README.md) · [конфигурация](code/api-gateway/config.md) · [изменения](code/api-gateway/CHANGELOG.md) |
| etcd-backup | `v1.5.0` | — | — | [обзор](code/etcd-backup/README.md) · [API](code/etcd-backup/api.md) · [конфигурация](code/etcd-backup/config.md) · [метрики](code/etcd-backup/metrics.md) · [изменения](code/etcd-backup/CHANGELOG.md) |

## Общие модули

| Модуль | Версия | Документация |
|--------|--------|--------------|
| core | `v1.2.0` | [обзор](code/core/README.md) · [пакеты](code/core/packages.md) · [изменения](code/core/CHANGELOG.md) |

## Изменения в работе

Страницы создаёт CI: `changes_sync.py` после merge спецификации и по расписанию.

- [MK8S-101: Инкрементальные бэкапы etcd](changes/MK8S-101.md) — etcd-backup · Ready for QA

## Релизы платформы

- [2026.11.0](code/releases/2026.11.0.md)
- [2026.10.1](code/releases/2026.10.1.md)
- [2026.10.0](code/releases/2026.10.0.md)

## L2 — линия поддержки

Страниц нет.

## L3 — пользовательская документация

Страниц нет.

## Источники

В `raw/` 0 файлов. Источники не редактируют.
