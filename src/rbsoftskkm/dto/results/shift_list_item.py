from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ShiftListItem:
    """Элемент списка отчётов"""

    #: Результат обработки.
    ResultCode: int = 0

    #: Описание результата.
    ResultDescription: Optional[str] = None

    #: Дата создания документа.
    Date: datetime = datetime.min

    #: Идентификатор документа.
    DocId: Optional[str] = None

    #: Номер сессии (смены).
    ShiftNumber: int = 0

    #: Имя устройства.
    DeviceName: Optional[str] = None

    #: Идентификатор терминала, с которого пришёл документ.
    TerminalId: Optional[str] = None
