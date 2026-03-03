#!/usr/bin/env python3
"""
KaaS DB Analyzer — анализ данных БД и генерация HTML-отчётов.

Подключение: psycopg2 + mTLS + логин/пароль (PostgreSQL).
Единый отчёт: report.html с TOC и SQL под каждым графиком.
"""

import argparse
import json
import os
from pathlib import Path
from typing import Any

import pandas as pd

# SQL-шаблоны для отчёта (period_days подставляется)
def _sql(period_days: int) -> dict:
    pd_str = str(period_days)
    return {
        "cr_usage": f"""-- conf.custom_resource: resource_type + version, deleted=False
SELECT resource_type, version, COUNT(*) AS cluster_count, COUNT(DISTINCT cluster_uid) AS clusters
FROM conf.custom_resource
WHERE (deleted IS NULL OR deleted = false)
  AND modify_ts > now() - interval '{pd_str} days'
GROUP BY resource_type, version
ORDER BY cluster_count DESC;""",
        "clusters_status": f"""SELECT status, COUNT(*) AS cnt FROM state.cluster_consumption
WHERE update_ts > now() - interval '{pd_str} days' GROUP BY status;""",
        "nodes_status": f"""SELECT status, COUNT(*) AS cnt FROM state.node_consumption
WHERE update_ts > now() - interval '{pd_str} days' GROUP BY status;""",
        "k8s_version": f"""SELECT k8s_version, COUNT(*) FROM state.cluster_consumption
WHERE update_ts > now() - interval '{pd_str} days' GROUP BY k8s_version;""",
        "ops_state": f"""SELECT state, COUNT(*) FROM operation_v2.operations
WHERE state_dt > now() - interval '{pd_str} days' GROUP BY state;""",
        "ops_timeline": f"""SELECT DATE(state_dt) AS day,
  SUM(CASE WHEN LOWER(state) IN ('success','completed','done') THEN 1 ELSE 0 END) AS success,
  SUM(CASE WHEN LOWER(state) NOT IN ('success','completed','done') THEN 1 ELSE 0 END) AS failed
FROM operation_v2.operations WHERE state_dt > now() - interval '{pd_str} days'
GROUP BY DATE(state_dt) ORDER BY day;""",
    }


def load_schema(config_path: Path) -> list[dict]:
    """Загрузка конфигурации схемы БД из JSON."""
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


def get_db_engine(
    db_url: str,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
    ssl_rootcert: str | None = None,
) -> Any:
    """SQLAlchemy engine для PostgreSQL: mTLS + логин/пароль из URL."""
    from sqlalchemy import create_engine
    from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

    if db_url.startswith("postgresql://") and not db_url.startswith("postgresql+psycopg2://"):
        db_url = db_url.replace("postgresql://", "postgresql+psycopg2://", 1)

    if ssl_cert or ssl_key or ssl_rootcert:
        parsed = urlparse(db_url)
        query = parse_qs(parsed.query)
        query.setdefault("sslmode", ["verify-full"])
        if ssl_cert:
            query["sslcert"] = [ssl_cert]
        if ssl_key:
            query["sslkey"] = [ssl_key]
        if ssl_rootcert:
            query["sslrootcert"] = [ssl_rootcert]
        new_query = urlencode(query, doseq=True)
        db_url = urlunparse(parsed._replace(query=new_query))

    return create_engine(db_url)


def fetch_table(
    engine: Any,
    schema: str,
    table: str,
    columns: str,
    where: str | None,
    period_days: int = 7,
) -> pd.DataFrame:
    """Чтение таблицы в DataFrame."""
    import re
    cols = columns.split(",")
    cols_str = ", ".join(c.strip() for c in cols)
    full_table = f'"{schema}"."{table}"'
    sql = f"SELECT {cols_str} FROM {full_table}"
    if where:
        where = re.sub(r"interval\s+'\d+\s*hours'", f"interval '{period_days} days'", where, flags=re.I)
        sql += f" WHERE {where}"
    return pd.read_sql(sql, engine)


