"""
Генерация ER-диаграмм (PlantUML entity / Mermaid erDiagram) из TableDef.
"""

from __future__ import annotations

import re
from typing import Dict

from parsers.migration_schema import TableDef


def _sanitize_id(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", name)


def _ensure_stub_tables(tables: Dict[str, TableDef]) -> Dict[str, TableDef]:
    out = dict(tables)
    for t in list(tables.values()):
        for fk in t.foreign_keys:
            if fk.ref_table not in out:
                short = fk.ref_table.split(".")[-1]
                sch = "public"
                if "." in fk.ref_table:
                    sch, short = fk.ref_table.split(".", 1)
                out[fk.ref_table] = TableDef(name=short, schema_name=sch)
    return out


def generate_plantuml_er(tables: Dict[str, TableDef]) -> str:
    all_t = _ensure_stub_tables(tables)
    lines = [
        "@startuml ER_from_migrations",
        "!theme plain",
        "skinparam linetype ortho",
        "title ER (миграции)",
        "",
    ]
    for key in sorted(all_t.keys()):
        t = all_t[key]
        eid = _sanitize_id(key)
        lines.append(f'entity "{key}" as {eid} {{')
        for c in t.columns:
            lines.append(f"  {c.name} : {c.col_type}")
        if not t.columns:
            lines.append("  _")
        lines.append("}")
        lines.append("")

    seen: set = set()
    for key in sorted(tables.keys()):
        t = tables[key]
        src = _sanitize_id(key)
        for fk in t.foreign_keys:
            tgt_id = _sanitize_id(fk.ref_table)
            sig = (key, fk.from_col, fk.ref_table)
            if sig in seen:
                continue
            seen.add(sig)
            lines.append(f'{src} }}o--|| {tgt_id} : "{fk.from_col}"')
            lines.append("")

    lines.append("@enduml")
    lines.append("")
    return "\n".join(lines)


def _mermaid_type(ctype: str) -> str:
    t = ctype.split()[0].lower()
    if t in (
        "integer",
        "int",
        "int4",
        "bigint",
        "int8",
        "smallint",
        "serial",
        "bigserial",
    ):
        return "int"
    if t in ("uuid",):
        return "uuid"
    if t in ("boolean", "bool"):
        return "bool"
    if "timestamp" in t or t == "date":
        return "datetime"
    if t in ("text",) or t.startswith("varchar") or t.startswith("char"):
        return "string"
    if t in ("json", "jsonb"):
        return "json"
    if t in ("float", "double", "real", "numeric", "decimal"):
        return "float"
    return "string"


def generate_mermaid_er(tables: Dict[str, TableDef]) -> str:
    all_t = _ensure_stub_tables(tables)
    lines = ["erDiagram"]
    for key in sorted(all_t.keys()):
        t = all_t[key]
        eid = _sanitize_id(key)
        lines.append(f"    {eid} {{")
        if not t.columns:
            lines.append("        string _ref_only")
        else:
            for c in t.columns:
                lines.append(f"        {_mermaid_type(c.col_type)} {c.name}")
        lines.append("    }")

    seen: set = set()
    for key in sorted(tables.keys()):
        t = tables[key]
        src = _sanitize_id(key)
        for fk in t.foreign_keys:
            tgt = _sanitize_id(fk.ref_table)
            sig = (src, tgt, fk.from_col)
            if sig in seen:
                continue
            seen.add(sig)
            lines.append(f'    {src} }}|--|| {tgt} : "{fk.from_col}"')

    lines.append("")
    return "\n".join(lines)
