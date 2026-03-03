#!/usr/bin/env python3
"""
KaaS DB Analyzer — анализ данных БД и генерация HTML-отчётов.

Подключение: psycopg2 + mTLS + логин/пароль (PostgreSQL).
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
        .no-data {{ color: #888; font-style: italic; padding: 1rem; }}
        .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 1rem 0; }}
        .kpi-card {{ background: white; padding: 1rem; border-radius: 8px; text-align: center; }}
        .kpi-card .value {{ font-size: 1.5rem; font-weight: bold; }}
        .kpi-card .label {{ font-size: 0.85rem; color: #666; }}
    </style>
</head>
<body>
"""


def html_footer() -> str:
    return "</body>\n</html>"


PALE_PALETTE = [
    "rgba(179, 229, 252, 0.75)",  # light blue
    "rgba(200, 230, 201, 0.75)",  # light green
    "rgba(255, 236, 179, 0.75)",  # light amber
    "rgba(248, 187, 217, 0.75)",  # light pink
    "rgba(225, 190, 231, 0.75)",  # light purple
    "rgba(178, 223, 219, 0.75)",  # teal
    "rgba(215, 204, 200, 0.75)",  # warm grey
    "rgba(207, 216, 220, 0.75)",  # blue grey
]


def render_chart(chart_id: str, chart_type: str, labels: list, data: list, title: str) -> str:
    """Генерация HTML + JS для Chart.js с бледной палитрой."""
    n = len(data)
    colors = [PALE_PALETTE[i % len(PALE_PALETTE)] for i in range(n)]
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
            datasets: [{{ label: '{title}', data: {json.dumps(data)}, backgroundColor: {json.dumps(colors)} }}]
        }},
        options: {{ responsive: true, maintainAspectRatio: false }}
    }});
}})();
</script>
"""


def render_chart_multi(
    chart_id: str,
    chart_type: str,
    labels: list,
    datasets: list[tuple[str, list]],
) -> str:
    """Генерация Chart.js с несколькими наборами данных (stacked bar/line)."""
    colors = PALE_PALETTE[: len(datasets)]
    ds_json = [
        {"label": name, "data": data, "backgroundColor": color}
        for (name, data), color in zip(datasets, colors)
    ]
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
            datasets: {json.dumps(ds_json)}
        }},
        options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ stacked: true }}, y: {{ stacked: true }} }} }}
    }});
}})();
</script>
"""


def _no_data(msg: str = "Нет данных за период.") -> str:
    return f"<p class='no-data'>{msg}</p>"


def _kpi_card(label: str, value: int | str) -> str:
    """KPI-карточка для агрегатов."""
    return f"<div class='kpi-card'><div class='value'>{value}</div><div class='label'>{label}</div></div>"


