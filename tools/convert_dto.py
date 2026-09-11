"""Конвертер C#-моделей SkkmConnector в Python-датаклассы.

Запуск: python tools/convert_dto.py <путь к репозиторию C#> [<каталог назначения>]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- разбор C#

ROOT_PACKAGE = "rbsoftskkm"

SUMMARY_OPEN = "<summary>"
SUMMARY_CLOSE = "</summary>"

RE_ENUM = re.compile(r"^\s*(?:public|internal)\s+enum\s+(?P<name>\w+)")
RE_CLASS = re.compile(
    r"^\s*(?:public|internal)\s+(?:sealed\s+|abstract\s+)?class\s+(?P<name>\w+)"
    r"(?:\s*:\s*(?P<base>\w+))?"
)
RE_PROPERTY = re.compile(
    r"^\s*public\s+(?P<type>[\w<>\[\],?.\s]+?)\s+(?P<name>\w+)\s*\{\s*get;"
    r"(?:\s*(?:init|set);)?\s*\}"
    r"(?:\s*=\s*(?P<default>.+?)\s*;)?\s*$"
)
RE_ENUM_MEMBER = re.compile(r"^\s*(?P<name>[^\W\d]\w*)\s*(?:=\s*(?P<value>-?\d+)\s*)?,?\s*$")
RE_JSON_NAME = re.compile(r'\[JsonPropertyName\("(?P<value>[^"]+)"\)\]')
RE_JSON_ORDER = re.compile(r"\[JsonPropertyOrder\((?P<value>-?\d+)\)\]")

PRIMITIVES = {
    "string": "str",
    "int": "int",
    "long": "int",
    "short": "int",
    "uint": "int",
    "ulong": "int",
    "byte": "int",
    "bool": "bool",
    "decimal": "Decimal",
    "double": "float",
    "float": "float",
    "DateTime": "datetime",
    "TimeSpan": "timedelta",
    "JsonElement": "Any",
    "object": "Any",
    "Guid": "str",
}

PY_KEYWORDS = {
    "None", "True", "False", "class", "import", "from", "lambda", "global", "def",
    "is", "in", "and", "or", "not", "pass", "del", "for", "while", "return",
}


def safe_name(name: str) -> str:
    """Имя элемента, пригодное для Python: ключевые слова получают подчёркивание."""
    return f"{name}_" if name in PY_KEYWORDS else name


@dataclass
class Member:
    name: str
    type: str
    optional: bool
    default: str
    json_name: str
    order: int
    doc: list[str]
    is_list: bool = False


@dataclass
class TypeDef:
    name: str
    kind: str  # "class" | "enum"
    base: str | None
    doc: list[str]
    members: list[Member] = field(default_factory=list)
    module: str = ""
    package: str = ""


def snake_case(name: str) -> str:
    text = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return text.lower()


def clean_doc(lines: list[str]) -> list[str]:
    """XML-комментарий C# в текст: <para> — абзац, <see cref="X"/> — просто X."""
    text = "\n".join(lines)
    text = text.replace(SUMMARY_OPEN, "").replace(SUMMARY_CLOSE, "")
    text = re.sub(r"<para>\s*", "\n", text)
    text = re.sub(r"\s*</para>", "\n", text)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r'<(?:see|seealso)\s+cref="(?:[A-Z]:)?([\w.]+)"\s*/>', lambda m: m.group(1).split(".")[-1], text)
    text = re.sub(r'<(?:see|seealso)\s+cref="(?:[A-Z]:)?([\w.]+)"\s*>(.*?)</(?:see|seealso)>', r"\2", text)
    text = re.sub(r"</?c>", "", text)
    text = re.sub(r"</?(?:remarks|value|example|code)>", "", text)
    text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")

    result: list[str] = []
    for raw in text.split("\n"):
        line = re.sub(r"[ \t]+", " ", raw).strip()
        if line or (result and result[-1]):
            result.append(line)
    while result and not result[-1]:
        result.pop()
    return result


