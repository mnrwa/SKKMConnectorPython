"""Перенос API.md из эталонного репозитория: меняется только колонка типов.

Запуск: python tools/convert_api_doc.py <путь к API.md эталона> [<файл назначения>]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TYPE_MAP = {
    "string": "str",
    "String": "str",
    "decimal": "Decimal",
    "DateTime": "datetime",
    "TimeSpan": "timedelta",
    "JsonElement": "Any",
    "long": "int",
    "double": "float",
    "float": "float",
    "object": "Any",
    "guid": "str",
    "Guid": "str",
}

ARRAY_RE = re.compile(r"^(?P<item>.+?)\[\]$")
GENERIC_RE = re.compile(r"^(?:List|IReadOnlyList|IList|IEnumerable)<(?P<item>.+)>$")
LINK_RE = re.compile(r"^\[(?P<title>[^\]]+)\]\((?P<anchor>[^)]+)\)$")


def convert_type(value: str) -> str:
    text = value.strip()
    if not text or text == "-":
        return value

    if text.startswith("`") and text.endswith("`"):
        return f"`{convert_type(text[1:-1])}`"

    array = ARRAY_RE.match(text)
    if array:
        return f"list[{convert_type(array.group('item'))}]"

    generic = GENERIC_RE.match(text)
    if generic:
        return f"list[{convert_type(generic.group('item'))}]"

    if LINK_RE.match(text):
        return text

    return TYPE_MAP.get(text, text)


def convert_line(line: str) -> tuple[str, int]:
    if not line.startswith("|"):
        return line, 0

    prefix_spaces = ""
    cells = line.rstrip().strip("|").split("|")
    if len(cells) < 2:
        return line, 0
    if set(cells[0].strip()) <= set("-: ") and cells[0].strip():
        return line, 0
    if cells[0].strip().startswith("**"):
        return line, 0

    # В эталоне одна строка со сдвинутыми колонками: тип стоит третьим.
    index = 1
    if cells[1].strip() == "-" and len(cells) > 2 and cells[2].strip() in TYPE_MAP:
        index = 2

    original = cells[index]
    converted = convert_type(original)
    if converted == original.strip():
        return line, 0

    # Ширину ячейки сохраняем: в эталоне таблицы выровнены по столбцам.
    cells[index] = f" {converted} ".ljust(len(original))
    return f"{prefix_spaces}|" + "|".join(cells) + "|", 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path, nargs="?", default=Path("API.md"))
    args = parser.parse_args()

    replaced = 0
    lines: list[str] = []
    for line in args.source.read_text(encoding="utf-8").splitlines():
        converted, count = convert_line(line)
        replaced += count
        lines.append(converted)

    args.target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"замен типов: {replaced}, строк: {len(lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
