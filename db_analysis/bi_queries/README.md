# SQL-запросы для BI-инструментов KaaS

Готовые SQL-запросы для Metabase, Tableau, Power BI, Superset и др.

## Маппинг: запрос → чарт → дашборд

| Файл | Запрос | Тип чарта | Дашборд |
|------|--------|-----------|---------|
| 01_clusters_resources.sql | Q1 | Bar | Кластеры и ресурсы |
| 01_clusters_resources.sql | Q2 | Stacked Bar | Кластеры и ресурсы |
| 01_clusters_resources.sql | Q3 | Pie | Кластеры и ресурсы |
| 01_clusters_resources.sql | Q4 | Table | Кластеры и ресурсы |
| 01_clusters_resources.sql | Q5 | Bar | Кластеры и ресурсы |
| 02_operations_slo.sql | Q1 | Pie | Операции и SLO |
| 02_operations_slo.sql | Q2 | Line | Операции и SLO |
| 02_operations_slo.sql | Q3 | Bar | Операции и SLO |
| 02_operations_slo.sql | Q4 | Table | Операции и SLO |
| 02_operations_slo.sql | Q5 | Gauge/KPI | Операции и SLO |
| 03_errors.sql | Q1 | Bar | Ошибки |
| 03_errors.sql | Q2 | Bar | Ошибки |
| 03_errors.sql | Q3 | Table | Ошибки |
| 03_errors.sql | Q4 | Stacked Bar | Ошибки |
| 04_config_admins.sql | Q1 | Table | Конфигурация |
| 04_config_admins.sql | Q2 | Bar | Конфигурация |
| 04_config_admins.sql | Q3 | Table | Конфигурация |
| 04_config_admins.sql | Q4 | Table | Конфигурация |
| 05_geography.sql | Q1 | Heatmap/Table | География |
| 05_geography.sql | Q2 | Bar | География |
| 05_geography.sql | Q3 | Bar | География |
| 06_consumption_trends.sql | Q1 | Line | Тренды потребления |
| 06_consumption_trends.sql | Q2 | Line | Тренды потребления |
| 06_consumption_trends.sql | Q3 | Area | Тренды потребления |

## Подключение к BI

- **Metabase**: Database → Add database → PostgreSQL. Используйте параметры mTLS в connection string.
- **Tableau**: Connect to PostgreSQL, указать JDBC URL с SSL.
- **Power BI**: Get Data → PostgreSQL.
- **Superset**: Databases → + Database → PostgreSQL.

## Плейсхолдеры

В запросах используются опциональные фильтры:
- `:period_start` — начало периода (timestamp)
- `:period_end` — конец периода (timestamp)

В Metabase: `{{period_start}}`, `{{period_end}}`.
В Tableau: замените на параметры.