def load_all_tables(
    engine: Any, schema_config: list[dict], period_days: int = 7
) -> dict[str, pd.DataFrame]:
    """Загрузка всех таблиц из конфигурации."""
    tables = {}
    for item in schema_config:
        schema = item["schema_name"]
        table = item["table_name"]
        columns = item["columns"]
        where = item.get("where")
        key = f"{schema}.{table}"
        try:
            tables[key] = fetch_table(engine, schema, table, columns, where, period_days)
        except Exception as e:
            print(f"Warning: could not load {key}: {e}")
            tables[key] = pd.DataFrame()
    return tables


def html_header(title: str) -> str:
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
        h3 {{ color: #666; margin-top: 1.5rem; }}
        .chart-container {{ position: relative; height: 300px; max-width: 800px; margin: 1rem 0; }}
        table {{ border-collapse: collapse; width: 100%; background: white; border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #f0f0f0; font-weight: 600; }}
        .kpi {{ font-size: 2rem; font-weight: bold; color: #2e7d32; }}
        .no-data {{ color: #888; font-style: italic; padding: 1rem; }}
        .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 1rem 0; }}
        .kpi-card {{ background: white; padding: 1rem; border-radius: 8px; text-align: center; }}
        .kpi-card .value {{ font-size: 1.5rem; font-weight: bold; }}
        .kpi-card .label {{ font-size: 0.85rem; color: #666; }}
        .sql-collapse {{ margin: 0.5rem 0 1.5rem 0; }}
        .sql-collapse summary {{ cursor: pointer; color: #666; font-size: 0.9rem; }}
        .sql-collapse pre {{ background: #f8f8f8; padding: 0.75rem; border-radius: 4px; overflow-x: auto; font-size: 0.8rem; margin: 0.25rem 0 0 0; }}
        .section {{ margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid #ddd; }}
        .toc {{ background: white; padding: 1rem; border-radius: 8px; margin-bottom: 2rem; }}
        .toc a {{ color: #1976d2; text-decoration: none; }}
        .toc a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
"""


def html_footer() -> str:
    return "</body>\n</html>"


PALE_PALETTE = [
    "rgba(179, 229, 252, 0.75)", "rgba(200, 230, 201, 0.75)", "rgba(255, 236, 179, 0.75)",
    "rgba(248, 187, 217, 0.75)", "rgba(225, 190, 231, 0.75)", "rgba(178, 223, 219, 0.75)",
    "rgba(215, 204, 200, 0.75)", "rgba(207, 216, 220, 0.75)",
]


def sql_collapse(sql: str) -> str:
    escaped = sql.replace("<", "&lt;").replace(">", "&gt;")
    return f'<details class="sql-collapse"><summary>Показать SQL</summary><pre>{escaped}</pre></details>'


def render_chart(chart_id: str, chart_type: str, labels: list, data: list, title: str, sql: str | None = None) -> str:
    n = len(data)
    colors = [PALE_PALETTE[i % len(PALE_PALETTE)] for i in range(n)]
    labels_js = json.dumps(labels)
    data_js = json.dumps(data)
    colors_js = json.dumps(colors)
    out = f"""<div class="chart-container"><canvas id="{chart_id}"></canvas></div>
<script>(function(){{
    const ctx = document.getElementById('{chart_id}');
    new Chart(ctx, {{
        type: '{chart_type}',
        data: {{ labels: {labels_js}, datasets: [{{ label: '{title}', data: {data_js}, backgroundColor: {colors_js} }}] }},
        options: {{ responsive: true, maintainAspectRatio: false }}
    }});
}})();</script>"""
    return out + (sql_collapse(sql) if sql else "")


def render_chart_multi(chart_id: str, chart_type: str, labels: list, datasets: list[tuple[str, list]], sql: str | None = None) -> str:
    colors = PALE_PALETTE[: len(datasets)]
    ds_json = [{"label": n, "data": d, "backgroundColor": c} for (n, d), c in zip(datasets, colors)]
    labels_js = json.dumps(labels)
    ds_js = json.dumps(ds_json)
    out = f"""<div class="chart-container"><canvas id="{chart_id}"></canvas></div>
<script>(function(){{
    const ctx = document.getElementById('{chart_id}');
    new Chart(ctx, {{
        type: '{chart_type}',
        data: {{ labels: {labels_js}, datasets: {ds_js} }},
        options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ stacked: true }}, y: {{ stacked: true }} }} }}
    }});
}})();</script>"""
    return out + (sql_collapse(sql) if sql else "")


def _table_with_sql(html: str, sql: str | None = None) -> str:
    return html + (sql_collapse(sql) if sql else "")


def _kpi_card(label: str, value: int | str) -> str:
    return f"<div class='kpi-card'><div class='value'>{value}</div><div class='label'>{label}</div></div>"


def _no_data(msg: str) -> str:
    return f"<p class='no-data'>{msg}</p>"


def build_unified_report(tables: dict[str, pd.DataFrame], period_days: int) -> str:
    """Единый HTML-отчёт со всеми разделами, TOC и SQL под каждым графиком."""
    sql = _sql(period_days)
    out = html_header("KaaS — Аналитический отчёт")
    out += "<h1>KaaS — Аналитический отчёт</h1>"
    out += """<div class="toc"><h3>Содержание</h3>
<a href="#cr_usage">1. Custom Resource (resource_type+version, deleted=False)</a><br>
<a href="#clusters">2. Кластеры и ресурсы</a><br>
<a href="#operations">3. Операции и SLO</a><br>
<a href="#timeline">4. Операции на временной шкале</a><br>
<a href="#errors">5. Ошибки</a><br>
<a href="#config">6. Конфигурация</a><br>
<a href="#cr_clusters">7. CR по кластерам</a><br>
<a href="#geography">8. География</a><br>
<a href="#trends">9. Тренды потребления</a>
</div>"""

    # 1. Custom Resource: resource_type + version, deleted=False
    out += '<div class="section" id="cr_usage"><h2>1. Custom Resource — использование (resource_type + version, deleted=False)</h2>'
    cr = tables.get("conf.custom_resource", pd.DataFrame())
    if not cr.empty and "resource_type" in cr.columns and "version" in cr.columns:
        cr = cr.copy()
        cr = cr[~cr["deleted"].astype(str).str.lower().isin(["true", "1", "yes"])] if "deleted" in cr.columns else cr
        agg = cr.groupby(["resource_type", "version"]).agg(
            cluster_count=("cluster_uid", "nunique"),
            total=("cluster_uid", "count"),
        ).reset_index()
        out += agg.to_html(index=False)
        if sql.get("cr_usage"):
            out += sql_collapse(sql["cr_usage"])
    else:
        out += _no_data("Нет данных custom_resource.")
    out += "</div>"

    # 2. Кластеры и ресурсы
    out += '<div class="section" id="clusters"><h2>2. Кластеры и ресурсы</h2>'
    cc = tables.get("state.cluster_consumption", pd.DataFrame())
    nc = tables.get("state.node_consumption", pd.DataFrame())
    nd = tables.get("state.node", pd.DataFrame())
    STATUS_ACTIVE = {"updating", "running", "pending"}
    STATUS_DEAD = {"error", "deleting"}

    if not cc.empty and "status" in cc.columns:
        status_lower = cc["status"].astype(str).str.lower().str.strip()
        cc_active = int(status_lower.isin(STATUS_ACTIVE).sum())
        cc_dead = int(status_lower.isin(STATUS_DEAD).sum())
        out += "<h3>Кластеры</h3><div class='kpi-grid'>"
        out += _kpi_card("Всего", len(cc)) + _kpi_card("Активных", cc_active) + _kpi_card("Мёртвых", cc_dead) + "</div>"
        if cc_active + cc_dead > 0:
            out += render_chart("c_pie", "pie", ["Активные", "Мёртвые"], [cc_active, cc_dead], "Кластеры")
        if "status" in cc.columns:
            by_s = cc["status"].astype(str).str.strip().value_counts()
            out += "<h3>Кластеры по статусу</h3>"
            out += render_chart("c_status", "bar", by_s.index.tolist(), by_s.values.tolist(), "Кол-во", sql.get("clusters_status"))

    if not nc.empty or not nd.empty:
        nd_total = len(nc) if not nc.empty else len(nd)
        nd_active, nd_dead = nd_total, 0  # значения по умолчанию
        if not nd.empty and "deleted" in nd.columns:
            nd_dead = int(nd["deleted"].astype(str).str.lower().isin(["true", "1", "yes"]).sum())
            nd_active = len(nd) - nd_dead
        elif not nc.empty and "status" in nc.columns:
            sl = nc["status"].astype(str).str.lower().str.strip()
            nd_active = int(sl.isin(STATUS_ACTIVE).sum())
            nd_dead = int(sl.isin(STATUS_DEAD).sum())
        out += "<h3>Ноды</h3><div class='kpi-grid'>"
        out += _kpi_card("Всего", nd_total) + _kpi_card("Активных", nd_active) + _kpi_card("Мёртвых", nd_dead) + "</div>"
        if nd_total > 0:
            out += render_chart("n_pie", "pie", ["Активные", "Мёртвые"], [nd_active, nd_dead], "Ноды")
        if not nc.empty and "status" in nc.columns:
            by_s = nc["status"].astype(str).str.strip().value_counts()
            out += "<h3>Ноды по статусу</h3>"
            out += render_chart("n_status", "bar", by_s.index.tolist(), by_s.values.tolist(), "Кол-во", sql.get("nodes_status"))

    if not cc.empty and "k8s_version" in cc.columns:
        v = cc["k8s_version"].value_counts().head(10)
        out += "<h3>Версии K8s</h3>" + render_chart("c_k8s", "bar", v.index.tolist(), v.values.tolist(), "Кластеры", sql.get("k8s_version"))
    if not cc.empty:
        cols = [c for c in ["cluster_type_code", "cpu_total", "ram_total", "nod_total"] if c in cc.columns]
        if cols:
            out += "<h3>Потребление по cluster_type_code</h3>" + cc.groupby("cluster_type_code", dropna=False)[cols].sum().to_html()
    if not nc.empty and "on_dedicated_resources" in nc.columns:
        d = nc["on_dedicated_resources"].value_counts()
        out += "<h3>Dedicated vs Shared</h3>" + render_chart("c_ded", "pie", [str(x) for x in d.index], d.values.tolist(), "Узлы")
    if not cc.empty and "environment" in cc.columns:
        e = cc["environment"].value_counts()
        out += "<h3>По environment</h3>" + render_chart("c_env", "bar", e.index.astype(str).tolist(), e.values.tolist(), "Кластеры")
    out += "</div>"

    # 3. Операции и SLO
    out += '<div class="section" id="operations"><h2>3. Операции и SLO</h2>'
    ops = tables.get("operation_v2.operations", pd.DataFrame())
    if not ops.empty and "state" in ops.columns:
        s = ops["state"].value_counts()
        out += render_chart("o_state", "pie", s.index.astype(str).tolist(), s.values.tolist(), "Операции", sql.get("ops_state"))
        success = ops["state"].astype(str).str.lower().isin(["success", "completed", "done"]).sum()
        out += f"<h3>% успешных</h3><p class='kpi'>{round(100*success/len(ops),1)}%</p>"
    else:
        out += _no_data("Нет данных operations.")
    out += "</div>"

    # 4. Операции на временной шкале
    out += '<div class="section" id="timeline"><h2>4. Операции на временной шкале</h2>'
    if not ops.empty and "state_dt" in ops.columns and "state" in ops.columns:
        ops = ops.copy()
        ops["day"] = pd.to_datetime(ops["state_dt"]).dt.date
        ops["ok"] = ops["state"].astype(str).str.lower().isin(["success", "completed", "done"])
        daily = ops.groupby("day").agg(success=("ok", "sum"), failed=("ok", lambda x: (~x).sum())).reset_index()
        if not daily.empty:
            out += render_chart_multi("o_tl", "bar", [str(d) for d in daily["day"]],
                [("Успешные", daily["success"].astype(int).tolist()), ("Неуспешные", daily["failed"].astype(int).tolist())],
                sql.get("ops_timeline"))
    out += "</div>"

    # 5. Ошибки
    out += '<div class="section" id="errors"><h2>5. Ошибки</h2>'
    tasks = tables.get("operation_v2.tasks", pd.DataFrame())
    res = tables.get("state.resource", pd.DataFrame())
    op = tables.get("state.operator", pd.DataFrame())
    err_types = []
    if not ops.empty and "error_type" in ops.columns:
        err_types.extend(ops["error_type"].dropna().astype(str).tolist())
    if not tasks.empty and "error_type" in tasks.columns:
        err_types.extend(tasks["error_type"].dropna().astype(str).tolist())
    if err_types:
        from collections import Counter
        top = Counter(err_types).most_common(15)
        out += "<h3>Топ error_type</h3>" + render_chart("e_type", "bar", [x[0] for x in top], [x[1] for x in top], "Кол-во")
    if not res.empty and "operator_uuid" in res.columns:
        agg = res.groupby("operator_uuid").agg({"status": "count", "error_count": "sum"}).reset_index()
        if not op.empty:
            agg = agg.merge(op[["uuid", "name"]], left_on="operator_uuid", right_on="uuid", how="left")
        out += "<h3>Ресурсы в ошибке по operator</h3>" + agg.to_html(index=False)
    out += "</div>"

    # 6. Конфигурация
    out += '<div class="section" id="config"><h2>6. Конфигурация</h2>'
    cr = tables.get("conf.custom_resource", pd.DataFrame())
    cl = tables.get("conf.cluster", pd.DataFrame())
    adm = tables.get("conf.admins", pd.DataFrame())
    if not cr.empty and "cluster_uid" in cr.columns:
        cr = cr[~cr["deleted"].astype(str).str.lower().isin(["true", "1", "yes"])] if "deleted" in cr.columns else cr
        combos = cr.groupby("cluster_uid").apply(lambda x: ", ".join(sorted(set(x["resource_type"] + "@" + x["version"].astype(str))))).reset_index()
        out += "<h3>CR комбинации на кластер</h3>" + combos.to_html(index=False)
    if not adm.empty:
        out += "<h3>Админы</h3>" + adm.to_html(index=False)
    out += "</div>"

    # 7. CR по кластерам
    out += '<div class="section" id="cr_clusters"><h2>7. CR по кластерам</h2>'
    if not cr.empty and "cluster_uid" in cr.columns:
        cr = cr.copy()
        cr["cr_v"] = cr["resource_type"] + " @ " + cr["version"].astype(str)
        by_cl = cr.groupby("cluster_uid").agg(cr_list=("cr_v", lambda x: ", ".join(sorted(set(x)))), cr_count=("resource_type", "nunique")).reset_index()
        if not cl.empty:
            by_cl = by_cl.merge(cl[["uid", "short_name"]], left_on="cluster_uid", right_on="uid", how="left")
        out += by_cl.to_html(index=False)
        by_type = cr.groupby(["resource_type", "version"]).agg(cluster_count=("cluster_uid", "nunique")).reset_index()
        out += "<h3>Тип+версия → кластеры</h3>" + by_type.to_html(index=False)
        if sql.get("cr_usage"):
            out += sql_collapse(sql["cr_usage"])
    out += "</div>"

    # 8. География
    out += '<div class="section" id="geography"><h2>8. География</h2>'
    if not cc.empty and "region" in cc.columns and "environment" in cc.columns:
        heat = cc.groupby(["region", "environment"]).size().unstack(fill_value=0)
        out += heat.to_html()
    if not nc.empty and "region" in nc.columns:
        r = nc["region"].value_counts().head(15)
        out += "<h3>Узлы по region</h3>" + render_chart("g_reg", "bar", r.index.astype(str).tolist(), r.values.tolist(), "Узлы")
    out += "</div>"

    # 9. Тренды потребления
    out += '<div class="section" id="trends"><h2>9. Тренды потребления</h2>'
    if not cc.empty and "update_ts" in cc.columns:
        cc = cc.copy()
        cc["day"] = pd.to_datetime(cc["update_ts"]).dt.date
        cols = [c for c in ["cpu_total", "ram_total", "nod_total"] if c in cc.columns]
        if cols:
            out += cc.groupby("day")[cols].sum().to_html()
    out += "</div>"

    out += html_footer()
    return out


def main():
    parser = argparse.ArgumentParser(description="KaaS DB Analyzer")
    parser.add_argument("--config", default="db_schema.json", help="Path to db_schema.json")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"), help="PostgreSQL connection URL")
    parser.add_argument("--db-user", default=os.environ.get("DB_USER"), help="DB user")
    parser.add_argument("--db-password", default=os.environ.get("DB_PASSWORD"), help="DB password")
    parser.add_argument("--ssl-cert", default=os.environ.get("DB_SSL_CERT"), help="Path to client cert (mTLS)")
    parser.add_argument("--ssl-key", default=os.environ.get("DB_SSL_KEY"), help="Path to client key (mTLS)")
    parser.add_argument("--ssl-rootcert", default=os.environ.get("DB_SSL_ROOTCERT"), help="Path to CA cert (mTLS)")
    parser.add_argument("--output", default="reports", help="Output directory")
    parser.add_argument("--period-days", type=int, default=7, help="Период загрузки в днях")
    parser.add_argument("--dry-run", action="store_true", help="Empty data, no DB")
    args = parser.parse_args()

    base = Path(__file__).parent
    config_path = base / args.config if not Path(args.config).is_absolute() else Path(args.config)
    output_dir = base / args.output if not Path(args.output).is_absolute() else Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    schema_config = load_schema(config_path)
    tables: dict[str, pd.DataFrame] = {}

    if args.dry_run:
        for item in schema_config:
            tables[f"{item['schema_name']}.{item['table_name']}"] = pd.DataFrame()
    elif args.db_url:
        def _resolve(p, d):
            return str(base / p) if p and not Path(p).is_absolute() else (str(d) if d.exists() else None)
        ssl_cert = _resolve(args.ssl_cert, base / "certs" / "client.pem")
        ssl_key = _resolve(args.ssl_key, base / "certs" / "client-key.pem")
        ssl_rootcert = _resolve(args.ssl_rootcert, base / "certs" / "ca.pem")
        if args.db_user or args.db_password:
            from urllib.parse import urlparse, urlunparse
            p = urlparse(args.db_url)
            u = args.db_user or p.username or ""
            pw = args.db_password or p.password or ""
            np = f"{u}:{pw}@{p.hostname}" + (f":{p.port}" if p.port else "")
            args.db_url = urlunparse(p._replace(netloc=np))
        engine = get_db_engine(args.db_url, ssl_cert, ssl_key, ssl_rootcert)
        try:
            tables = load_all_tables(engine, schema_config, args.period_days)
        finally:
            engine.dispose()
    else:
        print("Error: --db-url or DATABASE_URL required (use --dry-run)")
        return 1

    html = build_unified_report(tables, args.period_days)
    out_path = output_dir / "report.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Written {out_path}")

    return 0


if __name__ == "__main__":
    exit(main())
