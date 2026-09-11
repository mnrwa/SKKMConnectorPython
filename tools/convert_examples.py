"""Конвертер примеров демо-приложения из C# в Python.

Запуск: python tools/convert_examples.py <каталог Examples C#> [<каталог demo/examples>]

Синтаксис примеров ограничен: присваивания, инициализаторы объектов, вызовы
методов коннектора и проверка kkm.Ok. Типы полей берутся из библиотеки
rbsoftskkm, поэтому числовые литералы в decimal-полях становятся Decimal.
"""

from __future__ import annotations

import argparse
import keyword
import re
import subprocess
import sys
from dataclasses import dataclass, field, is_dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any, Optional, Union, get_args, get_origin

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import rbsoftskkm  # noqa: E402
from rbsoftskkm.data import json_codec  # noqa: E402

PUBLIC_NAMES: dict[str, Any] = {name: getattr(rbsoftskkm, name) for name in rbsoftskkm.__all__}

SAMPLE_FIELDS = {"deviceName", "cashierName", "cashierVatin", "documentId", "fromDate", "toDate"}
LINE_WIDTH = 100


# ------------------------------------------------------------------- разбор

@dataclass
class Token:
    kind: str  # ident | number | string | punct | comment
    text: str


TOKEN_RE = re.compile(
    r"""
    (?P<comment>///.*?$|//.*?$)
  | (?P<string>@"(?:[^"]|"")*"|"(?:[^"\\]|\\.)*")
  | (?P<char>'(?:[^'\\]|\\.)*')
  | (?P<number>\d+(?:\.\d+)?[mMdDfF]?)
  | (?P<ident>[A-Za-z_Ѐ-ӿ][A-Za-z0-9_Ѐ-ӿ]*)
  | (?P<punct>[{}()\[\];,=.!+<>:?-])
    """,
    re.VERBOSE | re.MULTILINE,
)


def tokenize(text: str) -> list[Token]:
    tokens: list[Token] = []
    for match in TOKEN_RE.finditer(text):
        kind = match.lastgroup or "punct"
        value = match.group()
        if kind == "comment":
            tokens.append(Token("comment", value))
        elif kind == "char":
            tokens.append(Token("string", value))
        else:
            tokens.append(Token(kind, value))
    return tokens


@dataclass
class Node:
    kind: str  # new | name | literal | call | array | concat
    text: str = ""
    type_name: str = ""
    args: list["Node"] = field(default_factory=list)
    items: list[tuple[str, "Node"]] = field(default_factory=list)


