"""
Сбор модели схемы БД из SQL-миграций (PostgreSQL-совместимый DDL, best effort).

Без подключения к БД: последовательный разбор CREATE TABLE / ALTER TABLE ... FOREIGN KEY.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import sqlparse
except ImportError:  # pragma: no cover
    sqlparse = None


@dataclass
class ColumnDef:
    name: str
    col_type: str


@dataclass
class ForeignKeyDef:
    from_col: str
    ref_table: str
    ref_col: str


@dataclass
class TableDef:
    name: str
    schema_name: str = "public"
    columns: List[ColumnDef] = field(default_factory=list)
    foreign_keys: List[ForeignKeyDef] = field(default_factory=list)


def _strip_sql_comments(sql: str) -> str:
    sql = re.sub(r"/\*[\s\S]*?\*/", " ", sql)
    sql = re.sub(r"--[^\n]*", " ", sql)
    return sql


def _split_statements(sql: str) -> List[str]:
    sql = _strip_sql_comments(sql)
    if sqlparse:
        parts = sqlparse.split(sql)  # type: ignore[union-attr]
        return [p.strip() for p in parts if p and p.strip()]
    return [p.strip() for p in sql.split(";") if p.strip()]


def _sort_key(path: Path) -> Tuple:
    m = re.match(r"^(\d+)", path.name)
    if m:
        return (0, int(m.group(1)), path.name.lower())
    return (1, 0, path.name.lower())


def discover_migration_files(go_dir: Path, paths: List[str], auto_discover: bool) -> List[Path]:
    found: List[Path] = []
    for rel in paths:
        p = go_dir / rel
        if p.is_dir():
            for f in sorted(p.rglob("*.sql"), key=_sort_key):
                if f.name.endswith(".down.sql"):
                    continue
                found.append(f)
        elif p.is_file() and p.suffix.lower() == ".sql":
            found.append(p)

    if not found and auto_discover:
        for candidate in ("migrations", "db/migrations", "internal/infrastructure/sql"):
            p = go_dir / candidate
            if p.is_dir():
                for f in sorted(p.rglob("*.sql"), key=_sort_key):
                    if f.name.endswith(".down.sql"):
                        continue
                    found.append(f)
                break
    # de-dup preserve order
    seen = set()
    uniq: List[Path] = []
    for f in sorted(found, key=lambda x: (str(x.relative_to(go_dir)), _sort_key(x))):
        rp = f.resolve()
        if rp not in seen:
            seen.add(rp)
            uniq.append(f)
    return uniq


_re_create = re.compile(
    r"(?is)CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?"
    r'(?:(?:"([^"]+)"|(\w+))\.)?(?:"([^"]+)"|(\w+))\s*\(',
)

_re_fk_inline = re.compile(
    r'(?is)REFERENCES\s+(?:(?:"([^"]+)"|(\w+))\.)?(?:"([^"]+)"|(\w+))\s*\(\s*(?:"([^"]+)"|(\w+))\s*\)',
)

_re_alter_fk = re.compile(
    r'(?is)ALTER\s+TABLE\s+(?:(?:"([^"]+)"|(\w+))\.)?(?:"([^"]+)"|(\w+))\s+'
    r'ADD\s+(?:CONSTRAINT\s+(?:"[^"]+"|\w+)\s+)?'
    r'FOREIGN\s+KEY\s*\(\s*(?:"([^"]+)"|(\w+))\s*\)\s*'
    r'REFERENCES\s+(?:(?:"([^"]+)"|(\w+))\.)?(?:"([^"]+)"|(\w+))\s*\(\s*(?:"([^"]+)"|(\w+))\s*\)',
)


def _parse_create_table(stmt: str, tables: Dict[str, TableDef], warnings: List[str]) -> None:
    m = _re_create.search(stmt)
    if not m:
        return
    sch = m.group(1) or m.group(2) or "public"
    tname = m.group(3) or m.group(4)
    if not tname:
        return
    key = f"{sch}.{tname}" if sch != "public" else tname
    if key not in tables:
        tables[key] = TableDef(name=tname, schema_name=sch)

    # find matching closing paren for column list (first opening after CREATE)
    start = stmt.find("(")
    if start < 0:
        return
    depth = 0
    end = -1
    for i, ch in enumerate(stmt[start:], start=start):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                end = i
                break
    if end < 0:
        warnings.append("CREATE TABLE: не найдена закрывающая скобка")
        return
    body = stmt[start + 1 : end]

    for raw_line in body.split("\n"):
        line = raw_line.strip().rstrip(",")
        if not line or line.upper().startswith("PRIMARY KEY"):
            continue
        if line.upper().startswith("CONSTRAINT") and "FOREIGN KEY" in line.upper():
            fm = _re_fk_inline.search(line)
            if fm:
                rs = fm.group(1) or fm.group(2) or "public"
                rt = fm.group(3) or fm.group(4)
                rc = fm.group(5) or fm.group(6)
                # local col: before REFERENCES
                local_m = re.search(
                    r"FOREIGN\s+KEY\s*\(\s*(?:\"([^\"]+)\"|(\w+))\s*\)",
                    line,
                    re.I,
                )
                if local_m and rt and rc:
                    lc = local_m.group(1) or local_m.group(2)
                    rkey = f"{rs}.{rt}" if rs != "public" else rt
                    tables[key].foreign_keys.append(
                        ForeignKeyDef(from_col=lc, ref_table=rkey, ref_col=rc)
                    )
            continue
        if "FOREIGN KEY" in line.upper() and "REFERENCES" in line.upper():
            fm = _re_fk_inline.search(line)
            local_m = re.search(
                r"FOREIGN\s+KEY\s*\(\s*(?:\"([^\"]+)\"|(\w+))\s*\)",
                line,
                re.I,
            )
            if fm and local_m:
                lc = local_m.group(1) or local_m.group(2)
                rs = fm.group(1) or fm.group(2) or "public"
                rt = fm.group(3) or fm.group(4)
                rc = fm.group(5) or fm.group(6)
                if rt and rc and lc:
                    rkey = f"{rs}.{rt}" if rs != "public" else rt
                    tables[key].foreign_keys.append(
                        ForeignKeyDef(from_col=lc, ref_table=rkey, ref_col=rc)
                    )
            continue

        # Inline: col TYPE ... REFERENCES other(col)
        if "REFERENCES" in line.upper() and "FOREIGN KEY" not in line.upper():
            fm = _re_fk_inline.search(line)
            if fm:
                head = re.split(r"\s+REFERENCES\s+", line, maxsplit=1, flags=re.I)[0].strip()
                hparts = head.split()
                if hparts:
                    cname = hparts[0].strip('"')
                    ctype = hparts[1] if len(hparts) > 1 else "unknown"
                    tables[key].columns.append(ColumnDef(name=cname, col_type=ctype))
                    rs = fm.group(1) or fm.group(2) or "public"
                    rt = fm.group(3) or fm.group(4)
                    rc = fm.group(5) or fm.group(6)
                    if rt and rc:
                        rkey = f"{rs}.{rt}" if rs != "public" else rt
                        tables[key].foreign_keys.append(
                            ForeignKeyDef(from_col=cname, ref_table=rkey, ref_col=rc)
                        )
            continue

        # column definition: name type ...
        cm = re.match(
            r'^\s*(?:"([^"]+)"|(\w+))\s+(\S+)',
            line,
        )
        if cm:
            cname = cm.group(1) or cm.group(2)
            ctype = cm.group(3)
            if cname.upper() in ("CONSTRAINT", "UNIQUE", "CHECK", "PRIMARY"):
                continue
            tables[key].columns.append(ColumnDef(name=cname, col_type=ctype))


def _parse_alter_table(stmt: str, tables: Dict[str, TableDef], warnings: List[str]) -> None:
    m = _re_alter_fk.search(stmt)
    if not m:
        return
    sch = m.group(1) or m.group(2) or "public"
    tname = m.group(3) or m.group(4)
    fcol = m.group(5) or m.group(6)
    rsch = m.group(7) or m.group(8) or "public"
    rtab = m.group(9) or m.group(10)
    rcol = m.group(11) or m.group(12)
    if not all([tname, fcol, rtab, rcol]):
        return
    key = f"{sch}.{tname}" if sch != "public" else tname
    if key not in tables:
        tables[key] = TableDef(name=tname, schema_name=sch)
    rkey = f"{rsch}.{rtab}" if rsch != "public" else rtab
    tables[key].foreign_keys.append(
        ForeignKeyDef(from_col=fcol, ref_table=rkey, ref_col=rcol)
    )


def build_schema_from_migration_files(files: List[Path]) -> Tuple[Dict[str, TableDef], List[str]]:
    tables: Dict[str, TableDef] = {}
    warnings: List[str] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            warnings.append(f"{path}: не прочитан ({e})")
            continue
        for stmt in _split_statements(text):
            su = stmt.upper()
            if "CREATE TABLE" in su:
                _parse_create_table(stmt, tables, warnings)
            elif "ALTER TABLE" in su and "FOREIGN KEY" in su:
                _parse_alter_table(stmt, tables, warnings)
    return tables, warnings


def build_schema_from_migrations(
    go_dir: Path,
    rules: Dict,
) -> Tuple[Dict[str, TableDef], List[str]]:
    er = rules.get("er_diagram") or {}
    paths = list(er.get("migrations_paths") or [])
    auto = bool(er.get("migrations_auto_discover", True))
    files = discover_migration_files(go_dir, paths, auto)
    if not files:
        return {}, ["Миграции не найдены (задайте er_diagram.migrations_paths или каталог migrations/)"]
    return build_schema_from_migration_files(files)