def map_type(cs_type: str) -> tuple[str, bool, bool]:
    """C#-тип в Python-тип. Возвращает (тип, optional, список)."""
    text = cs_type.strip()
    optional = False
    if text.endswith("?"):
        optional = True
        text = text[:-1].strip()

    is_list = False
    inner = None
    if text.endswith("[]"):
        is_list = True
        inner = text[:-2].strip()
    else:
        generic = re.match(r"(List|IReadOnlyList|IList|IEnumerable|ICollection)<(.+)>$", text)
        if generic:
            is_list = True
            inner = generic.group(2).strip()

    if is_list and inner is not None:
        item, item_optional, _ = map_type(inner)
        if item_optional:
            item = f"Optional[{item}]"
        return f"list[{item}]", optional, True

    dictionary = re.match(r"(?:Dictionary|IDictionary)<([^,]+),\s*(.+)>$", text)
    if dictionary:
        key, _, _ = map_type(dictionary.group(1))
        value, _, _ = map_type(dictionary.group(2))
        return f"dict[{key}, {value}]", optional, False

    if text.endswith("?"):
        text = text[:-1]
        optional = True

    return PRIMITIVES.get(text, text), optional, False


def parse_file(path: Path) -> list[TypeDef]:
    types: list[TypeDef] = []
    doc: list[str] = []
    json_name = ""
    order = 0
    current: TypeDef | None = None
    depth_of_type: int | None = None
    entered_body = False
    depth = 0
    enum_next_value = 0

    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()

        if line.startswith("///"):
            doc.append(line[3:].strip())
            continue

        if line.startswith("["):
            match_name = RE_JSON_NAME.search(line)
            if match_name:
                json_name = match_name.group("value")
            match_order = RE_JSON_ORDER.search(line)
            if match_order:
                order = int(match_order.group("value"))
            continue

        if not line or line.startswith("//") or line.startswith("using") or line.startswith("namespace"):
            if not line:
                pass
            else:
                doc = []
            continue

        if current is None:
            enum_match = RE_ENUM.match(line)
            class_match = RE_CLASS.match(line)
            if enum_match:
                current = TypeDef(enum_match.group("name"), "enum", None, clean_doc(doc))
                enum_next_value = 0
                depth_of_type = depth
                entered_body = False
                doc = []
            elif class_match:
                current = TypeDef(
                    class_match.group("name"), "class", class_match.group("base"), clean_doc(doc)
                )
                depth_of_type = depth
                entered_body = False
                doc = []
            else:
                doc = []
        else:
            if current.kind == "class":
                prop = RE_PROPERTY.match(line)
                if prop:
                    py_type, optional, is_list = map_type(prop.group("type"))
                    current.members.append(
                        Member(
                            name=prop.group("name"),
                            type=py_type,
                            optional=optional,
                            default=(prop.group("default") or "").strip(),
                            json_name=json_name or prop.group("name"),
                            order=order,
                            doc=clean_doc(doc),
                            is_list=is_list,
                        )
                    )
                    doc = []
                    json_name = ""
                    order = 0
            else:
                member = RE_ENUM_MEMBER.match(line)
                if member and "{" not in line and "}" not in line:
                    value = member.group("value")
                    enum_next_value = int(value) if value is not None else enum_next_value
                    current.members.append(
                        Member(
                            name=safe_name(member.group("name")),
                            type="int",
                            optional=False,
                            default=str(enum_next_value),
                            json_name=member.group("name"),
                            order=0,
                            doc=clean_doc(doc),
                        )
                    )
                    enum_next_value += 1
                    doc = []

        depth += line.count("{") - line.count("}")
        if current is not None and depth_of_type is not None:
            if depth > depth_of_type:
                entered_body = True
            elif entered_body:
                types.append(current)
                current = None
                depth_of_type = None

    if current is not None:
        types.append(current)
    return types


# ------------------------------------------------------------- генерация

