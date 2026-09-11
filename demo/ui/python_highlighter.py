"""Подсветка Python-кода в панели «Запрос». Палитра как в IntelliJ (тёмная тема)."""

from __future__ import annotations

import keyword
import re

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat, QTextDocument

import rbsoftskkm

KEYWORD_COLOR = "#CF8E6D"
STRING_COLOR = "#6AAB73"
NUMBER_COLOR = "#2AACB8"
COMMENT_COLOR = "#7A7E85"
TYPE_COLOR = "#B5B6E3"
DEFAULT_COLOR = "#BCBEC4"

LIBRARY_NAMES = set(rbsoftskkm.__all__)
KEYWORDS = set(keyword.kwlist) | {"self", "match", "case"}

TOKEN_RE = re.compile(
    r"(?P<comment>#[^\n]*)"
    r"|(?P<string>\"\"\"(?:.|\n)*?\"\"\"|'''(?:.|\n)*?'''|\"(?:[^\"\\\n]|\\.)*\"|'(?:[^'\\\n]|\\.)*')"
    r"|(?P<number>\b\d+(?:\.\d+)?\b)"
    r"|(?P<ident>[A-Za-z_Ѐ-ӿ][A-Za-z0-9_Ѐ-ӿ]*)"
)


def text_format(color: str) -> QTextCharFormat:
    result = QTextCharFormat()
    result.setForeground(QColor(color))
    return result


class PythonHighlighter(QSyntaxHighlighter):
    """Раскрашивает ключевые слова, строки, числа, комментарии и типы библиотеки."""

    def __init__(self, document: QTextDocument) -> None:
        super().__init__(document)
        self.keyword_format = text_format(KEYWORD_COLOR)
        self.string_format = text_format(STRING_COLOR)
        self.number_format = text_format(NUMBER_COLOR)
        self.comment_format = text_format(COMMENT_COLOR)
        self.type_format = text_format(TYPE_COLOR)
        self.default_format = text_format(DEFAULT_COLOR)
        self.triple_quote = QRegularExpression(r'"""')

    def highlightBlock(self, text: str) -> None:  # noqa: N802 - имя из Qt
        self.setFormat(0, len(text), self.default_format)

        if self.previousBlockState() == 1:
            end = text.find('"""')
            if end < 0:
                self.setFormat(0, len(text), self.string_format)
                self.setCurrentBlockState(1)
                return
            self.setFormat(0, end + 3, self.string_format)
            offset = end + 3
        else:
            offset = 0

        self.setCurrentBlockState(0)
        for match in TOKEN_RE.finditer(text, offset):
            start, length = match.start(), match.end() - match.start()
            if match.lastgroup == "comment":
                self.setFormat(start, length, self.comment_format)
            elif match.lastgroup == "string":
                self.setFormat(start, length, self.string_format)
            elif match.lastgroup == "number":
                self.setFormat(start, length, self.number_format)
            else:
                word = match.group()
                if word in KEYWORDS:
                    self.setFormat(start, length, self.keyword_format)
                elif word in LIBRARY_NAMES or word[:1].isupper():
                    self.setFormat(start, length, self.type_format)

        opening = text.rfind('"""')
        if opening >= 0 and text.count('"""') % 2 == 1:
            self.setFormat(opening, len(text) - opening, self.string_format)
            self.setCurrentBlockState(1)