class Parser:
    """Разбор ограниченного подмножества C#, встречающегося в примерах."""

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.position = 0

    def peek(self, offset: int = 0) -> Optional[Token]:
        index = self.position + offset
        return self.tokens[index] if index < len(self.tokens) else None

    def next(self) -> Token:
        token = self.tokens[self.position]
        self.position += 1
        return token

    def accept(self, text: str) -> bool:
        token = self.peek()
        if token is not None and token.text == text:
            self.position += 1
            return True
        return False

    def expect(self, text: str) -> Token:
        token = self.next()
        if token.text != text:
            raise ValueError(f"ожидался «{text}», получено «{token.text}»")
        return token

    # выражения

    def parse_expression(self) -> Node:
        node = self.parse_primary()
        while True:
            token = self.peek()
            if token is not None and token.text == "+":
                self.next()
                right = self.parse_primary()
                if node.kind == "concat":
                    node.args.append(right)
                else:
                    node = Node("concat", args=[node, right])
                continue
            break
        return node

    def parse_primary(self) -> Node:
        token = self.next()

        if token.kind in ("string", "number"):
            return Node("literal", text=token.text)

        if token.text == "[":
            return self.parse_array("]")

        if token.kind == "ident" and token.text == "new":
            return self.parse_new()

        if token.kind == "ident":
            parts = [token.text]
            while self.peek() is not None and self.peek().text == "." and self.peek(1) is not None:  # type: ignore[union-attr]
                self.next()
                parts.append(self.next().text)
            name = Node("name", text=".".join(parts))
            if self.peek() is not None and self.peek().text == "(":  # type: ignore[union-attr]
                self.next()
                call = Node("call", text=name.text)
                while not self.accept(")"):
                    call.args.append(self.parse_expression())
                    self.accept(",")
                return call
            return name

        raise ValueError(f"неожиданный токен «{token.text}»")

    def parse_new(self) -> Node:
        token = self.peek()
        if token is None:
            raise ValueError("оборванное выражение new")

        type_name = ""
        if token.text == "[":  # new[] { ... }
            self.next()
            self.expect("]")
        else:
            type_name = self.next().text
            while self.peek() is not None and self.peek().text == ".":  # type: ignore[union-attr]
                self.next()
                type_name = self.next().text
            if self.accept("["):
                self.expect("]")
                type_name = ""

        node = Node("new", type_name=type_name)
        if self.accept("("):
            while not self.accept(")"):
                node.args.append(self.parse_expression())
                self.accept(",")

        if self.accept("{"):
            if not type_name:
                array = self.parse_array("}")
                array.type_name = type_name
                return array
            while not self.accept("}"):
                name_token = self.next()
                if name_token.text == ",":
                    continue
                self.expect("=")
                value = self.parse_initializer_value()
                node.items.append((name_token.text, value))
                self.accept(",")
        return node

    def parse_initializer_value(self) -> Node:
        token = self.peek()
        if token is not None and token.text == "{":
            self.next()
            return self.parse_array("}")
        return self.parse_expression()

    def parse_array(self, closing: str) -> Node:
        node = Node("array")
        while not self.accept(closing):
            node.args.append(self.parse_initializer_value())
            self.accept(",")
        return node


# --------------------------------------------------------------- кодогенерация

def field_type(owner: str, name: str) -> Any:
    """Тип поля по имени класса библиотеки; None, если тип неизвестен."""
    target = PUBLIC_NAMES.get(owner)
    if target is None or not isinstance(target, type):
        return None
    if is_dataclass(target):
        return json_codec.field_types(target).get(name)
    return None


def connector_field_type(name: str) -> Any:
    connector = PUBLIC_NAMES["SkkmConnector"]
    return json_codec.field_types(connector).get(name)


def is_decimal_type(annotation: Any) -> bool:
    if annotation is Decimal:
        return True
    if get_origin(annotation) is Union:
        return any(arg is Decimal for arg in get_args(annotation))
    return False


def python_string(text: str) -> str:
    """C#-литерал в Python-литерал: экранирование и управляющие символы."""
    if text.startswith("@"):
        value = text[2:-1].replace('""', '"')
    elif text.startswith("'"):
        value = decode_escapes(text[1:-1])
    else:
        value = decode_escapes(text[1:-1])

    result = ['"']
    for char in value:
        if char == '"':
            result.append('\\"')
        elif char == "\\":
            result.append("\\\\")
        elif char == "\n":
            result.append("\\n")
        elif char == "\r":
            result.append("\\r")
        elif char == "\t":
            result.append("\\t")
        elif ord(char) < 32 or ord(char) == 127:
            result.append(f"\\x{ord(char):02x}")
        else:
            result.append(char)
    result.append('"')
    return "".join(result)


ESCAPES = {"n": "\n", "r": "\r", "t": "\t", "0": "\0", "\\": "\\", '"': '"', "'": "'"}


def decode_escapes(value: str) -> str:
    result: list[str] = []
    index = 0
    while index < len(value):
        char = value[index]
        if char == "\\" and index + 1 < len(value):
            following = value[index + 1]
            if following in ESCAPES:
                result.append(ESCAPES[following])
                index += 2
                continue
            if following in "uU":
                size = 4 if following == "u" else 8
                code = value[index + 2 : index + 2 + size]
                result.append(chr(int(code, 16)))
                index += 2 + size
                continue
            if following == "x":
                match = re.match(r"[0-9a-fA-F]{1,4}", value[index + 2 :])
                if match:
                    result.append(chr(int(match.group(), 16)))
                    index += 2 + len(match.group())
                    continue
        result.append(char)
        index += 1
    return "".join(result)


