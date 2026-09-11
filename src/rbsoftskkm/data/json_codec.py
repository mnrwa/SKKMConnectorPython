"""Сериализация моделей: чтение ответов и запись тел запросов.

Два режима, как в эталонной реализации:

* чтение ответов — имена полей нечувствительны к регистру, неизвестные поля
  игнорируются;
* запись тела запроса — поля со значением ``None`` не сериализуются.
"""

from __future__ import annotations

import json
import sys
from dataclasses import MISSING, Field, fields, is_dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Any, Union, get_args, get_origin

JSON_NAME = "json"
JSON_ORDER = "order"

_hints_cache: dict[type, dict[str, Any]] = {}


def field_types(target: type) -> dict[str, Any]:
    """Аннотации класса, вычисленные в пространстве имён его модуля.

    Имя поля в моделях часто совпадает с именем типа (``LineStyle: LineStyle``),
    поэтому аннотации нельзя разрешать через словарь самого класса.
    """
    cached = _hints_cache.get(target)
    if cached is not None:
        return cached

    hints: dict[str, Any] = {}
    for base in reversed(target.__mro__):
        annotations = base.__dict__.get("__annotations__", {})
        if not annotations:
            continue
        module = sys.modules.get(base.__module__)
        namespace = vars(module) if module else {}
        for name, annotation in annotations.items():
            if isinstance(annotation, str):
                try:
                    hints[name] = eval(annotation, namespace)
                except NameError:
                    hints[name] = Any
            else:
                hints[name] = annotation

    _hints_cache[target] = hints
    return hints


def json_name(field_name: str, metadata: Any) -> str:
    return str(metadata.get(JSON_NAME, field_name))


def ordered_fields(target: type) -> list[Field[Any]]:
    """Поля в порядке сериализации: сначала JsonPropertyOrder, затем объявление."""
    items = list(fields(target))
    indexed = sorted(enumerate(items), key=lambda pair: (pair[1].metadata.get(JSON_ORDER, 0), pair[0]))
    return [item for _, item in indexed]


# ------------------------------------------------------------------- запись

def to_json_value(value: Any) -> Any:
    """Значение в структуру из dict/list/примитивов. Поля None отбрасываются."""
    if value is None:
        return None
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (bool, int, float, str, Decimal)):
        return value
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, (list, tuple)):
        return [to_json_value(item) for item in value]
    if isinstance(value, dict):
        return {str(key): to_json_value(item) for key, item in value.items() if item is not None}
    if is_dataclass(value) and not isinstance(value, type):
        result: dict[str, Any] = {}
        for item in ordered_fields(type(value)):
            raw = getattr(value, item.name)
            if raw is None:
                continue
            result[json_name(item.name, item.metadata)] = to_json_value(raw)
        return result
    return value


def dumps(value: Any, indent: int = 2) -> str:
    """JSON-текст без экранирования кириллицы; Decimal пишется как число."""
    return _write(to_json_value(value), indent, 0)


def _write(value: Any, indent: int, level: int) -> str:
    pad = " " * (indent * (level + 1))
    closing = " " * (indent * level)

    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, Decimal):
        return format(value.normalize(), "f")
    if isinstance(value, (int, float)):
        return json.dumps(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        if not value:
            return "[]"
        items = [pad + _write(item, indent, level + 1) for item in value]
        return "[" + _NEWLINE + ("," + _NEWLINE).join(items) + _NEWLINE + closing + "]"
    if isinstance(value, dict):
        if not value:
            return "{}"
        items = [
            pad + json.dumps(str(key), ensure_ascii=False) + ": " + _write(item, indent, level + 1)
            for key, item in value.items()
        ]
        return "{" + _NEWLINE + ("," + _NEWLINE).join(items) + _NEWLINE + closing + "}"
    return json.dumps(str(value), ensure_ascii=False)


_NEWLINE = "\n"


# ------------------------------------------------------------------ чтение

def parse_datetime(value: Any) -> datetime | None:
    """Даты сервера: 2026-09-03T16:27:36 и 2026-09-07T11:30:38.03+08:00."""
    if isinstance(value, datetime):
        return value
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        pass
    for pattern in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%Y%m%d%H%M%S"):
        try:
            return datetime.strptime(text, pattern)
        except ValueError:
            continue
    return None


def from_json(target: Any, value: Any) -> Any:
    """Значение JSON в объект указанного типа. Неизвестные поля игнорируются."""
    if target is Any or target is None:
        return value

    origin = get_origin(target)
    if origin is Union:
        args = [arg for arg in get_args(target) if arg is not type(None)]
        if value is None:
            return None
        return from_json(args[0], value) if args else value

    if value is None:
        return None

    if origin in (list, tuple):
        list_args = get_args(target)
        item_type = list_args[0] if list_args else Any
        if not isinstance(value, list):
            return []
        return [from_json(item_type, item) for item in value]

    if origin is dict:
        dict_args = get_args(target)
        value_type = dict_args[1] if len(dict_args) > 1 else Any
        if not isinstance(value, dict):
            return {}
        return {str(key): from_json(value_type, item) for key, item in value.items()}

    if isinstance(target, type):
        if issubclass(target, Enum):
            return _to_enum(target, value)
        if target is datetime:
            return parse_datetime(value)
        if target is Decimal:
            return _to_decimal(value)
        if target is bool:
            return bool(value)
        if target is int:
            return _to_int(value)
        if target is float:
            return float(value) if isinstance(value, (int, float, str)) else 0.0
        if target is str:
            return value if isinstance(value, str) else str(value)
        if is_dataclass(target):
            return _to_dataclass(target, value)

    return value


def _to_enum(target: type[Enum], value: Any) -> Any:
    try:
        return target(value)
    except ValueError:
        pass
    if isinstance(value, str):
        for member in target:
            if member.name.lower() == value.strip().lower():
                return member
    return None


def _to_decimal(value: Any) -> Decimal:
    if isinstance(value, Decimal):
        return value
    if isinstance(value, bool):
        return Decimal(0)
    if isinstance(value, (int, float, str)):
        try:
            return Decimal(str(value))
        except InvalidOperation:
            return Decimal(0)
    return Decimal(0)


def _to_int(value: Any) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float, Decimal)):
        return int(value)
    if isinstance(value, str):
        try:
            return int(float(value))
        except ValueError:
            return 0
    return 0


def _to_dataclass(target: type, value: Any) -> Any:
    if not isinstance(value, dict):
        return None

    lowered = {str(key).lower(): item for key, item in value.items()}
    hints = field_types(target)
    arguments: dict[str, Any] = {}

    for item in fields(target):
        raw = lowered.get(json_name(item.name, item.metadata).lower())
        if raw is None:
            raw = lowered.get(item.name.lower())
        if raw is None:
            continue
        arguments[item.name] = from_json(hints.get(item.name, Any), raw)

    required = [
        item.name
        for item in fields(target)
        if item.default is MISSING and item.default_factory is MISSING and item.name not in arguments
    ]
    for name in required:
        arguments[name] = None

    return target(**arguments)


def loads(text: str) -> Any:
    """JSON-текст в структуру; числа с точкой читаются как Decimal."""
    return json.loads(text, parse_float=Decimal)
