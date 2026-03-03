#!/usr/bin/env python3
"""
KaaS DB Analyzer — анализ данных БД и генерация HTML-отчётов.

Подключение: JDBC mTLS PostgreSQL.
Дашборды: Кластеры и ресурсы, Операции и SLO, Ошибки, Конфигурация, География, Тренды потребления.
"""

import argparse
import json
import os
from pathlib import Path
from typing import Any

import pandas as pd


def load_schema(config_path: Path) -> list[dict]:
    """Загрузка конфигурации схемы БД из JSON."""
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


def get_jdbc_connection(jdbc_url: str, jdbc_jar: str) -> Any:
    """Подключение к PostgreSQL через JDBC с mTLS."""
    import jaydebeapi

    driver = "org.postgresql.Driver"
    conn = jaydebeapi.connect(jclassname=driver, url=jdbc_url, jars=[jdbc_jar])
    return conn


def fetch_table(conn: Any, schema: str, table: str, columns: str, where: str | None) -> pd.DataFrame:
    """Чтение таблицы в DataFrame."""
    cols = columns.split(",")
    cols_str = ", ".join(c.strip() for c in cols)
    full_table = f'"{schema}"."{table}"'
    sql = f"SELECT {cols_str} FROM {full_table}"
    if where:
        sql += f" WHERE {where}"
    return pd.read_sql(sql, conn)


def load_all_tables(conn: Any, schema_config: list[dict]) -> dict[str, pd.DataFrame]:
    """Загрузка всех таблиц из конфигурации."""
    tables = {}
    for item in schema_config:
        schema = item["schema_name"]
        table = item["table_name"]
        columns = item["columns"]
        where = item.get("where")
        key = f"{schema}.{table}"
        try:
            tables[key] = fetch_table(conn, schema, table, columns, where)
        except Exception as e:
            print(f"Warning: could not load {key}: {e}")
            tables[key] = pd.DataFrame()
    return tables