def python_name(text: str) -> str:
    """Идентификатор C# в Python: поля примера, DateTime и члены перечислений."""
    if text == "DateTime.Today":
        return "datetime.combine(date.today(), time.min)"
    if text == "DateTime.Now":
        return "datetime.now()"

    parts = text.split(".")
    if parts[0] in SAMPLE_FIELDS:
        parts[0] = f"self.{parts[0]}"
    if len(parts) == 2 and keyword.iskeyword(parts[1]):
        parts[1] = f"{parts[1]}_"
    return ".".join(parts)


def render_number(text: str, decimal_expected: bool) -> str:
    literal = text.rstrip("mMdDfF")
    if text[-1] in "mM" or decimal_expected:
        return f'Decimal("{literal}")'
    return literal


def render(node: Node, indent: int, decimal_expected: bool = False) -> list[str]:
    """Строки выражения: первая — без отступа, остальные — относительно её начала."""
    if node.kind == "literal":
        if node.text[0] in "\"'@":
            return [python_string(node.text)]
        return [render_number(node.text, decimal_expected)]

    if node.kind == "name":
        if node.text == "true":
            return ["True"]
        if node.text == "false":
            return ["False"]
        if node.text == "null":
            return ["None"]
        return [python_name(node.text)]

    if node.kind == "concat":
        lines = ["("]
        for item in node.args:
            for text in render(item, indent + 4):
                lines.append("    " + text)
        lines.append(")")
        return lines

    if node.kind == "call":
        arguments = [render(argument, indent)[0] for argument in node.args]
        return [f"{python_name(node.text)}({', '.join(arguments)})"]

    if node.kind == "array":
        if not node.args:
            return ["[]"]
        rendered = [render(item, indent + 4, decimal_expected) for item in node.args]
        single = "[" + ", ".join(block[0] for block in rendered if len(block) == 1) + "]"
        if all(len(block) == 1 for block in rendered) and len(single) + indent <= LINE_WIDTH:
            return [single]
        lines = ["["]
        for block in rendered:
            lines.append("    " + block[0])
            for extra in block[1:]:
                lines.append("    " + extra)
            lines[-1] += ","
        lines.append("]")
        return lines

    if node.kind == "new":
        return render_new(node, indent)

    raise ValueError(f"неизвестный узел {node.kind}")


def render_new(node: Node, indent: int) -> list[str]:
    type_name = node.type_name
    arguments: list[tuple[str, list[str]]] = []

    for value in node.args:
        arguments.append(("", render(value, indent + 4)))

    for name, value in node.items:
        annotation = field_type(type_name, name)
        expects_decimal = is_decimal_type(annotation)
        if get_origin(annotation) in (list, Union):
            args = [arg for arg in get_args(annotation) if arg is not type(None)]
            inner = get_args(args[0])[0] if args and get_origin(args[0]) is list else None
            expects_decimal = expects_decimal or inner is Decimal
        arguments.append((name, render(value, indent + 4, expects_decimal)))

    single_parts = [
        (f"{name}={block[0]}" if name else block[0]) for name, block in arguments if len(block) == 1
    ]
    if len(single_parts) == len(arguments):
        single = f"{type_name}({', '.join(single_parts)})"
        if len(single) + indent <= LINE_WIDTH:
            return [single]

    lines = [f"{type_name}("]
    for name, block in arguments:
        lines.append("    " + (f"{name}=" if name else "") + block[0])
        for extra in block[1:]:
            lines.append("    " + extra)
        lines[-1] += ","
    lines.append(")")
    return lines


# ---------------------------------------------------------------- операторы