def default_expression(member: Member, registry: dict[str, TypeDef]) -> str:
    """Значение по умолчанию поля: как в C#, иначе None для nullable."""
    if member.is_list:
        if member.optional and not member.default:
            return "None"
        return "field(default_factory=list)"

    value = member.default
    if value == "DateTime.Today":
        return "field(default_factory=lambda: datetime.combine(date.today(), time.min))"
    if value:
        if value in {"[]", "new()"}:
            return "field(default_factory=list)" if member.is_list else f"field(default_factory={member.type})"
        if value.startswith('"'):
            return value
        if value in {"true", "false"}:
            return value.capitalize()
        if re.fullmatch(r"-?\d+(\.\d+)?m?", value):
            literal = value.rstrip("m")
            return f'Decimal("{literal}")' if member.type == "Decimal" else literal
        if "." in value:  # PictureAlignment.Center и подобные
            return value
        return value

    if member.optional:
        return "None"
    target = registry.get(member.type)
    if target is not None and target.kind == "enum":
        zero = next((m.name for m in target.members if m.default == "0"), None)
        return f"{member.type}.{zero}" if zero else f"{member.type}(0)"
    if member.type == "datetime":
        return "datetime.min"
    if member.type == "str":
        return '""'
    if member.type == "int":
        return "0"
    if member.type == "float":
        return "0.0"
    if member.type == "bool":
        return "False"
    if member.type == "Decimal":
        return 'Decimal("0")'
    return "None"


def annotation(member: Member) -> str:
    if member.optional:
        return f"Optional[{member.type}]"
    return member.type


def collect_references(type_def: TypeDef) -> set[str]:
    names: set[str] = set()
    if type_def.base:
        names.add(type_def.base)
    for member in type_def.members:
        names.update(re.findall(r"[A-Za-z_]\w*", member.type))
        if member.default and "." in member.default and not member.default.startswith('"'):
            names.add(member.default.split(".")[0])
    return names


def apply_aliases(text: str, aliases: dict[str, str]) -> str:
    """Подставляет псевдонимы импортов в аннотацию или значение по умолчанию."""
    if not aliases:
        return text
    return re.sub(r"[A-Za-z_]\w*", lambda match: aliases.get(match.group(0), match.group(0)), text)


def module_aliases(types: list[TypeDef], registry: dict[str, TypeDef]) -> dict[str, str]:
    """Псевдонимы для типов, чьё имя занято полем модуля (ShiftIncome: ShiftIncome)."""
    own = {t.name for t in types}
    member_names = {member.name for t in types if t.kind == "class" for member in t.members}
    aliases: dict[str, str] = {}
    for type_def in types:
        for name in collect_references(type_def):
            if name in member_names and name in registry and name not in own:
                aliases[name] = f"_{name}"
    return aliases


