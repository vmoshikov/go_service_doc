#!/usr/bin/env python3
"""
Экспорт данных для отчёта KaaS в CSV (закрытый контур).

Использование:
  export DATABASE_URL="postgresql://user:pass@host:5432/dbname"
  python export_to_csv.py [--output csv_export] [--period-days 7]

  # С mTLS (переменные DB_SSL_CERT, DB_SSL_KEY, DB_SSL_ROOTCERT)
  python export_to_csv.py --output csv_export

Выход: CSV-файлы в указанной директории.
"""

import argparse
import os
import sys
from pathlib import Path

# Период подставляется в запросы
QUERIES = [
    ("01_cr_usage", """
        SELECT cr.resource_type, cr.version, COUNT(DISTINCT cr.cluster_uid) AS cluster_count
        FROM conf.custom_resource cr
        JOIN conf.cluster c ON c.uid = cr.cluster_uid AND c.delete_ts IS NULL
        WHERE (cr.deleted IS NULL OR cr.deleted = false) AND cr.modify_ts > now() - interval '%(period)s days'
        GROUP BY cr.resource_type, cr.version ORDER BY cluster_count DESC
    """),
    ("02_clusters_status", """
        SELECT cc.status, COUNT(*) AS cnt FROM state.cluster_consumption cc
        JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days' GROUP BY cc.status
    """),
    ("03_nodes_status", """
        SELECT nc.status, COUNT(*) AS cnt FROM state.node_consumption nc
        JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
        WHERE nc.update_ts > now() - interval '%(period)s days' GROUP BY nc.status
    """),
    ("04_k8s_version", """
        SELECT cc.k8s_version, COUNT(*) AS cnt FROM state.cluster_consumption cc
        JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days' GROUP BY cc.k8s_version
    """),
    ("05_ops_status", """
        SELECT state, COUNT(*) AS cnt FROM operation_v2.operations
        WHERE state_dt > now() - interval '%(period)s days' GROUP BY state
    """),
    ("06_ops_timeline", """
        SELECT DATE(state_dt) AS day,
          SUM(CASE WHEN LOWER(state) IN ('success','completed','done') THEN 1 ELSE 0 END) AS success,
          SUM(CASE WHEN LOWER(state) NOT IN ('success','completed','done') THEN 1 ELSE 0 END) AS failed
        FROM operation_v2.operations WHERE state_dt > now() - interval '%(period)s days'
        GROUP BY DATE(state_dt) ORDER BY day
    """),
    ("07_tasks_action", """
        SELECT COALESCE(action::text, 'null') AS action, COUNT(*) AS cnt FROM operation_v2.tasks
        WHERE state_dt > now() - interval '%(period)s days' GROUP BY action ORDER BY cnt DESC
    """),
    ("08_tasks_operator", """
        SELECT COALESCE(operator::text, 'null') AS operator, COUNT(*) AS cnt FROM operation_v2.tasks
        WHERE state_dt > now() - interval '%(period)s days' GROUP BY operator ORDER BY cnt DESC
    """),
    ("09_tasks_failed_operator", """
        SELECT COALESCE(operator::text, 'null') AS operator, COUNT(*) AS failed_cnt FROM operation_v2.tasks
        WHERE state_dt > now() - interval '%(period)s days'
          AND (error_type IS NOT NULL OR error_message IS NOT NULL)
        GROUP BY operator ORDER BY failed_cnt DESC
    """),
    ("10_tasks_per_op", """
        SELECT task_count, COUNT(*) AS operation_count FROM (
          SELECT operation_id, COUNT(*) AS task_count FROM operation_v2.tasks
          WHERE state_dt > now() - interval '%(period)s days' GROUP BY operation_id
        ) t GROUP BY task_count ORDER BY task_count
    """),
    ("11_tasks_duration", """
        SELECT COALESCE(action::text, 'null') AS action, COUNT(*) AS cnt,
          ROUND(AVG(EXTRACT(EPOCH FROM duration)), 2) AS avg_duration_sec
        FROM operation_v2.tasks WHERE state_dt > now() - interval '%(period)s days' AND duration IS NOT NULL
        GROUP BY action ORDER BY avg_duration_sec DESC NULLS LAST
    """),
    ("12_nodepool_cluster", """
        SELECT c.uid AS cluster_uid, MAX(cc.cluster_ci) AS cluster_ci, c.short_name, MAX(cc.environment) AS env,
          c.di_area_id, COUNT(np.uid) AS nodepool_count
        FROM conf.cluster c
        LEFT JOIN conf.nodepool np ON np.cluster_uid = c.uid AND (np.deleted IS NULL OR np.deleted = false)
        LEFT JOIN state.cluster_consumption cc ON cc.uid = c.uid AND cc.update_ts > now() - interval '%(period)s days'
        WHERE c.delete_ts IS NULL AND c.modify_ts > now() - interval '%(period)s days'
        GROUP BY c.uid, c.short_name, c.di_area_id ORDER BY nodepool_count DESC
    """),
    ("13_node_type", """
        SELECT COALESCE(np.node_type_code::text, 'null') AS node_type_code, COUNT(*) AS cnt
        FROM conf.nodepool np JOIN conf.cluster c ON c.uid = np.cluster_uid AND c.delete_ts IS NULL
        WHERE (np.deleted IS NULL OR np.deleted = false) AND np.modify_ts > now() - interval '%(period)s days'
        GROUP BY np.node_type_code ORDER BY cnt DESC
    """),
    ("14_nodes_per_nodepool", """
        SELECT np.uid AS nodepool_uid, np.name AS nodepool_name, COUNT(n.uid) AS node_count
        FROM conf.nodepool np JOIN conf.cluster c ON c.uid = np.cluster_uid AND c.delete_ts IS NULL
        LEFT JOIN state.node n ON n.nodepool_uid = np.uid
          AND (n.deleted IS NULL OR LOWER(COALESCE(n.deleted::text, '')) NOT IN ('true', '1', 'yes'))
        WHERE (np.deleted IS NULL OR np.deleted = false) AND np.modify_ts > now() - interval '%(period)s days'
        GROUP BY np.uid, np.name ORDER BY node_count DESC
    """),
    ("15_resources_error", """
        SELECT o.name AS operator_name, o.operator_type, COUNT(*) AS resource_count,
          SUM(r.error_count) AS total_error_count
        FROM state.resource r JOIN state.operator o ON r.operator_uuid = o.uuid
        WHERE r.operator_ts > now() - interval '%(period)s days'
          AND (r.error_count > 0 OR r.status ILIKE '%%error%%' OR r.status ILIKE '%%fail%%')
        GROUP BY o.name, o.operator_type ORDER BY total_error_count DESC NULLS LAST
    """),
    ("16_admins", """
        SELECT cluster_uid, admins FROM conf.admins
        WHERE cluster_uid IS NOT NULL AND admins IS NOT NULL AND TRIM(admins::text) != ''
        ORDER BY cluster_uid
    """),
    ("17_cr_clusters", """
        SELECT cr.cluster_uid, MAX(cc.cluster_ci) AS cluster_ci, MAX(c.short_name) AS short_name,
          MAX(cc.environment) AS env, MAX(c.di_area_id) AS di_area_id,
          STRING_AGG(DISTINCT cr.resource_type || ' @ ' || cr.version, ', ' ORDER BY cr.resource_type || ' @ ' || cr.version) AS cr_list
        FROM conf.custom_resource cr
        JOIN conf.cluster c ON c.uid = cr.cluster_uid AND c.delete_ts IS NULL
        LEFT JOIN state.cluster_consumption cc ON cc.uid = cr.cluster_uid AND cc.update_ts > now() - interval '%(period)s days'
        WHERE (cr.deleted IS NULL OR cr.deleted = false) AND cr.modify_ts > now() - interval '%(period)s days'
        GROUP BY cr.cluster_uid ORDER BY cr.cluster_uid
    """),
    ("18_geography", """
        SELECT cc.region, cc.environment, COUNT(*) AS cluster_count
        FROM state.cluster_consumption cc JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
        GROUP BY cc.region, cc.environment ORDER BY cc.region, cc.environment
    """),
    ("19_nodes_region", """
        SELECT nc.region, COUNT(*) AS node_count FROM state.node_consumption nc
        JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
        WHERE nc.update_ts > now() - interval '%(period)s days'
        GROUP BY nc.region ORDER BY node_count DESC
    """),
    ("20_trends", """
        SELECT DATE(cc.update_ts) AS day, SUM(cc.cpu_total) AS cpu_total, SUM(cc.ram_total) AS ram_total, SUM(cc.nod_total) AS nod_total
        FROM state.cluster_consumption cc JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
        GROUP BY DATE(cc.update_ts) ORDER BY day
    """),
    ("21_error_type", """
        SELECT error_type, SUM(cnt) AS cnt FROM (
          SELECT COALESCE(error_type::text, 'null') AS error_type, COUNT(*) AS cnt
          FROM operation_v2.operations WHERE state_dt > now() - interval '%(period)s days' AND error_type IS NOT NULL GROUP BY error_type
          UNION ALL
          SELECT COALESCE(error_type::text, 'null') AS error_type, COUNT(*) AS cnt
          FROM operation_v2.tasks WHERE state_dt > now() - interval '%(period)s days' AND error_type IS NOT NULL GROUP BY error_type
        ) t GROUP BY error_type ORDER BY cnt DESC LIMIT 20
    """),
    ("22_dedicated_shared", """
        SELECT COALESCE(nc.on_dedicated_resources::text, 'unknown') AS resource_type, COUNT(*) AS node_count
        FROM state.node_consumption nc JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
        WHERE nc.update_ts > now() - interval '%(period)s days'
        GROUP BY nc.on_dedicated_resources
    """),
    ("23_environment", """
        SELECT cc.environment, COUNT(*) AS cluster_count FROM state.cluster_consumption cc
        JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
        GROUP BY cc.environment ORDER BY cluster_count DESC
    """),
    ("24_cpu_ram_nod_totals", """
        SELECT SUM(cc.cpu_total) AS cpu_total, SUM(cc.ram_total) AS ram_total, SUM(cc.nod_total) AS nod_total,
          SUM(cc.cpu_running) AS cpu_running, SUM(cc.ram_running) AS ram_running, SUM(cc.nod_running) AS nod_running,
          SUM(cc.cpu_error) AS cpu_error, SUM(cc.ram_error) AS ram_error, SUM(cc.nod_error) AS nod_error
        FROM state.cluster_consumption cc JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
    """),
    ("25_top_cpu", """
        SELECT cc.short_name, cc.cpu_total, cc.cpu_running, cc.cpu_error FROM state.cluster_consumption cc
        JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
        ORDER BY cc.cpu_total DESC NULLS LAST LIMIT 15
    """),
    ("26_top_ram", """
        SELECT cc.short_name, cc.ram_total, cc.ram_running, cc.ram_error FROM state.cluster_consumption cc
        JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
        ORDER BY cc.ram_total DESC NULLS LAST LIMIT 15
    """),
    ("27_top_nod", """
        SELECT cc.short_name, cc.nod_total, cc.nod_running, cc.nod_error FROM state.cluster_consumption cc
        JOIN conf.cluster c ON c.uid = cc.uid AND c.delete_ts IS NULL
        WHERE cc.update_ts > now() - interval '%(period)s days'
        ORDER BY cc.nod_total DESC NULLS LAST LIMIT 15
    """),
    ("28_node_flavor", """
        SELECT nc.flavor, SUM(nc.cpu) AS cpu_total, SUM(nc.ram) AS ram_total, SUM(nc.disk) AS disk_total
        FROM state.node_consumption nc JOIN conf.cluster c ON c.uid = nc.cluster_uid AND c.delete_ts IS NULL
        WHERE nc.update_ts > now() - interval '%(period)s days'
        GROUP BY nc.flavor
    """),
]