def convert_body(tokens: list[Token], indent: int) -> list[str]:
    parser = Parser(tokens)
    lines: list[str] = []
    pad = " " * indent

    while parser.position < len(parser.tokens):
        token = parser.peek()
        if token is None:
            break

        if token.kind == "comment":
            parser.next()
            text = token.text.lstrip("/").strip()
            lines.append("")
            lines.append(pad + f"# {text}")
            continue

        if token.text == ";":
            parser.next()
            continue

        if token.text == "if":
            parser.next()
            parser.expect("(")
            negated = parser.accept("!")
            condition = parser.parse_expression()
            parser.expect(")")
            condition_text = python_name(condition.text)
            lines.append("")
            lines.append(pad + f"if {'not ' if negated else ''}{condition_text}:")
            lines.extend(convert_body(read_statement(parser), indent + 4))
            continue

        if token.text == "throw":
            parser.next()
            expression = parser.parse_expression()
            argument = render(expression.items[0][1], indent) if expression.items else None
            if expression.kind == "new":
                inner = expression.args[0] if expression.args else None
                argument = render(inner, indent) if inner is not None else ["\"\""]
            lines.append(pad + f"raise RuntimeError({argument[0] if argument else ''})")
            parser.accept(";")
            continue

        if token.text == "return":
            parser.next()
            expression = parser.parse_expression()
            lines.append("")
            lines.append(pad + f"return {python_name(expression.text)}")
            parser.accept(";")
            continue

        if token.text == "await":
            parser.next()
            continue

        statement = parser.parse_expression()
        if parser.accept("="):
            value = parser.parse_expression()
            target = python_name(statement.text)
            expects_decimal = False
            if statement.text.startswith("kkm."):
                expects_decimal = is_decimal_type(connector_field_type(statement.text.split(".", 1)[1]))
            block = render(value, indent, expects_decimal)
            if len(block) > 1:
                lines.append("")
            lines.append(pad + f"{target} = {block[0]}")
            lines.extend(pad + extra for extra in block[1:])
            if len(block) > 1:
                lines.append("")
        else:
            block = render_statement_call(statement, indent)
            if len(block) > 1:
                lines.append("")
            lines.extend(pad + text for text in block)
            if len(block) > 1:
                lines.append("")
        parser.accept(";")

    return trim_blank_lines(lines)


def render_statement_call(node: Node, indent: int) -> list[str]:
    if node.kind != "call":
        return [python_name(node.text)]

    name = node.text
    if name.endswith(".Add"):
        name = name[: -len(".Add")] + ".append"
    elif name.endswith(".Clear"):
        name = name[: -len(".Clear")] + ".clear"
    elif name.endswith(".Remove"):
        name = name[: -len(".Remove")] + ".remove"

    if not node.args:
        return [f"{python_name(name)}()"]

    blocks = [render(argument, indent) for argument in node.args]
    if all(len(block) == 1 for block in blocks):
        single = f"{python_name(name)}({', '.join(block[0] for block in blocks)})"
        if len(single) + indent <= LINE_WIDTH:
            return [single]

    lines = [f"{python_name(name)}("]
    for block in blocks:
        lines.extend(" " * 4 + text for text in block)
        lines[-1] += ","
    lines.append(")")
    return lines


def read_statement(parser: Parser) -> list[Token]:
    """Токены одного оператора (до ; на нулевой глубине скобок)."""
    depth = 0
    collected: list[Token] = []
    while parser.position < len(parser.tokens):
        token = parser.next()
        collected.append(token)
        if token.text in "({[":
            depth += 1
        elif token.text in ")}]":
            depth -= 1
        elif token.text == ";" and depth == 0:
            break
    return collected


def trim_blank_lines(lines: list[str]) -> list[str]:
    result: list[str] = []
    for line in lines:
        if not line.strip() and (not result or not result[-1].strip()):
            continue
        result.append(line)
    while result and not result[-1].strip():
        result.pop()
    return result


# --------------------------------------------------------------------- файл