def render(type_def: TypeDef, registry: dict[str, TypeDef], aliases: dict[str, str] | None = None) -> str:
    aliases = aliases or {}
    lines: list[str] = []
    if type_def.kind == "enum":
        lines.append(f"class {type_def.name}(IntEnum):")
    elif type_def.base and type_def.base in registry:
        lines.append("@dataclass")
        lines.append(f"class {type_def.name}({type_def.base}):")
    else:
        lines.append("@dataclass")
        lines.append(f"class {type_def.name}:")

    if type_def.doc:
        if len(type_def.doc) == 1:
            lines.append(f'    """{type_def.doc[0]}"""')
        else:
            lines.append('    """' + type_def.doc[0])
            for extra in type_def.doc[1:]:
                lines.append(f"    {extra}" if extra else "")
            lines.append('    """')
        lines.append("")

    if not type_def.members:
        lines.append("    pass" if type_def.kind == "class" else "    pass")
        return "\n".join(lines)

    for member in type_def.members:
        enum_target = registry.get(member.type)
        if (
            enum_target is not None
            and enum_target.kind == "enum"
            and not member.optional
            and not member.default
            and all(item.default != "0" for item in enum_target.members)
        ):
            # В C# такое поле хранит (Enum)0 — значения с таким кодом нет, значит «не задано».
            member.optional = True

        for doc_line in member.doc:
            lines.append(f"    #: {doc_line}" if doc_line else "    #:")
        if type_def.kind == "enum":
            lines.append(f"    {member.name} = {member.default}")
        else:
            metadata: list[str] = []
            if member.json_name != member.name:
                metadata.append(f'"json": "{member.json_name}"')
            if member.order:
                metadata.append(f'"order": {member.order}')
            default = apply_aliases(default_expression(member, registry), aliases)
            if metadata:
                meta_text = "{" + ", ".join(metadata) + "}"
                if default.startswith("field("):
                    default = default[:-1] + f", metadata={meta_text})"
                else:
                    default = f"field(default={default}, metadata={meta_text})"
            lines.append(f"    {member.name}: {apply_aliases(annotation(member), aliases)} = {default}")
        lines.append("")

    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def module_header(types: list[TypeDef], registry: dict[str, TypeDef], module_package: str) -> str:
    aliases = module_aliases(types, registry)
    body = "\n".join(render(t, registry, aliases) for t in types)
    annotations_text = "\n".join(
        f"{annotation(member)} = {default_expression(member, registry)}"
        for type_def in types
        if type_def.kind == "class"
        for member in type_def.members
    )

    dataclass_names: set[str] = set()
    if any(t.kind == "class" for t in types):
        dataclass_names.add("dataclass")
    if "field(" in body:
        dataclass_names.add("field")

    datetime_names: set[str] = set()
    if re.search(r"\bdatetime\b", annotations_text):
        datetime_names.add("datetime")
    if "date.today()" in annotations_text:
        datetime_names.update({"date", "time"})
    if re.search(r"\btimedelta\b", annotations_text):
        datetime_names.add("timedelta")

    typing_names: set[str] = set()
    if "Optional[" in body:
        typing_names.add("Optional")
    if re.search(r"\bAny\b", body):
        typing_names.add("Any")

    imports: list[str] = ["from __future__ import annotations", ""]
    if dataclass_names:
        imports.append("from dataclasses import " + ", ".join(sorted(dataclass_names)))
    if datetime_names:
        imports.append("from datetime import " + ", ".join(sorted(datetime_names)))
    if re.search(r"\bDecimal\b", annotations_text):
        imports.append("from decimal import Decimal")
    if any(t.kind == "enum" for t in types):
        imports.append("from enum import IntEnum")
    if typing_names:
        imports.append("from typing import " + ", ".join(sorted(typing_names)))

    own = {t.name for t in types}
    external: dict[str, set[str]] = {}
    for type_def in types:
        for name in collect_references(type_def):
            if name in own or name not in registry:
                continue
            target = registry[name]
            module_path = f"{target.package}.{target.module}" if target.package else target.module
            external.setdefault(module_path, set()).add(name)

    package_imports: list[str] = []
    for module_path in sorted(external):
        names = ", ".join(
            f"{name} as {aliases[name]}" if name in aliases else name for name in sorted(external[module_path])
        )
        package_imports.append(f"from {ROOT_PACKAGE}.{module_path} import {names}")

    header = "\n".join(imports)
    if package_imports:
        header += "\n\n" + "\n".join(sorted(package_imports))
    return header + "\n\n\n" + body + "\n"


# ------------------------------------------------------------------ запуск

SOURCE_MAP: list[tuple[str, str]] = [
    ("SkkmConnector/Dto/Enums", "dto/enums"),
    ("SkkmConnector/Dto/Admin", "dto/admin"),
    ("SkkmConnector/Dto/Fiscalization", "dto/fiscalization"),
    ("SkkmConnector/Dto/Marking", "dto/marking"),
    ("SkkmConnector/Dto/Operations", "dto/operations"),
    ("SkkmConnector/Dto/Positions", "dto/positions"),
    ("SkkmConnector/Dto/Queue", "dto/queue"),
    ("SkkmConnector/Dto/Results", "dto/results"),
    ("SkkmConnector/Dto/Templates", "dto/templates"),
    ("SkkmConnector/Dto", "dto"),
    ("SkkmConnector/Data/Contracts", "data/contracts"),
]



PUBLIC_PACKAGES = ("dto",)

ROOT_DOC = '''"""Коннектор Сервера ККМ: клиент REST API службы печати РБ-Софт.

Публичные имена — классы, поля и методы — совпадают с эталонной реализацией,
поэтому пишутся в PascalCase, а не по PEP 8. Обоснование — в README.
"""
'''


