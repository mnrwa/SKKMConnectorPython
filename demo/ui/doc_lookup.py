"""Подсказки по коду примера: описания методов, типов и полей из docs/*.json."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Optional

DOCS_DIR = Path(__file__).resolve().parent.parent / "resources" / "docs"

WORD_CHARS = "_"


@lru_cache(maxsize=1)
def documents() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Три словаря: методы, типы, поля. Файлы общие для всех реализаций."""
    return (
        load("methodDocs.json"),
        load("typeDocs.json"),
        load("fieldDocs.json"),
    )


def load(name: str) -> dict[str, str]:
    path = DOCS_DIR / name
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {str(key): str(value) for key, value in data.items()}


def is_word_char(char: str) -> bool:
    return char.isalnum() or char in WORD_CHARS


def word_at(code: str, index: int) -> Optional[tuple[str, int, int]]:
    if not code or index < 0 or index >= len(code):
        return None
    if not is_word_char(code[index]):
        if index > 0 and is_word_char(code[index - 1]):
            index -= 1
        else:
            return None

    start = index
    end = index
    while start > 0 and is_word_char(code[start - 1]):
        start -= 1
    while end + 1 < len(code) and is_word_char(code[end + 1]):
        end += 1
    word = code[start : end + 1]
    if not (word[0].isalpha() or word[0] == "_"):
        return None
    return word, start, end + 1


def followed_by_call(code: str, end: int) -> bool:
    index = end
    while index < len(code) and code[index].isspace():
        index += 1
    return index < len(code) and code[index] == "("


def preceded_by_dot(code: str, start: int) -> bool:
    index = start - 1
    while index >= 0 and code[index].isspace():
        index -= 1
    return index >= 0 and code[index] == "."


def summary_at(code: str, index: int) -> Optional[str]:
    """Описание имени под курсором.

    Правила как в эталонном демо: после имени скобка — метод, имя с заглавной —
    тип, перед именем точка — поле.
    """
    found = word_at(code, index)
    if found is None:
        return None

    word, start, end = found
    method_docs, type_docs, field_docs = documents()
    is_call = followed_by_call(code, end)
    is_type = word[:1].isupper()

    if is_call and word in method_docs:
        return method_docs[word]
    if is_type and word in type_docs:
        return type_docs[word]
    if not is_call and preceded_by_dot(code, start) and word in field_docs:
        return field_docs[word]
    if word in field_docs and not is_call:
        return field_docs[word]
    return None