CONST_RE = re.compile(
    r"public\s+const\s+(?P<type>string|int|bool)\s+(?P<name>\w+)\s*=\s*(?P<value>.+?);",
    re.DOTALL,
)
METHOD_RE = re.compile(r"public\s+async\s+Task<SkkmConnector>\s+(?P<name>\w+)\s*\(\s*\)")
CLASS_RE = re.compile(r"public\s+class\s+(?P<name>\w+)\s*:\s*Sample")


def snake_case(name: str) -> str:
    text = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return text.lower()


def method_body(text: str, start: int) -> str:
    brace = text.index("{", start)
    depth = 0
    for index in range(brace, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[brace + 1 : index]
    raise ValueError("не найден конец метода")


def convert_file(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    class_match = CLASS_RE.search(text)
    method_match = METHOD_RE.search(text)
    if class_match is None or method_match is None:
        raise ValueError(f"{path.name}: не найден класс примера")

    class_name = class_match.group("name")
    method_name = method_match.group("name")
    constants = [(m.group("name"), m.group("type"), m.group("value").strip()) for m in CONST_RE.finditer(text)]
    body_tokens = tokenize(method_body(text, method_match.end()))
    body_lines = convert_body(body_tokens, 8)

    doc_match = re.search(r"///\s*<summary>\s*(?P<doc>.*?)\s*///\s*</summary>", text, re.DOTALL)
    doc = ""
    if doc_match:
        doc = " ".join(line.strip().lstrip("/").strip() for line in doc_match.group("doc").splitlines()).strip()

    header: list[str] = []
    for name, kind, value in constants:
        if kind == "string":
            header.append(f"    {name} = {python_string(value)}")
        elif kind == "bool":
            header.append(f"    {name} = {'True' if value == 'true' else 'False'}")
        else:
            header.append(f"    {name} = {value}")

    source_lines = ["from __future__ import annotations", ""]
    body_text = "\n".join(body_lines)

    stdlib: list[str] = []
    if "Decimal(" in body_text:
        stdlib.append("from decimal import Decimal")
    if "date.today()" in body_text:
        stdlib.append("from datetime import date, datetime, time")
    elif "datetime." in body_text:
        stdlib.append("from datetime import datetime")
    source_lines.extend(stdlib)
    if stdlib:
        source_lines.append("")

    used = sorted(
        {
            name
            for name in re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", body_text)
            if name in PUBLIC_NAMES and name != "SkkmConnector"
        }
    )
    source_lines.append("from rbsoftskkm import SkkmConnector" + ("" if not used else ", " + ", ".join(used)))
    source_lines.append("")
    source_lines.append("from demo.examples.sample import Sample")
    source_lines.append("")
    source_lines.append("")
    source_lines.append(f"class {class_name}(Sample):")
    if doc:
        source_lines.append(f'    """{doc}"""')
        source_lines.append("")
    source_lines.extend(header)
    source_lines.append("")
    source_lines.append(f"    def {method_name}(self) -> SkkmConnector:")
    source_lines.append("        kkm = self.kkm")
    source_lines.extend(body_lines)
    source_lines.append("")

    return class_name, "\n".join(source_lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path, nargs="?", default=Path("demo/examples"))
    args = parser.parse_args()

    args.target.mkdir(parents=True, exist_ok=True)
    converted = 0
    failed: list[str] = []

    for path in sorted(args.source.rglob("*.cs")):
        if path.stem == "Sample":
            continue
        try:
            class_name, source = convert_file(path)
        except Exception as error:  # noqa: BLE001 - показываем, какой файл не разобрался
            failed.append(f"{path.name}: {error}")
            continue
        (args.target / f"{snake_case(class_name)}.py").write_text(source, encoding="utf-8")
        converted += 1

    subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--fix", "--quiet", str(args.target)],
        check=False,
        capture_output=True,
    )

    print(f"примеров: {converted}, ошибок: {len(failed)}")
    for item in failed:
        print("  " + item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
