# План анализа данных по структуре БД KaaS

## Цели анализа

- Описание схем и таблиц (conf, state, operation_v2)
- Анализ колонок и типов данных
- Выявление ключевых полей (uid, *_uid, *_id) для связей
- Определение полей для временных фильтров (max_value_column, where)
- Стратегия инкрементальной загрузки (24h по modify_ts/operator_ts/state_dt)

## Схемы и таблицы

| Схема | Таблицы | Назначение |
|-------|---------|------------|
| conf | cluster, nodepool, admins, custom_resource | Конфигурационные данные |
| state | node, resource, operator, cluster_consumption, node_consumption | Состояние системы |
| operation_v2 | operations, tasks | Операции и задачи |

## Ключевые поля для связей

- `cluster.uid` — связь с nodepool (cluster_uid), admins (cluster_uid), custom_resource (cluster_uid), operator (cluster_uid), operations (cluster_id), tasks (cluster_id), node_consumption (cluster_uid)
- `nodepool.uid` — связь с node (nodepool_uid)
- `operator.uuid` — связь с resource (operator_uuid)
- `operations.id` — связь с tasks (operation_id)

## Временные фильтры

| Таблица | max_value_column | Where (24h) |
|---------|------------------|-------------|
| cluster, nodepool, node, custom_resource | modify_ts | modify_ts > now() - interval '24 hours' |
| resource | operator_ts | operator_ts > now() - interval '24 hours' |
| operator | start_ts | start_ts > now() - interval '24 hours' |
| operations, tasks | state_dt | state_dt > now() - interval '24 hours' |
| cluster_consumption, node_consumption | update_ts | update_ts > now() - interval '24 hours' |
| admins | — | cluster_uid is not null |

## Этапы выполнения

1. Загрузка метаданных из `db_schema.json`
2. Подключение к БД (PostgreSQL) через JDBC с mTLS
3. Выполнение запросов с учётом `where` для каждой таблицы
4. Агрегация в pandas DataFrame
5. Экспорт в HTML-отчёты
