"""Разбор .proto: сервисы, методы, HTTP-привязки grpc-gateway, сообщения, enum.

Разбор построчный. Вложенные сообщения и oneof не раскрываются: поля верхнего уровня
показываются, вложенные блоки пропускаются.
"""
import re
from dataclasses import dataclass, field
from pathlib import Path

RPC_RE = re.compile(r"^rpc\s+(\w+)\s*\(\s*(stream\s+)?([\w.]+)\s*\)\s*returns\s*\(\s*(stream\s+)?([\w.]+)\s*\)")
HTTP_RE = re.compile(r"\b(get|post|put|patch|delete)\s*:\s*\"([^\"]+)\"")
FIELD_RE = re.compile(r"^(repeated\s+|optional\s+)?(map<[^>]+>|[\w.]+)\s+(\w+)\s*=\s*(\d+)")
ENUM_VALUE_RE = re.compile(r"^(\w+)\s*=\s*(-?\d+)")


@dataclass
class Rpc:
    name: str
    request: str
    response: str
    client_stream: bool
    server_stream: bool
    comment: str
    line: int
    http: list = field(default_factory=list)  # [(метод, путь)]


@dataclass
class Service:
    name: str
    comment: str
    file: str
    line: int
    rpcs: list = field(default_factory=list)


@dataclass
class Message:
    name: str
    kind: str  # message или enum
    comment: str
    file: str
    line: int
    fields: list = field(default_factory=list)  # [(тип, имя, номер, комментарий)]


def parse_proto(path: Path, rel: str):
    """Возвращает (пакет, [Service], {имя: Message})."""
    package, services, messages = "", [], {}
    comment, depth = [], 0
    block = None          # текущий service/message/enum верхнего уровня
    rpc = None            # текущий rpc с блоком опций
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        code, _, trailing = raw.partition("//")
        line = code.strip()
        if not line:
            if raw.strip().startswith("//"):
                comment.append(trailing.strip())
            else:
                comment = []
            continue
        text = " ".join(comment)
        comment = []

        if depth == 0:
            if line.startswith("package "):
                package = line.removeprefix("package ").rstrip(";").strip()
            elif m := re.match(r"^service\s+(\w+)", line):
                block = Service(m.group(1), text, rel, number)
                services.append(block)
            elif m := re.match(r"^(message|enum)\s+(\w+)", line):
                block = Message(m.group(2), m.group(1), text, rel, number)
                messages[block.name] = block
                inline = line.partition("{")[2].rpartition("}")[0]  # message X { поля } в одну строку
                for part in filter(None, (p.strip() for p in inline.split(";"))):
                    if block.kind == "message" and (f := FIELD_RE.match(part)):
                        block.fields.append((((f.group(1) or "") + f.group(2)).strip(), f.group(3), f.group(4), ""))
                    elif block.kind == "enum" and (f := ENUM_VALUE_RE.match(part)):
                        block.fields.append(("", f.group(1), f.group(2), ""))
        elif depth == 1 and isinstance(block, Service) and (m := RPC_RE.match(line)):
            rpc = Rpc(m.group(1), m.group(3), m.group(5), bool(m.group(2)), bool(m.group(4)), text, number)
            block.rpcs.append(rpc)
        elif depth == 1 and isinstance(block, Message):
            if block.kind == "message" and (m := FIELD_RE.match(line)):
                kind = (m.group(1) or "").strip()
                ftype = f"{kind} {m.group(2)}".strip()
                block.fields.append((ftype, m.group(3), m.group(4), trailing.strip() or text))
            elif block.kind == "enum" and (m := ENUM_VALUE_RE.match(line)):
                block.fields.append(("", m.group(1), m.group(2), trailing.strip() or text))
        if rpc is not None and depth >= 2:
            rpc.http.extend((verb.upper(), url) for verb, url in HTTP_RE.findall(line))

        depth += line.count("{") - line.count("}")
        if depth <= 1:
            rpc = None
        if depth == 0:
            block = None
    return package, services, messages


def parse_protos(repo: Path, exclude: list):
    """Все .proto репозитория: ([(пакет, Service)], {имя: Message})."""
    services, messages = [], {}
    for path in sorted(repo.rglob("*.proto")):
        rel = path.relative_to(repo).as_posix()
        if any(p in ("vendor", "third_party") or p.startswith(".") for p in rel.split("/")[:-1]):
            continue
        if any(rel.startswith(e.rstrip("/") + "/") for e in exclude):
            continue
        package, file_services, file_messages = parse_proto(path, rel)
        services += [(package, s) for s in file_services]
        messages.update(file_messages)
    return services, messages