def dashboard_clusters_resources(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Кластеры и ресурсы."""
    out = html_header("Кластеры и ресурсы")
    out += "<h1>Кластеры и ресурсы</h1>"

    cc = tables.get("state.cluster_consumption", pd.DataFrame())
    nc = tables.get("state.node_consumption", pd.DataFrame())
    cl = tables.get("conf.cluster", pd.DataFrame())
    nd = tables.get("state.node", pd.DataFrame())
    has_content = False

    # Статусы: Updating, Running, Error, Pending, Deleting
    STATUS_ACTIVE = {"updating", "running", "pending"}
    STATUS_DEAD = {"error", "deleting"}

    # Агрегаты: кластеры и ноды, активные/мёртвые
    if not cc.empty or not cl.empty:
        if not cc.empty and "status" in cc.columns:
            status_lower = cc["status"].astype(str).str.lower().str.strip()
            cc_active = int(status_lower.isin(STATUS_ACTIVE).sum())
            cc_dead = int(status_lower.isin(STATUS_DEAD).sum())
            cc_total = len(cc)
        elif not cl.empty and "delete_ts" in cl.columns:
            cc_active = int(cl["delete_ts"].isna().sum())
            cc_dead = int(cl["delete_ts"].notna().sum())
            cc_total = len(cl)
        else:
            cc_total = len(cc) if not cc.empty else len(cl)
            cc_active = cc_total
            cc_dead = 0
        out += "<h2>Кластеры</h2>"
        out += "<div class='kpi-grid'>"
        out += _kpi_card("Всего", cc_total)
        out += _kpi_card("Активных", cc_active)
        out += _kpi_card("Мёртвых", cc_dead)
        out += "</div>"
        if cc_total > 0:
            out += render_chart("chart_clusters", "pie", ["Активные", "Мёртвые"], [cc_active, cc_dead], "Кластеры")
        if not cc.empty and "status" in cc.columns:
            by_status = cc["status"].astype(str).str.strip().value_counts()
            out += "<h2>Кластеры по статусу</h2>"
            out += render_chart("chart_clusters_status", "bar", by_status.index.tolist(), by_status.values.tolist(), "Кол-во")
        has_content = True

    if not nc.empty or not nd.empty:
        if not nd.empty and "deleted" in nd.columns:
            nd_deleted = int(nd["deleted"].astype(str).str.lower().isin(["true", "1", "yes"]).sum())
            nd_active = len(nd) - nd_deleted
            nd_total = len(nd)
        elif not nc.empty and "status" in nc.columns:
            status_lower = nc["status"].astype(str).str.lower().str.strip()
            nd_active = int(status_lower.isin(STATUS_ACTIVE).sum())
            nd_dead = int(status_lower.isin(STATUS_DEAD).sum())
            nd_total = len(nc)
        else:
            nd_total = len(nc) if not nc.empty else len(nd)
            nd_active = nd_total
            nd_dead = 0
        out += "<h2>Ноды</h2>"
        out += "<div class='kpi-grid'>"
        out += _kpi_card("Всего", nd_total)
        out += _kpi_card("Активных", nd_active)
        out += _kpi_card("Мёртвых", nd_dead)
        out += "</div>"
        if nd_total > 0:
            out += render_chart("chart_nodes", "pie", ["Активные", "Мёртвые"], [nd_active, nd_dead], "Ноды")
        if not nc.empty and "status" in nc.columns:
            by_status = nc["status"].astype(str).str.strip().value_counts()
            out += "<h2>Ноды по статусу</h2>"
            out += render_chart("chart_nodes_status", "bar", by_status.index.tolist(), by_status.values.tolist(), "Кол-во")
        has_content = True

    if not cc.empty and "k8s_version" in cc.columns:
        v = cc["k8s_version"].value_counts().head(10)
        out += "<h2>Распределение по версии K8s</h2>"
        out += render_chart("chart1", "bar", v.index.tolist(), v.values.tolist(), "Кластеры")
        has_content = True


    if not cc.empty:
        cols = ["cluster_type_code", "cpu_total", "ram_total", "nod_total", "cpu_running", "ram_running", "nod_running"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            agg = cc.groupby("cluster_type_code", dropna=False)[avail].sum()
            out += "<h2>Потребление по cluster_type_code</h2>"
            out += agg.to_html(classes="data-table")
            has_content = True

    if not nc.empty and "on_dedicated_resources" in nc.columns:
        d = nc["on_dedicated_resources"].value_counts()
        out += "<h2>Dedicated vs Shared</h2>"
        out += render_chart("chart2", "pie", [str(x) for x in d.index], d.values.tolist(), "Узлы")
        has_content = True

    if not cc.empty:
        cols = ["short_name", "cpu_total", "ram_total", "nod_total"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            top = cc.nlargest(15, "cpu_total" if "cpu_total" in cc.columns else "nod_total")
            out += "<h2>Топ кластеров по потреблению</h2>"
            out += top[avail].to_html(classes="data-table", index=False)
            has_content = True

    if not cc.empty and "environment" in cc.columns:
        e = cc["environment"].value_counts()
        out += "<h2>Потребление по environment</h2>"
        out += render_chart("chart3", "bar", e.index.astype(str).tolist(), e.values.tolist(), "Кластеры")
        has_content = True

    if not has_content:
        out += _no_data("Нет данных cluster_consumption/node_consumption. Увеличьте --period-days.")

    out += html_footer()
    return out


def dashboard_operations_slo(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Операции и SLO."""
    out = html_header("Операции и SLO")
    out += "<h1>Операции и SLO</h1>"

    ops = tables.get("operation_v2.operations", pd.DataFrame())
    tasks = tables.get("operation_v2.tasks", pd.DataFrame())
    has_content = False

    if not ops.empty and "state" in ops.columns:
        s = ops["state"].value_counts()
        out += "<h2>Распределение operations по state</h2>"
        out += render_chart("chart1", "pie", s.index.astype(str).tolist(), s.values.tolist(), "Операции")
        has_content = True

    if not ops.empty and "state_dt" in ops.columns and "create_dt" in ops.columns:
        ops = ops.copy()
        ops["duration_min"] = (pd.to_datetime(ops["state_dt"]) - pd.to_datetime(ops["create_dt"])).dt.total_seconds() / 60
        by_type = ops.groupby("type", dropna=False)["duration_min"].mean()
        out += "<h2>Среднее время выполнения по type</h2>"
        out += render_chart("chart2", "bar", by_type.index.astype(str).tolist(), by_type.values.tolist(), "Минуты")
        has_content = True

    success_states = ["success", "completed", "done"]
    if not ops.empty and "state" in ops.columns:
        total = len(ops)
        success = ops["state"].astype(str).str.lower().isin(success_states).sum()
        pct = round(100 * success / total, 1) if total else 0
        out += f"<h2>Общий % успешных операций</h2><p class='kpi'>{pct}%</p>"
        has_content = True

    if not ops.empty and "cluster_id" in ops.columns:
        failed = ops[ops["state"].astype(str).str.lower().str.contains("fail|error", na=False)]
        if not failed.empty:
            top_failed = failed.groupby("cluster_id").size().nlargest(10)
            out += "<h2>Топ проблемных кластеров (failed операций)</h2>"
            out += pd.DataFrame({"cluster_id": top_failed.index, "failed_count": top_failed.values}).to_html(index=False)
            has_content = True

    if not has_content:
        out += _no_data("Нет данных operations/tasks. Увеличьте --period-days.")

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
    has_content = False

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
        has_content = True

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
        has_content = True

    if not res.empty and "operator_uuid" in res.columns and "error_count" in res.columns:
        agg = res.groupby("operator_uuid").agg({"status": "count", "error_count": "sum"}).reset_index()
        if not op.empty and "uuid" in op.columns and "name" in op.columns:
            agg = agg.merge(op[["uuid", "name"]], left_on="operator_uuid", right_on="uuid", how="left")
        out += "<h2>Ресурсы в ошибке по operator</h2>"
        out += agg.to_html(index=False)
        has_content = True

    if not has_content:
        out += _no_data("Нет данных об ошибках (operations/tasks/resource). Увеличьте --period-days.")

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
    has_content = False

    if not cr.empty and "cluster_uid" in cr.columns and "resource_type" in cr.columns and "version" in cr.columns:
        cr = cr.copy()
        cr["combo"] = cr["resource_type"] + "@" + cr["version"].astype(str)
        combos = cr.groupby("cluster_uid")["combo"].apply(lambda x: ", ".join(sorted(set(x)))).reset_index()
        out += "<h2>CR комбинации на кластер</h2>"
        out += combos.to_html(index=False)
        has_content = True

    if not cr.empty and "resource_type" in cr.columns and "version" in cr.columns:
        cr = cr.copy()
        cr["combo"] = cr["resource_type"] + "@" + cr["version"].astype(str)
        top = cr["combo"].value_counts().head(10)
        if not top.empty:
            out += "<h2>Топ комбинаций CR</h2>"
            out += render_chart("chart1", "bar", top.index.tolist(), top.values.tolist(), "Кластеры")
            has_content = True

    if not op.empty and not cl.empty and "cluster_uid" in op.columns and "operators_version" in cl.columns:
        merged = op.merge(cl[["uid", "operators_version"]], left_on="cluster_uid", right_on="uid", how="left")
        mismatched = merged[merged["version"].astype(str) != merged["operators_version"].astype(str)]
        cols = [c for c in ["name", "version", "operators_version", "cluster_uid"] if c in mismatched.columns]
        if cols and not mismatched.empty:
            out += "<h2>Несовпадение версий operator vs cluster</h2>"
            out += mismatched[cols].to_html(index=False)
            has_content = True

    if not adm.empty:
        out += "<h2>Админы по кластерам</h2>"
        out += adm.to_html(index=False)
        has_content = True

    if not has_content:
        out += _no_data("Нет данных custom_resource/operator/admins.")

    out += html_footer()
    return out


def dashboard_geography(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: География."""
    out = html_header("География")
    out += "<h1>География и зоны</h1>"

    cc = tables.get("state.cluster_consumption", pd.DataFrame())
    nc = tables.get("state.node_consumption", pd.DataFrame())
    has_content = False

    if not cc.empty and "region" in cc.columns and "environment" in cc.columns:
        heat = cc.groupby(["region", "environment"]).size().unstack(fill_value=0)
        out += "<h2>Region × Environment (кластеры)</h2>"
        out += heat.to_html()
        has_content = True

    if not cc.empty and "geo_zone" in cc.columns:
        g = cc["geo_zone"].value_counts().head(15)
        out += "<h2>Кластеры по geo_zone</h2>"
        out += render_chart("chart1", "bar", g.index.astype(str).tolist(), g.values.tolist(), "Кластеры")
        has_content = True

    if not nc.empty and "region" in nc.columns:
        r = nc["region"].value_counts().head(15)
        out += "<h2>Узлы по region</h2>"
        out += render_chart("chart2", "bar", r.index.astype(str).tolist(), r.values.tolist(), "Узлы")
        has_content = True

    if not has_content:
        out += _no_data("Нет данных cluster_consumption/node_consumption. Увеличьте --period-days.")

    out += html_footer()
    return out


def dashboard_consumption_trends(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Тренды потребления."""
    out = html_header("Тренды потребления")
    out += "<h1>Тренды потребления</h1>"

    cc = tables.get("state.cluster_consumption", pd.DataFrame())
    has_content = False

    if not cc.empty and "update_ts" in cc.columns:
        cc = cc.copy()
        cc["update_ts"] = pd.to_datetime(cc["update_ts"])
        cc["day"] = cc["update_ts"].dt.date
        cols = ["cpu_total", "ram_total", "nod_total"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            daily = cc.groupby("day")[avail].sum()
            out += "<h2>Потребление по дням</h2>"
            out += daily.to_html()
            has_content = True

    if not cc.empty and "short_name" in cc.columns:
        cols = ["cpu_running", "ram_running"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            top5 = cc.nlargest(5, "cpu_running" if "cpu_running" in cc.columns else "nod_total")
            out += "<h2>Топ-5 кластеров по потреблению</h2>"
            out += top5[["short_name"] + avail].to_html(index=False)
            has_content = True

    if not cc.empty and "environment" in cc.columns:
        cols = ["cpu_total", "ram_total", "nod_total"]
        avail = [c for c in cols if c in cc.columns]
        if avail:
            by_env = cc.groupby("environment")[avail].sum()
            out += "<h2>Потребление по environment</h2>"
            out += by_env.to_html()
            has_content = True

    if not has_content:
        out += _no_data("Нет данных cluster_consumption. Увеличьте --period-days.")

    out += html_footer()
    return out


def dashboard_operations_timeline(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: Успешные / неуспешные операции на временной шкале."""
    out = html_header("Операции: успешные / неуспешные по дням")
    out += "<h1>Операции на временной шкале</h1>"

    ops = tables.get("operation_v2.operations", pd.DataFrame())
    has_content = False

    if not ops.empty and "state_dt" in ops.columns and "state" in ops.columns:
        ops = ops.copy()
        ops["day"] = pd.to_datetime(ops["state_dt"]).dt.date
        success_states = ["success", "completed", "done"]
        ops["is_success"] = ops["state"].astype(str).str.lower().isin(success_states)

        daily = ops.groupby("day").agg(
            success=("is_success", "sum"),
            failed=("is_success", lambda x: (~x).sum()),
        ).reset_index()

        if not daily.empty:
            labels = [str(d) for d in daily["day"]]
            datasets = [
                ("Успешные", daily["success"].astype(int).tolist()),
                ("Неуспешные", daily["failed"].astype(int).tolist()),
            ]
            out += "<h2>Успешные / неуспешные операции по дням</h2>"
            out += render_chart_multi("chart_timeline", "bar", labels, datasets)
            out += "<h2>Данные по дням</h2>"
            out += daily.to_html(index=False)
            has_content = True

    if not has_content:
        out += _no_data("Нет данных operations. Увеличьте --period-days.")

    out += html_footer()
    return out


def dashboard_cr_per_cluster(tables: dict[str, pd.DataFrame]) -> str:
    """Дашборд: CR установленные на каждый кластер."""
    out = html_header("Custom Resources по кластерам")
    out += "<h1>CR установленные на кластеры</h1>"

    cr = tables.get("conf.custom_resource", pd.DataFrame())
    cl = tables.get("conf.cluster", pd.DataFrame())
    has_content = False

    if not cr.empty and "cluster_uid" in cr.columns and "resource_type" in cr.columns and "version" in cr.columns:
        cr = cr.copy()
        cr["cr_version"] = cr["resource_type"] + " @ " + cr["version"].astype(str)
        if "deleted" in cr.columns:
            cr = cr[~cr["deleted"].astype(str).str.lower().isin(["true", "1", "yes"])]

        cluster_crs = cr.groupby("cluster_uid").agg(
            cr_list=("cr_version", lambda x: ", ".join(sorted(set(x)))),
            cr_count=("resource_type", "nunique"),
        ).reset_index()

        if not cl.empty and "uid" in cl.columns and "short_name" in cl.columns:
            cluster_crs = cluster_crs.merge(
                cl[["uid", "short_name", "name"]],
                left_on="cluster_uid",
                right_on="uid",
                how="left",
            )
            cols = ["short_name", "name", "cr_count", "cr_list"]
            cols = [c for c in cols if c in cluster_crs.columns]
            out += "<h2>CR по кластерам</h2>"
            out += cluster_crs[cols].to_html(index=False)
            has_content = True
        else:
            out += "<h2>CR по кластерам</h2>"
            out += cluster_crs.to_html(index=False)
            has_content = True

        cr_by_type = cr.groupby(["resource_type", "version"]).agg(
            cluster_count=("cluster_uid", "nunique"),
            clusters=("cluster_uid", lambda x: ", ".join(sorted(set(str(u) for u in x)))),
        ).reset_index()
        out += "<h2>Установки CR: тип и версия → кластеры</h2>"
        out += cr_by_type.to_html(index=False)
        has_content = True

    if not has_content:
        out += _no_data("Нет данных custom_resource. Увеличьте --period-days.")

    out += html_footer()
    return out


def main():
    parser = argparse.ArgumentParser(description="KaaS DB Analyzer")
    parser.add_argument("--config", default="db_schema.json", help="Path to db_schema.json")
    parser.add_argument("--db-url", default=os.environ.get("DATABASE_URL"), help="PostgreSQL connection URL")
    parser.add_argument("--db-user", default=os.environ.get("DB_USER"), help="DB user (если не в URL)")
    parser.add_argument("--db-password", default=os.environ.get("DB_PASSWORD"), help="DB password (если не в URL)")
    parser.add_argument("--ssl-cert", default=os.environ.get("DB_SSL_CERT"), help="Path to client cert (mTLS)")
    parser.add_argument("--ssl-key", default=os.environ.get("DB_SSL_KEY"), help="Path to client key (mTLS)")
    parser.add_argument("--ssl-rootcert", default=os.environ.get("DB_SSL_ROOTCERT"), help="Path to CA cert (mTLS)")
    parser.add_argument("--output", default="reports", help="Output directory for HTML reports")
    parser.add_argument("--period-days", type=int, default=7, help="Период загрузки в днях (по умолчанию 7)")
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
    elif args.db_url:
        def _resolve_cert(path: str | None, default: Path) -> str | None:
            if path:
                p = Path(path)
                return str(base / p) if not p.is_absolute() else path
            return str(default) if default.exists() else None

        db_url = args.db_url
        if args.db_user is not None or args.db_password is not None:
            from urllib.parse import urlparse, urlunparse
            parsed = urlparse(db_url)
            user = args.db_user if args.db_user is not None else (parsed.username or "")
            password = args.db_password if args.db_password is not None else (parsed.password or "")
            host_part = f"{parsed.hostname}:{parsed.port}" if parsed.port else (parsed.hostname or "")
            netloc = f"{user}:{password}@{host_part}" if (user or password) else host_part
            db_url = urlunparse(parsed._replace(netloc=netloc))

        ssl_cert = _resolve_cert(args.ssl_cert, base / "certs" / "client.pem")
        ssl_key = _resolve_cert(args.ssl_key, base / "certs" / "client-key.pem")
        ssl_rootcert = _resolve_cert(args.ssl_rootcert, base / "certs" / "ca.pem")
        engine = get_db_engine(db_url, ssl_cert, ssl_key, ssl_rootcert)
        try:
            tables = load_all_tables(engine, schema_config, args.period_days)
        finally:
            engine.dispose()
    else:
        print("Error: --db-url or DATABASE_URL required (use --dry-run for empty reports)")
        return 1

    dashboards = [
        ("clusters_resources.html", dashboard_clusters_resources),
        ("operations_slo.html", dashboard_operations_slo),
        ("operations_timeline.html", dashboard_operations_timeline),
        ("errors.html", dashboard_errors),
        ("config.html", dashboard_config),
        ("cr_per_cluster.html", dashboard_cr_per_cluster),
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
