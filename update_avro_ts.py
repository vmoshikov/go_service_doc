"""
update_avro_ts.py
-----------------
Обновляет все поля, заканчивающиеся на '_ts', в Avro-файлах на сегодняшнюю дату.

Использование:
    python update_avro_ts.py file1.avro file2.avro ...
    python update_avro_ts.py *.avro
    python update_avro_ts.py --dir /path/to/folder

Зависимости:
    pip install fastavro
"""

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import fastavro
    from fastavro import reader as avro_reader, writer as avro_writer, parse_schema
except ImportError:
    print("Установите fastavro: pip install fastavro")
    sys.exit(1)


# Сегодняшняя дата/время (UTC)
TODAY_TS = datetime.now(timezone.utc)
TODAY_DATE_STR = TODAY_TS.strftime("%Y-%m-%dT%H:%M:%SZ")


def detect_ts_type(schema, field_name: str):
    """
    Определяет тип поля _ts в схеме (int/long timestamp, string, или plain).
    Возвращает: 'timestamp-millis', 'timestamp-micros', 'date', 'string', 'long', 'int', None
    """
    if not isinstance(schema, dict):
        return None

    fields = schema.get("fields", [])
    for f in fields:
        if f.get("name") == field_name:
            ftype = f.get("type")
            # Разворачиваем union ["null", {...}]
            if isinstance(ftype, list):
                for t in ftype:
                    if isinstance(t, dict):
                        ftype = t
                        break
            if isinstance(ftype, dict):
                logical = ftype.get("logicalType")
                if logical in ("timestamp-millis", "timestamp-micros", "date"):
                    return logical
                return ftype.get("type")
            if isinstance(ftype, str):
                return ftype
    return None


def new_ts_value(ts_type: str):
    """Возвращает новое значение _ts в зависимости от типа поля."""
    if ts_type == "timestamp-millis":
        return int(TODAY_TS.timestamp() * 1_000)
    elif ts_type == "timestamp-micros":
        return int(TODAY_TS.timestamp() * 1_000_000)
    elif ts_type == "date":
        # Avro date — количество дней с 1970-01-01
        return (TODAY_TS.date() - datetime(1970, 1, 1).date()).days
    elif ts_type == "string":
        return TODAY_DATE_STR
    elif ts_type in ("long", "int"):
        # Предполагаем epoch-секунды
        return int(TODAY_TS.timestamp())
    else:
        # Неизвестный тип — пробуем строку
        return TODAY_DATE_STR


def update_record(record: dict, ts_fields: dict) -> dict:
    """Рекурсивно обновляет все _ts-поля в записи."""
    updated = {}
    for key, value in record.items():
        if key in ts_fields:
            updated[key] = new_ts_value(ts_fields[key])
        elif isinstance(value, dict):
            updated[key] = update_record(value, ts_fields)
        elif isinstance(value, list):
            updated[key] = [
                update_record(v, ts_fields) if isinstance(v, dict) else v
                for v in value
            ]
        else:
            updated[key] = value
    return updated


def find_ts_fields(schema) -> dict:
    """
    Находит все поля, заканчивающиеся на '_ts', в схеме.
    Возвращает словарь {field_name: ts_type}.
    """
    ts_fields = {}
    if not isinstance(schema, dict):
        return ts_fields

    for field in schema.get("fields", []):
        name = field.get("name", "")
        if name.endswith("_ts"):
            ts_fields[name] = detect_ts_type(schema, name)

    return ts_fields


def process_avro_file(input_path: Path, output_path: Path = None, inplace: bool = False):
    """Читает Avro-файл, обновляет _ts-поля, записывает результат."""
    if output_path is None:
        if inplace:
            output_path = input_path
        else:
            output_path = input_path.with_stem(input_path.stem + "_updated")

    # Читаем все записи и схему
    with open(input_path, "rb") as f:
        avro_file = avro_reader(f)
        schema = avro_file.writer_schema
        records = list(avro_file)

    ts_fields = find_ts_fields(schema)

    if not ts_fields:
        print(f"  [!] Поля _ts не найдены в {input_path.name} — файл пропущен.")
        return

    print(f"  Найдены поля _ts: {list(ts_fields.keys())}")

    updated_records = [update_record(r, ts_fields) for r in records]

    parsed = parse_schema(schema)
    tmp_path = output_path.with_suffix(".tmp.avro")

    with open(tmp_path, "wb") as out:
        avro_writer(out, parsed, updated_records)

    tmp_path.replace(output_path)
    print(f"  -> Сохранено: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Обновляет поля _ts в Avro-файлах на сегодняшнюю дату."
    )
    parser.add_argument("files", nargs="*", help="Avro-файлы для обработки")
    parser.add_argument("--dir", help="Папка с Avro-файлами")
    parser.add_argument(
        "--inplace", action="store_true",
        help="Перезаписать оригинальные файлы (без флага создаёт *_updated.avro)"
    )
    args = parser.parse_args()

    targets = []

    if args.dir:
        targets = list(Path(args.dir).glob("*.avro"))
        if not targets:
            print(f"Avro-файлы не найдены в {args.dir}")
            sys.exit(1)
    elif args.files:
        targets = [Path(f) for f in args.files]
    else:
        parser.print_help()
        sys.exit(0)

    print(f"Дата обновления: {TODAY_DATE_STR}")
    print(f"Файлов к обработке: {len(targets)}\n")

    for path in targets:
        if not path.exists():
            print(f"  [!] Файл не найден: {path}")
            continue
        print(f"Обрабатываю: {path.name}")
        try:
            process_avro_file(path, inplace=args.inplace)
        except Exception as e:
            print(f"  [ОШИБКА] {e}")

    print("\nГотово.")


if __name__ == "__main__":
    main()