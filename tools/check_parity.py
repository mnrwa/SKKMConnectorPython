"""Сверка состава библиотеки с эталонной реализацией.

Запуск: python tools/check_parity.py <путь к репозиторию C#>

Считает публичные типы, перечисления, методы и свойства коннектора с обеих
сторон и печатает расхождения — по критериям приёмки состав должен совпадать.
"""

from __future__ import annotations

import argparse
import inspect
import re
import sys
from dataclasses import is_dataclass
from enum import IntEnum
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import rbsoftskkm  # noqa: E402
from rbsoftskkm.data import json_codec  # noqa: E402

CS_CLASS_RE = re.compile(r"^\s*(?:public|internal)\s+(?:sealed\s+|abstract\s+)?class\s+(?P<name>\w+)", re.MULTILINE)
CS_ENUM_RE = re.compile(r"^\s*public\s+enum\s+(?P<name>\w+)", re.MULTILINE)
CS_METHOD_RE = re.compile(r"^\s*public\s+(?:async\s+)?(?:Task|void)\s+(?P<name>\w+)\s*\(", re.MULTILINE)
CS_PROPERTY_RE = re.compile(r"^\s*public\s+[\w<>\[\],?.\s]+?\s+(?P<name>\w+)\s*\{\s*get;", re.MULTILINE)

CORE_FILES = {
    "state": "SkkmConnector.State.cs",
    "connection": "SkkmConnector.Connection.cs",
    "input": "SkkmConnector.CheckInput.cs",
}


def cs_names(pattern: re.Pattern[str], path: Path) -> list[str]:
    return pattern.findall(path.read_text(encoding="utf-8-sig"))


def python_side() -> dict[str, set[str]]:
    classes: set[str] = set()
    enums: set[str] = set()
    for name in rbsoftskkm.__all__:
        member = getattr(rbsoftskkm, name)
        if not inspect.isclass(member):
            continue
        if issubclass(member, IntEnum):
            enums.add(name)
        elif is_dataclass(member) or name == "Position":
            classes.add(name)

    connector = rbsoftskkm.SkkmConnector
    methods = {
        name
        for name, value in inspect.getmembers(connector, inspect.isfunction)
        if not name.startswith("_")
    }
    fields = {name for name in json_codec.field_types(connector) if not name.startswith("_")}
    return {"classes": classes, "enums": enums, "methods": methods, "fields": fields}


def csharp_side(root: Path) -> dict[str, set[str]]:
    connector_dir = root / "SkkmConnector"
    classes: set[str] = set()
    enums: set[str] = set()
    for path in (connector_dir / "Dto").rglob("*.cs"):
        classes.update(name for name in cs_names(CS_CLASS_RE, path))
        enums.update(cs_names(CS_ENUM_RE, path))
    classes -= enums

    core = connector_dir / "Core"
    methods = set(cs_names(CS_METHOD_RE, core / "SkkmConnector.Api.cs"))
    methods.update(cs_names(CS_METHOD_RE, core / "SkkmConnector.cs"))

    fields: set[str] = set()
    for file_name in CORE_FILES.values():
        fields.update(cs_names(CS_PROPERTY_RE, core / file_name))

    return {"classes": classes, "enums": enums, "methods": methods, "fields": fields}


def report(title: str, python: set[str], csharp: set[str]) -> bool:
    only_python = sorted(python - csharp)
    only_csharp = sorted(csharp - python)
    status = "совпадает" if not only_python and not only_csharp else "расхождение"
    print(f"{title}: python {len(python)}, эталон {len(csharp)} — {status}")
    if only_csharp:
        print("  нет в python: " + ", ".join(only_csharp))
    if only_python:
        print("  лишние в python: " + ", ".join(only_python))
    return not only_python and not only_csharp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args()

    python = python_side()
    csharp = csharp_side(args.source)

    ok = True
    ok &= report("Классы", python["classes"], csharp["classes"])
    ok &= report("Перечисления", python["enums"], csharp["enums"])
    ok &= report("Методы SkkmConnector", python["methods"], csharp["methods"])
    ok &= report("Поля SkkmConnector", python["fields"], csharp["fields"])
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