def html_header(title: str) -> str:
    """HTML-заголовок с Chart.js."""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: system-ui, sans-serif; margin: 2rem; background: #f5f5f5; }}
        h1 {{ color: #333; }}
        h2 {{ color: #555; margin-top: 2rem; }}
        .chart-container {{ position: relative; height: 300px; max-width: 800px; margin: 1rem 0; }}
        table {{ border-collapse: collapse; width: 100%; background: white; border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #f0f0f0; font-weight: 600; }}
        .kpi {{ font-size: 2rem; font-weight: bold; color: #2e7d32; }}
    </style>
</head>
<body>
"""


def html_footer() -> str:
    return "</body>\n</html>"


def render_chart(chart_id: str, chart_type: str, labels: list, data: list, title: str) -> str:
    """Генерация HTML + JS для Chart.js."""
    return f"""
<div class="chart-container">
    <canvas id="{chart_id}"></canvas>
</div>
<script>
(function() {{
    const ctx = document.getElementById('{chart_id}');
    new Chart(ctx, {{
        type: '{chart_type}',
        data: {{
            labels: {json.dumps(labels)},
            datasets: [{{ label: '{title}', data: {json.dumps(data)}, backgroundColor: 'rgba(54, 162, 235, 0.5)' }}]
        }},
        options: {{ responsive: true, maintainAspectRatio: false }}
    }});
}})();
</script>
"""


def dashboard_clusters_resources(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Кластеры и ресурсы."""
    out = html_header("Кластеры и ресурсы")
    out += "<h1>Кластеры и ресурсы</h1>"

    cc = tables.get("state.cluster_consumption", pd.DataFrame())
    nc = tables.get("state.node_consumption", pd.DataFrame())
    cl = tables.get("conf.cluster", pd.DataFrame())

    if not cc.empty and "k8s_version" in cc.columns:
        v = cc["k8s_version"].value_counts().head(10)
        out += "<h2>Распределение по версии K8s</h2>"
        out += render_chart("chart1", "bar", v.index.tolist(), v.values.tolist(), "Кластеры")

    if not cc.empty:
        cols = ["cluster_type_code", "cpu_total", "ram_total", "nod_total", "cpu_running", "ram_running", "nod_running"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            agg = cc.groupby("cluster_type_code", dropna=False)[avail].sum()
            out += "<h2>Потребление по cluster_type_code</h2>"
            out += agg.to_html(classes="data-table")

    if not nc.empty and "on_dedicated_resources" in nc.columns:
        d = nc["on_dedicated_resources"].value_counts()
        out += "<h2>Dedicated vs Shared</h2>"
        out += render_chart("chart2", "pie", [str(x) for x in d.index], d.values.tolist(), "Узлы")

    if not cc.empty:
        cols = ["short_name", "cpu_total", "ram_total", "nod_total"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            top = cc.nlargest(15, "cpu_total" if "cpu_total" in cc.columns else "nod_total")
            out += "<h2>Топ кластеров по потреблению</h2>"
            out += top[avail].to_html(classes="data-table", index=False)

    if not cc.empty and "environment" in cc.columns:
        e = cc["environment"].value_counts()
        out += "<h2>Потребление по environment</h2>"
        out += render_chart("chart3", "bar", e.index.astype(str).tolist(), e.values.tolist(), "Кластеры")

    out += html_footer()
    return out


def dashboard_operations_slo(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Операции и SLO."""
    out = html_header("Операции и SLO")
    out += "<h1>Операции и SLO</h1>"

    ops = tables.get("operation_v2.operations", pd.DataFrame())
    tasks = tables.get("operation_v2.tasks", pd.DataFrame())

    if not ops.empty and "state" in ops.columns:
        s = ops["state"].value_counts()
        out += "<h2>Распределение operations по state</h2>"
        out += render_chart("chart1", "pie", s.index.astype(str).tolist(), s.values.tolist(), "Операции")

    if not ops.empty and "state_dt" in ops.columns and "create_dt" in ops.columns:
        ops["duration_min"] = (pd.to_datetime(ops["state_dt"]) - pd.to_datetime(ops["create_dt"])).dt.total_seconds() / 60
        by_type = ops.groupby("type", dropna=False)["duration_min"].mean()
        out += "<h2>Среднее время выполнения по type</h2>"
        out += render_chart("chart2", "bar", by_type.index.astype(str).tolist(), by_type.values.tolist(), "Минуты")

    success_states = ["success", "completed", "done"]
    if not ops.empty and "state" in ops.columns:
        total = len(ops)
        success = ops["state"].astype(str).str.lower().isin(success_states).sum()
        pct = round(100 * success / total, 1) if total else 0
        out += f"<h2>Общий % успешных операций</h2><p class='kpi'>{pct}%</p>"

    if not ops.empty and "cluster_id" in ops.columns:
        failed = ops[ops["state"].astype(str).str.lower().str.contains("fail|error", na=False)]
        top_failed = failed.groupby("cluster_id").size().nlargest(10)
        out += "<h2>Топ проблемных кластеров (failed операций)</h2>"
        out += pd.DataFrame({"cluster_id": top_failed.index, "failed_count": top_failed.values}).to_html(index=False)

    out += html_footer()
    return out


def dashboard_errors(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Ошибки."""
    out = html_header("Анализ ошибок")
    out += "<h1>Анализ ошибок</h1>"

    ops = tables.get("operation_v2.operations", pd.DataFrame())
    tasks = tables.get("operation_v2.tasks", pd.DataFrame())
    res = tables.get("state.resource", pd.DataFrame())
    op = tables.get("state.operator", pd.DataFrame())

    error_types = []
    if not ops.empty and "error_type" in ops.columns:
        error_types.extend(ops["error_type"].dropna().astype(str).tolist())
    if not tasks.empty and "error_type" in tasks.columns:
        error_types.extend(tasks["error_type"].dropna().astype(str).tolist())
    if not res.empty and "status" in res.columns:
        error_types.extend(res[res["status"].astype(str).str.contains("error|fail", case=False, na=False)]["status"].tolist())

    if error_types:
        from collections import Counter
        c = Counter(error_types)
        top = c.most_common(15)
        out += "<h2>Топ error_type</h2>"
        out += render_chart("chart1", "bar", [x[0] for x in top], [x[1] for x in top], "Кол-во")

    error_msgs = []
    if not ops.empty and "error_message" in ops.columns:
        error_msgs.extend(ops["error_message"].dropna().astype(str).tolist())
    if not tasks.empty and "error_message" in tasks.columns:
        error_msgs.extend(tasks["error_message"].dropna().astype(str).tolist())
    if error_msgs:
        from collections import Counter
        c = Counter(error_msgs)
        top = c.most_common(20)
        out += "<h2>Топ error_message</h2>"
        df = pd.DataFrame(top, columns=["message", "count"])
        out += df.to_html(index=False)

    if not res.empty and "operator_uuid" in res.columns and "error_count" in res.columns:
        agg = res.groupby("operator_uuid").agg({"status": "count", "error_count": "sum"}).reset_index()
        if not op.empty and "uuid" in op.columns and "name" in op.columns:
            agg = agg.merge(op[["uuid", "name"]], left_on="operator_uuid", right_on="uuid", how="left")
        out += "<h2>Ресурсы в ошибке по operator</h2>"
        out += agg.to_html(index=False)

    out += html_footer()
    return out


def dashboard_config(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Конфигурация."""
    out = html_header("Конфигурация")
    out += "<h1>Конфигурация</h1>"

    cr = tables.get("conf.custom_resource", pd.DataFrame())
    cl = tables.get("conf.cluster", pd.DataFrame())
    op = tables.get("state.operator", pd.DataFrame())
    adm = tables.get("conf.admins", pd.DataFrame())

    if not cr.empty and "cluster_uid" in cr.columns and "resource_type" in cr.columns and "version" in cr.columns:
        cr["combo"] = cr["resource_type"] + "@" + cr["version"].astype(str)
        combos = cr.groupby("cluster_uid")["combo"].apply(lambda x: ", ".join(sorted(set(x)))).reset_index()
        out += "<h2>CR комбинации на кластер</h2>"
        out += combos.to_html(index=False)

    if not cr.empty and "resource_type" in cr.columns and "version" in cr.columns:
        cr["combo"] = cr["resource_type"] + "@" + cr["version"].astype(str)
        top = cr["combo"].value_counts().head(10)
        out += "<h2>Топ комбинаций CR</h2>"
        out += render_chart("chart1", "bar", top.index.tolist(), top.values.tolist(), "Кластеры")

    if not op.empty and not cl.empty and "cluster_uid" in op.columns and "operators_version" in cl.columns:
        merged = op.merge(cl[["uid", "operators_version"]], left_on="cluster_uid", right_on="uid", how="left")
        mismatched = merged[merged["version"].astype(str) != merged["operators_version"].astype(str)]
        cols = [c for c in ["name", "version", "operators_version", "cluster_uid"] if c in mismatched.columns]
        if cols:
            out += "<h2>Несовпадение версий operator vs cluster</h2>"
            out += mismatched[cols].to_html(index=False)

    if not adm.empty:
        out += "<h2>Админы по кластерам</h2>"
        out += adm.to_html(index=False)

    out += html_footer()
    return out


def dashboard_geography(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: География."""
    out = html_header("География")
    out += "<h1>География и зоны</h1>"

    cc = tables.get("state.cluster_consumption", pd.DataFrame())
    nc = tables.get("state.node_consumption", pd.DataFrame())

    if not cc.empty and "region" in cc.columns and "environment" in cc.columns:
        heat = cc.groupby(["region", "environment"]).size().unstack(fill_value=0)
        out += "<h2>Region × Environment (кластеры)</h2>"
        out += heat.to_html()

    if not cc.empty and "geo_zone" in cc.columns:
        g = cc["geo_zone"].value_counts().head(15)
        out += "<h2>Кластеры по geo_zone</h2>"
        out += render_chart("chart1", "bar", g.index.astype(str).tolist(), g.values.tolist(), "Кластеры")

    if not nc.empty and "region" in nc.columns:
        r = nc["region"].value_counts().head(15)
        out += "<h2>Узлы по region</h2>"
        out += render_chart("chart2", "bar", r.index.astype(str).tolist(), r.values.tolist(), "Узлы")

    out += html_footer()
    return out


def dashboard_consumption_trends(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Тренды потребления."""
    out = html_header("Тренды потребления")
    out += "<h1>Тренды потребления</h1>"

    cc = tables.get("state.cluster_consumption", pd.DataFrame())

    if not cc.empty and "update_ts" in cc.columns:
        cc["update_ts"] = pd.to_datetime(cc["update_ts"])
        cc["day"] = cc["update_ts"].dt.date
        cols = ["cpu_total", "ram_total", "nod_total"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            daily = cc.groupby("day")[avail].sum()
            out += "<h2>Потребление по дням</h2>"
            out += daily.to_html()

    if not cc.empty and "short_name" in cc.columns:
        cols = ["cpu_running", "ram_running"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            top5 = cc.nlargest(5, "cpu_running" if "cpu_running" in cc.columns else "nod_total")
            out += "<h2>Топ-5 кластеров по потреблению</h2>"
            out += top5[["short_name"] + avail].to_html(index=False)

    if not cc.empty and "environment" in cc.columns:
        cols = ["cpu_total", "ram_total", "nod_total"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            by_env = cc.groupby("environment")[avail].sum()
            out += "<h2>Потребление по environment</h2>"
            out += by_env.to_html()

    out += html_footer()
    return out


def main():
    parser = argparse.ArgumentParser(description="KaaS DB Analyzer")
    parser.add_argument("--config", default="db_schema.json", help="Path to db_schema.json")
    parser.add_argument("--jdbc-url", default=os.environ.get("DATABASE_JDBC_URL"), help="JDBC URL")
    parser.add_argument("--jdbc-jar", default="jars/postgresql-42.7.3.jar", help="Path to PostgreSQL JDBC driver JAR")
    parser.add_argument("--output", default="reports", help="Output directory for HTML reports")
    parser.add_argument("--dry-run", action="store_true", help="Generate reports from empty data (no DB connection)")
    args = parser.parse_args()

    base = Path(__file__).parent
    config_path = base / args.config if not Path(args.config).is_absolute() else Path(args.config)
    output_dir = base / args.output if not Path(args.output).is_absolute() else Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    schema_config = load_schema(config_path)
    tables: dict[str, pd.DataFrame] = {}

    if args.dry_run:
        print("Dry run: using empty DataFrames")
        for item in schema_config:
            key = f"{item['schema_name']}.{item['table_name']}"
            tables[key] = pd.DataFrame()
    elif args.jdbc_url:
        jdbc_jar = base / args.jdbc_jar if not Path(args.jdbc_jar).is_absolute() else Path(args.jdbc_jar)
        if not jdbc_jar.exists():
            print(f"Error: JDBC driver not found at {jdbc_jar}")
            return 1
        conn = get_jdbc_connection(args.jdbc_url, str(jdbc_jar))
        try:
            tables = load_all_tables(conn, schema_config)
        finally:
            conn.close()
    else:
        print("Error: --jdbc-url or DATABASE_JDBC_URL required (use --dry-run for empty reports)")
        return 1

    dashboards = [
        ("clusters_resources.html", dashboard_clusters_resources),
        ("operations_slo.html", dashboard_operations_slo),
        ("errors.html", dashboard_errors),
        ("config.html", dashboard_config),
        ("geography.html", dashboard_geography),
        ("consumption_trends.html", dashboard_consumption_trends),
    ]

    for name, fn in dashboards:
        out_path = output_dir / name
        html = fn(tables)
        out_path.write_text(html, encoding="utf-8")
        print(f"Written {out_path}")

    return 0


if __name__ == "__main__":
    exit(main())
