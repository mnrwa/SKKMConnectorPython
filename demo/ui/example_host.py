"""Поиск примеров, дерево коллекции и запуск запроса."""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Optional

import demo.examples as examples_package
from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector

if TYPE_CHECKING:
    from demo.connection_settings import ConnectionSettings

ROOT_ORDER = [
    "Авторизация",
    "Служебные",
    "Администрирование",
    "Работа с ККМ",
]

KNOWN_ORDER = {
    "ККТ": 0,
    "Служба": 1,
    "Кассовые смены": 0,
    "Отчеты": 1,
    "Печать чеков": 2,
    "Примеры чеков": 0,
    "Корректировочные чеки": 3,
    "Корректировки ФФД 1.0.5": 0,
    "Корректировки ФФД 1.2": 1,
    "Денежный ящик": 4,
    "Нефискальные чеки": 5,
    "Рекламные чеки": 0,
    "Работа с картинками": 1,
    "Очередь": 6,
    "Работа с маркировкой": 7,
    "Фискализация": 8,
    "Шаблоны чека": 9,
    "Операции": 10,
}

OTHER_GROUP = "Прочее"
LAST = 1_000_000


@dataclass
class ExampleItem:
    """Один запрос коллекции: где показать, что вызвать."""

    GroupPath: list[str]
    Title: str
    NeedDocumentId: bool
    SortOrder: int
    Instance: Sample
    MethodName: str

    @property
    def HttpMethod(self) -> str:
        """Метод HTTP по префиксу имени: Get…, Put…, Delete…, остальное POST."""
        if self.MethodName.startswith("Get"):
            return "GET"
        if self.MethodName.startswith("Delete"):
            return "DELETE"
        if self.MethodName.startswith("Put"):
            return "PUT"
        return "POST"

    @property
    def Method(self) -> Callable[[], SkkmConnector]:
        method: Callable[[], SkkmConnector] = getattr(self.Instance, self.MethodName)
        return method


@dataclass
class ExampleTreeNode:
    Title: str = ""
    Item: Optional[ExampleItem] = None
    Children: list["ExampleTreeNode"] = field(default_factory=list)


def discover() -> list[ExampleItem]:
    """Примеры находятся сканированием пакета: регистрировать вручную не нужно."""
    items: list[ExampleItem] = []
    for module_info in pkgutil.walk_packages(examples_package.__path__, examples_package.__name__ + "."):
        module = importlib.import_module(module_info.name)
        for _, member in inspect.getmembers(module, inspect.isclass):
            if not issubclass(member, Sample) or member is Sample or member.__module__ != module.__name__:
                continue
            items.append(from_class(member))
    items.sort(key=lambda item: ("/".join(item.GroupPath), item.Title))
    return items


def from_class(target: type[Sample]) -> ExampleItem:
    method_name = next(
        name
        for name, value in vars(target).items()
        if callable(value) and not name.startswith("_")
    )
    group_path = [part.strip() for part in str(target.GroupPath).split("|") if part.strip()]
    return ExampleItem(
        GroupPath=group_path or [OTHER_GROUP],
        Title=target.Title or target.__name__,
        NeedDocumentId=bool(target.NeedDocumentId),
        SortOrder=int(target.SortOrder),
        Instance=target(),
        MethodName=method_name,
    )


def build_tree() -> list[ExampleTreeNode]:
    roots: dict[str, ExampleTreeNode] = {}
    for item in discover():
        node = get_or_create_root(roots, item.GroupPath[0])
        for title in item.GroupPath[1:]:
            node = get_or_create_child(node, title)
        node.Children.append(ExampleTreeNode(Title=item.Title, Item=item))

    ordered = sorted(roots.values(), key=lambda node: root_index(node.Title))
    return [sort_node(node) for node in ordered]


def get_or_create_root(roots: dict[str, ExampleTreeNode], title: str) -> ExampleTreeNode:
    node = roots.get(title)
    if node is None:
        node = ExampleTreeNode(Title=title)
        roots[title] = node
    return node


def get_or_create_child(parent: ExampleTreeNode, title: str) -> ExampleTreeNode:
    for child in parent.Children:
        if child.Item is None and child.Title == title:
            return child
    node = ExampleTreeNode(Title=title)
    parent.Children.append(node)
    return node


def sort_node(node: ExampleTreeNode) -> ExampleTreeNode:
    node.Children.sort(key=child_key)
    for child in node.Children:
        if child.Item is None:
            sort_node(child)
    return node


def child_key(node: ExampleTreeNode) -> tuple[int, int, str]:
    if node.Item is None:
        return (0, KNOWN_ORDER.get(node.Title, LAST), node.Title)
    return (1, node.Item.SortOrder, node.Title)


def root_index(title: str) -> int:
    return ROOT_ORDER.index(title) if title in ROOT_ORDER else LAST


class ExampleRunner:
    """Общая сессия коннектора для всех примеров."""

    Session = SkkmConnector()

    @staticmethod
    def apply_connection(sample: Sample, connection: "ConnectionSettings") -> None:
        session = ExampleRunner.Session
        session.Host = connection.Host.strip()
        session.Port = connection.Port
        session.Token = connection.Token.strip()
        sample.kkm = session
        sample.deviceName = connection.Device.strip()
        sample.cashierName = connection.Cashier.strip()
        sample.cashierVatin = connection.CashierVatin.strip()
        sample.documentId = connection.DocumentId.strip()
        sample.fromDate = connection.From
        sample.toDate = connection.To
        session.ShiftsFrom = connection.From
        session.ShiftsTo = connection.To

    @staticmethod
    def invoke(example: ExampleItem) -> SkkmConnector:
        return example.Method()
