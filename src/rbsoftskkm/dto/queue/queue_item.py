from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class QueueItem:
    """Элемент очереди печати."""

    #: Идентификатор документа задания.
    DocId: str = ""

    #: Название устройства, которому адресовано задание.
    DeviceName: str = ""

    #: Идентификатор пула (если задание адресовано пулу, а не конкретному устройству).
    PoolId: str = ""

    #: Признак отправки задания на устройство.
    SentToPrint: bool = False

    #: Время постановки задания в очередь.
    Time: datetime = datetime.min

    #: Время успешной печати.
    PrintedTime: datetime = datetime.min

    #: Признак успешной печати задания.
    Printed: bool = False

    #: Сумма документа.
    Sum: Decimal = Decimal("0")

    #: Описание текущего состояния или ошибки задания.
    ErrorDescription: str = ""

    #: Номер кассовой смены.
    Session: int = 0

    #: Номер документа (заполняется после успешной обработки).
    DocNumber: int = 0