def write_packages(target: Path, modules: dict[str, list[TypeDef]]) -> None:
    """__init__.py каждого сгенерированного пакета: реэкспорт своих модулей."""
    by_package: dict[str, list[TypeDef]] = {}
    for module_path, types in modules.items():
        package, _, _ = module_path.rpartition(".")
        by_package.setdefault(package, []).extend(types)

    for package in sorted(by_package):
        lines = ["from __future__ import annotations", ""]
        import_lines: list[str] = []
        exports: list[str] = []
        for type_def in sorted(by_package[package], key=lambda t: t.module):
            import_lines.append(f"from {ROOT_PACKAGE}.{package}.{type_def.module} import {type_def.name}")
            exports.append(type_def.name)

        children = sorted(p for p in by_package if p.startswith(f"{package}.") and p.count(".") == package.count(".") + 1)
        for child in children:
            names = sorted(t.name for t in by_package[child])
            import_lines.append(f"from {ROOT_PACKAGE}.{child} import " + ", ".join(names))
            exports.extend(names)

        lines.extend(sorted(import_lines))
        lines.append("")
        lines.append("__all__ = [")
        for name in sorted(exports):
            lines.append(f'    "{name}",')
        lines.append("]")
        path = target / package.replace(".", "/") / "__init__.py"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_root_init(target: Path, modules: dict[str, list[TypeDef]]) -> None:
    """Корневой __init__.py: коннектор и все публичные модели."""
    public: list[TypeDef] = []
    for module_path, types in modules.items():
        if module_path.split(".")[0] in PUBLIC_PACKAGES:
            public.extend(types)

    lines = [ROOT_DOC, "from __future__ import annotations", ""]
    import_lines = [f"from {ROOT_PACKAGE}.core.skkm_connector import SkkmConnector"]
    for type_def in public:
        module_path = f"{type_def.package}.{type_def.module}"
        import_lines.append(f"from {ROOT_PACKAGE}.{module_path} import {type_def.name}")
    lines.extend(sorted(import_lines))

    lines.append("")
    lines.append("__all__ = [")
    for name in sorted([t.name for t in public] + ["SkkmConnector"]):
        lines.append(f'    "{name}",')
    lines.append("]")
    (target / "__init__.py").write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_imports(target: Path) -> None:
    """Приводит импорты сгенерированных модулей к стилю ruff, если он установлен."""
    try:
        subprocess.run(
            [sys.executable, "-m", "ruff", "check", "--fix", "--quiet", str(target)],
            check=False,
            capture_output=True,
        )
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path, nargs="?", default=Path("src/rbsoftskkm"))
    args = parser.parse_args()

    registry: dict[str, TypeDef] = {}
    modules: dict[str, list[TypeDef]] = {}

    for cs_dir, py_dir in SOURCE_MAP:
        source_dir = args.source / cs_dir
        if not source_dir.is_dir():
            print(f"нет каталога {source_dir}", file=sys.stderr)
            continue
        for cs_file in sorted(source_dir.glob("*.cs")):
            package = py_dir.replace("/", ".")
            module = snake_case(cs_file.stem)
            types = parse_file(cs_file)
            if not types:
                continue
            for type_def in types:
                type_def.module = module
                type_def.package = package
                registry[type_def.name] = type_def
            modules.setdefault(f"{package}.{module}", []).extend(types)

    for module_path, types in sorted(modules.items()):
        package, _, module = module_path.rpartition(".")
        out_dir = args.target / package.replace(".", "/")
        out_dir.mkdir(parents=True, exist_ok=True)
        text = module_header(types, registry, package)
        (out_dir / f"{module}.py").write_text(text, encoding="utf-8")

    write_packages(args.target, modules)
    write_root_init(args.target, modules)
    format_imports(args.target)

    print(f"классов и перечислений: {len(registry)}, модулей: {len(modules)}")
    for module_path, types in sorted(modules.items()):
        print(f"  {module_path}: {', '.join(t.name for t in types)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
