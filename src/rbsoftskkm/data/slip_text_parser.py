"""Разбор текста с разметкой в строки нефискального документа.

Префиксы: [big], [center], [QR], [line], [line,dotted], [dotted].
"""

from __future__ import annotations

from enum import Enum
from typing import Optional, TypeVar

from rbsoftskkm.data.contracts.doc_position import DocPosition
from rbsoftskkm.data.contracts.text_string import TextString
from rbsoftskkm.dto.enums.barcode_type import BarcodeType
from rbsoftskkm.dto.enums.line_style import LineStyle
from rbsoftskkm.dto.enums.print_alignment import PrintAlignment
from rbsoftskkm.dto.enums.print_font import PrintFont
from rbsoftskkm.dto.positions.barcode_line import BarcodeLine
from rbsoftskkm.dto.positions.separator_line import SeparatorLine

TEnum = TypeVar("TEnum", bound=Enum)


def Parse(text: str) -> list[DocPosition]:
    return [ParseLine(line) for line in text.replace("\r\n", "\n").split("\n")]


def ParseLine(line: str, font: Optional[str] = None, alignment: Optional[str] = None) -> DocPosition:
    """Одна строка: префиксы в тексте превращаются в SeparatorLine / Barcode / TextString."""
    parsed_alignment = parse_enum(PrintAlignment, alignment)
    parsed_font = parse_enum(PrintFont, font)
    barcode_type: Optional[BarcodeType] = None
    line_style: Optional[LineStyle] = None
    has_line_tag = False

    if line.startswith("[") and "]" in line:
        close = line.index("]")
        tags = [tag.strip() for tag in line[1:close].split(",") if tag.strip()]
        recognized = False

        for tag in tags:
            if tag.lower() == "line":
                has_line_tag = True
                recognized = True

        for tag in tags:
            if not tag or tag[0].isdigit():
                continue

            style = try_line_style(tag, has_line_tag)
            if style is not None:
                line_style = style
            elif parse_enum(BarcodeType, tag) is not None:
                barcode_type = parse_enum(BarcodeType, tag)
            elif parse_enum(PrintAlignment, tag) is not None:
                parsed_alignment = parse_enum(PrintAlignment, tag)
            elif parse_enum(PrintFont, tag) is not None:
                parsed_font = parse_enum(PrintFont, tag)
            else:
                continue

            recognized = True

        # Префикс в квадратных скобках срезаем только если внутри распознан тег
        # (center, dotted, QR, line…). Обычный текст вида «[Промо]» остаётся как есть.
        if recognized:
            line = line[close + 1 :]

    if has_line_tag or (line_style is not None and len(line) == 0):
        return DocPosition(SeparatorLine=SeparatorLine(LineStyle=line_style or LineStyle.Solid))

    if barcode_type is not None:
        return DocPosition(
            Barcode=BarcodeLine(
                Type=barcode_type.name,
                Barcode=line.strip(),
                Alignment=parsed_alignment.name.lower() if parsed_alignment is not None else None,
            )
        )

    return DocPosition(
        TextString=TextString(
            Text=line,
            Font=parsed_font.name if parsed_font is not None else None,
            Alignment=parsed_alignment.name.lower() if parsed_alignment is not None else None,
        )
    )


def try_line_style(tag: str, has_line_tag: bool) -> Optional[LineStyle]:
    """[dotted] / [dashed] / [solid] / [double] — линия. [bold] — шрифт, линия только вместе с [line]."""
    style = parse_enum(LineStyle, tag)
    if style is None:
        return None
    if style == LineStyle.Bold and not has_line_tag:
        return None
    return style


def parse_enum(target: type[TEnum], value: Optional[str]) -> Optional[TEnum]:
    if value is None or not value.strip():
        return None
    text = value.strip().lower()
    for member in target:
        if member.name.lower() == text:
            return member
    return None
