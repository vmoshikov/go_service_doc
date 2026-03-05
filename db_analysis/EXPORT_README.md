# Экспорт данных для отчёта KaaS в CSV (закрытый контур)

Данные выгружаются из БД в CSV-файлы для последующей генерации отчёта без прямого доступа к БД.

## Способ 1: Python-скрипт (рекомендуется)

```bash
cd db_analysis
export DATABASE_URL="postgresql://user:pass@host:5432/dbname"
# С mTLS (сертификаты в certs/):
export DB_SSL_CERT=certs/client.pem DB_SSL_KEY=certs/client-key.pem DB_SSL_ROOTCERT=certs/ca.pem

python export_to_csv.py --output csv_export --period-days 7
# Или с явным диапазоном дат:
python export_to_csv.py --from-date 2025-01-01 --to-date 2025-01-31
```

**Аргументы (как в db_analyzer.py):**
- `--db-url` — URL подключения (или `DATABASE_URL`)
- `--db-user`, `--db-password` — переопределение учётных данных
- `--ssl-cert`, `--ssl-key`, `--ssl-rootcert` — пути к mTLS сертификатам
- `--output` — директория для CSV (по умолчанию `csv_export`)
- `--period-days` — период в днях (по умолчанию 7)
- `--from-date`, `--to-date` — явный диапазон дат (YYYY-MM-DD)

## Способ 2: psql вручную

Выполнить запросы из `bi_queries/09_export_for_report.sql` и сохранить результаты:

```bash
psql "$DATABASE_URL" -c "\copy (SELECT ...) to '01_cr_usage.csv' with csv header"
```

Или через DBeaver / pgAdmin: выполнить запрос → Export to CSV.

## Список CSV-файлов (28 шт.)

| Файл | Описание |
|------|----------|
| 01_cr_usage | Custom Resource: resource_type, version, cluster_count |
| 02_clusters_status | Кластеры по статусу |
| 03_nodes_status | Ноды по статусу |
| 04_k8s_version | Версии K8s |
| 05_ops_status | Операции по статусу |
| 06_ops_timeline | Операции по дням (success/failed) |
| 07–11 | Tasks: action, operator, failed, per-op, duration |
| 12–14 | Nodepool, node_type, nodes per nodepool |
| 15_resources_error | Ресурсы в ошибке по operator |
| 16_admins | Админы по кластерам |
| 17_cr_clusters | CR на кластер (cluster_ci, short_name, env, cr_list) |
| 18_geography | География (region × environment) |
| 19_nodes_region | Узлы по region |
| 20_trends | Тренды CPU/RAM/NOD по дням |
| 21_error_type | Топ error_type |
| 22_dedicated_shared | Dedicated vs Shared |
| 23_environment | По environment |
| 24–28 | CPU/RAM/NOD totals, top clusters, node flavor |

## Закрытый контур

1. На машине с доступом к БД: запустить `export_to_csv.py` или выполнить SQL из `09_export_for_report.sql`
2. Скопировать папку `csv_export/` на машину без доступа к БД
3. (Отдельная задача) Реализовать загрузку CSV и генерацию report.html
