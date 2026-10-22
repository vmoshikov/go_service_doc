"""Чтение Helm-чартов и CRD: версии, values с комментариями, схемы CRD."""
import json
import re
from pathlib import Path

import yaml

SECRET_KEY = re.compile(r"(?i)(password|passwd|secret|token|credential|private.?key|api.?key)")
KEY_LINE = re.compile(r"^(\s*)([\w.\-/]+):(\s|$)")
MAX_CRD_DEPTH = 4


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dig(data, dotted: str):
    """Значение по пути a.b.c. None, если пути нет."""
    for key in dotted.split(".") if dotted else []:
        if not isinstance(data, dict) or key not in data:
            return None
        data = data[key]
    return data


def split_ref(ref: str):
    """«файл#a.b.c» → ("файл", "a.b.c")."""
    file, _, dotted = ref.partition("#")
    return file, dotted


def flatten(data, prefix: str = "") -> list:
    """{a: {b: 1}} → [("a.b", 1)]. Списки и пустые словари — листья."""
    rows = []
    for key, value in (data or {}).items():
        path = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, dict) and value:
            rows += flatten(value, path)
        else:
            rows.append((path, value))
    return rows


def value_comments(text: str) -> dict:
    """Комментарии над ключами values.yaml: {a.b: текст}. Формат helm-docs «# --» тоже читается."""
    comments, stack, pending = {}, [], []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            pending.append(stripped.lstrip("#").strip().removeprefix("--").strip())
            continue
        match = KEY_LINE.match(line)
        if not match:
            pending = [] if not stripped else pending
            continue
        indent = len(match.group(1))
        while stack and stack[-1][0] >= indent:
            stack.pop()
        stack.append((indent, match.group(2)))
        text = " ".join(p for p in pending if p)
        if text:
            comments[".".join(k for _, k in stack)] = text
        pending = []
    return comments


def show(key: str, value) -> str:
    """Значение для таблицы. Значения секретов скрываются."""
    if value is None:
        return "—"
    if SECRET_KEY.search(key) and value not in ("", None, {}, []):
        return "`***`"
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    return f"`{text}`" if text != "" else '`""`'


# ---------- CRD ----------

def find_crds(dirs: list) -> list:
    """Все документы kind: CustomResourceDefinition в YAML-файлах каталогов dirs."""
    crds = []
    for base in dirs:
        if not base.is_dir():
            continue
        for path in sorted(list(base.rglob("*.yaml")) + list(base.rglob("*.yml"))):
            try:
                docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
            except yaml.YAMLError:
                continue  # шаблоны Helm с {{ }} не являются YAML
            crds += [d for d in docs if isinstance(d, dict) and d.get("kind") == "CustomResourceDefinition"]
    return crds


def crd_fields(schema: dict, prefix: str = "", depth: int = 0) -> list:
    """Поля схемы: [(путь, тип, обязательное, по умолчанию, описание)]."""
    rows = []
    required = set(schema.get("required", []))
    for name, prop in (schema.get("properties") or {}).items():
        path = f"{prefix}.{name}" if prefix else name
        ptype = prop.get("type", "")
        if ptype == "array":
            ptype = f"[]{(prop.get('items') or {}).get('type', '')}"
        if prop.get("format"):
            ptype += f" ({prop['format']})"
        rows.append((path, ptype, name in required, prop.get("default"), prop.get("description", "")))
        if depth + 1 < MAX_CRD_DEPTH:
            rows += crd_fields(prop, path, depth + 1)
            if prop.get("type") == "array" and isinstance(prop.get("items"), dict):
                rows += crd_fields(prop["items"], path + "[]", depth + 1)
    return rows
