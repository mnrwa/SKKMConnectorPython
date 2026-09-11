"""Базовый класс примера: параметры подключения из левой панели."""

from __future__ import annotations

from datetime import date, datetime, time, timedelta

from rbsoftskkm import SkkmConnector


class Sample:
    """Environment запроса (как переменные Bruno слева).

    Хост, порт и токен подставляются в сессию; касса и кассир — в тело запроса
    в коде примера.
    """

    #: Путь в дереве коллекции: разделы через «|».
    GroupPath = "Прочее"

    #: Заголовок запроса в дереве.
    Title = ""

    #: Порядок внутри группы. Меньше — выше.
    SortOrder = 1_000_000

    #: Примеру нужен Id документа из панели подключения.
    NeedDocumentId = False

    #: Сессия коннектора. Подставляется перед запуском примера.
    kkm: SkkmConnector

    def __init__(self) -> None:
        #: Имя ККМ, {{SKKMDEVICE}}.
        self.deviceName = ""

        #: Имя кассира из панели подключения.
        self.cashierName = ""

        #: ИНН кассира из панели подключения.
        self.cashierVatin = ""

        #: Id документа (DocId). Тот же идентификатор в очереди называется taskId.
        self.documentId = ""

        #: Начало периода (from) из панели подключения.
        self.fromDate: datetime = datetime.combine(date.today(), time.min) - timedelta(days=7)

        #: Конец периода (to) из панели подключения.
        self.toDate: datetime = datetime.combine(date.today(), time.min)
