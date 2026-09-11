"""Исходный текст примера для панели «Запрос»."""

from __future__ import annotations

import inspect
import re
from pathlib import Path

from demo.ui.example_host import ExampleItem

IMPORT_RE = re.compile(r"^from rbsoftskkm import .*?(?:\n|$)|^from rbsoftskkm import \([^)]*\)\n", re.MULTILINE | re.DOTALL)
STDLIB_RE = re.compile(r"^from (?:decimal|datetime) import .*$", re.MULTILINE)


def read(example: ExampleItem) -> str:
    """Читает файл примера с диска и оформляет его как клиентский код."""
    module = inspect.getmodule(type(example.Instance))
    path = Path(inspect.getfile(type(example.Instance))) if module is None else Path(str(module.__file__))
    if not path.exists():
        return ""
    return format_for_display(path.read_text(encoding="utf-8"), example.MethodName)


def format_for_display(text: str, method_name: str) -> str:
    header = imports(text)
    body = method_body(text, method_name)
    if not body:
        return text.strip()

    lines = [line for line in body.splitlines() if line.strip() != "kkm = self.kkm"]
    body = unindent("\n".join(lines)).strip("\n")
    body = re.sub(r"\n\s*return kkm\s*$", "", body)
    body = body.replace("self.", "")

    prefix = header + "\n\n" if header else ""
    return f"{prefix}kkm = SkkmConnector()\n{body.rstrip()}\n"


def imports(text: str) -> str:
    """Импорты примера: библиотека и стандартные модули, без служебных строк."""
    collected: list[str] = []
    for match in STDLIB_RE.finditer(text):
        collected.append(match.group().strip())

    start = text.find("from rbsoftskkm import")
    if start >= 0:
        end = text.find("\n\n", start)
        collected.append(text[start : end if end > 0 else len(text)].rstrip())
    return "\n".join(collected)


def method_body(text: str, method_name: str) -> str:
    marker = f"    def {method_name}(self)"
    start = text.find(marker)
    if start < 0:
        return ""
    body_start = text.find("\n", start)
    if body_start < 0:
        return ""

    lines: list[str] = []
    for line in text[body_start + 1 :].splitlines():
        if line.strip() and not line.startswith(" " * 8):
            break
        lines.append(line)
    return "\n".join(lines)


def unindent(text: str) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    widths = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    pad = min(widths) if widths else 0
    if pad <= 0:
        return text
    return "\n".join(line[pad:] if len(line) >= pad else line for line in lines)
