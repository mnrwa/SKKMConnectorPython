"""Подсветка JSON в панели «Ответ»."""

from __future__ import annotations

import re

from PySide6.QtGui import QSyntaxHighlighter, QTextDocument

from demo.ui.python_highlighter import text_format

KEY_COLOR = "#C77DBB"
STRING_COLOR = "#6AAB73"
NUMBER_COLOR = "#2AACB8"
LITERAL_COLOR = "#CF8E6D"
DEFAULT_COLOR = "#BCBEC4"

TOKEN_RE = re.compile(
    r"(?P<string>\"(?:[^\"\\]|\\.)*\")"
    r"|(?P<number>-?\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b)"
    r"|(?P<literal>\b(?:true|false|null)\b)"
)


class JsonHighlighter(QSyntaxHighlighter):
    """Ключи, строки, числа и литералы ответа сервера."""

    def __init__(self, document: QTextDocument) -> None:
        super().__init__(document)
        self.key_format = text_format(KEY_COLOR)
        self.string_format = text_format(STRING_COLOR)
        self.number_format = text_format(NUMBER_COLOR)
        self.literal_format = text_format(LITERAL_COLOR)
        self.default_format = text_format(DEFAULT_COLOR)

    def highlightBlock(self, text: str) -> None:  # noqa: N802 - имя из Qt
        self.setFormat(0, len(text), self.default_format)
        for match in TOKEN_RE.finditer(text):
            start, length = match.start(), match.end() - match.start()
            if match.lastgroup == "string":
                rest = text[match.end() :].lstrip()
                self.setFormat(start, length, self.key_format if rest.startswith(":") else self.string_format)
            elif match.lastgroup == "number":
                self.setFormat(start, length, self.number_format)
            else:
                self.setFormat(start, length, self.literal_format)
