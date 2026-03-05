#!/bin/bash
# Экспорт данных для отчёта KaaS в CSV (закрытый контур)
#
# Рекомендуется использовать Python-скрипт:
#   python export_to_csv.py --output csv_export --period-days 7
#
# Альтернатива — psql вручную. SQL-запросы в bi_queries/09_export_for_report.sql
# Выполнить каждый запрос и сохранить результат в CSV (DBeaver, pgAdmin, psql \copy).
#
# Пример для psql:
#   psql "$DATABASE_URL" -c "\copy (SELECT ... FROM ...) to '01_cr_usage.csv' with csv header"

echo "Use: python export_to_csv.py --output csv_export"
echo "Or run queries from bi_queries/09_export_for_report.sql manually."