def main():
    parser = argparse.ArgumentParser(description="Export KaaS report data to CSV")
    parser.add_argument("--output", "-o", default="csv_export", help="Output directory")
    parser.add_argument("--period-days", "-p", type=int, default=7, help="Period in days")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"), help="PostgreSQL URL")
    args = parser.parse_args()

    if not args.db_url:
        print("Error: DATABASE_URL or --db-url required", file=sys.stderr)
        return 1

    try:
        import pandas as pd
        from sqlalchemy import create_engine
    except ImportError:
        print("Error: pandas and sqlalchemy required. pip install pandas sqlalchemy psycopg2-binary", file=sys.stderr)
        return 1

    base = Path(__file__).parent
    sys.path.insert(0, str(base))
    engine = None
    ssl_cert = os.environ.get("DB_SSL_CERT") or (base / "certs" / "client.pem")
    ssl_key = os.environ.get("DB_SSL_KEY") or (base / "certs" / "client-key.pem")
    ssl_rootcert = os.environ.get("DB_SSL_ROOTCERT") or (base / "certs" / "ca.pem")
    use_ssl = all(Path(p).exists() for p in (ssl_cert, ssl_key, ssl_rootcert))
    try:
        from db_analyzer import get_db_engine
        engine = get_db_engine(
            args.db_url,
            str(ssl_cert) if use_ssl else None,
            str(ssl_key) if use_ssl else None,
            str(ssl_rootcert) if use_ssl else None,
        )
    except Exception:
        url = args.db_url.replace("postgresql://", "postgresql+psycopg2://", 1)
        engine = create_engine(url)

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    params = {"period": str(args.period_days)}

    for name, q in QUERIES:
        try:
            sql = q.strip() % params
            df = pd.read_sql(sql, engine)
            path = out_dir / f"{name}.csv"
            df.to_csv(path, index=False, encoding="utf-8")
            print(f"  {name}.csv ({len(df)} rows)")
        except Exception as e:
            print(f"  {name}.csv FAILED: {e}", file=sys.stderr)

    if engine and hasattr(engine, "dispose"):
        engine.dispose()
    print(f"Done. CSV files in {out_dir}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
