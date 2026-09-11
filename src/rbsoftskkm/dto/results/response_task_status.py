from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from rbsoftskkm.dto.results.document_header import DocumentHeader as _DocumentHeader


@dataclass
class ResponseTaskStatus:
    """Статус задания"""

    #: Имя устройства.
    DeviceName: Optional[str] = None

    #: Идентификатор документа.
    DocId: Optional[str] = None

    #: Дата и время постановки задания в обработку.
    Date: datetime = datetime.min

    #: Статус отправки: 0 — задача новая, в очереди; 1 — отправлена на выполнение; 2 — удачно обработана; −1 — вернулась с ошибкой.
    SentToPrint: int = 0

    #: Позиция задания в очереди на момент запроса. −1 — задание уже покинуло очередь.
    NumberInQueue: int = 0

    #: Размер очереди.
    QueueSize: int = 0

    #: Идентификатор пула. Если устройство не входит в пул — не заполняется.
    PoolId: Optional[str] = None

    #: Номер смены.
    ShiftNumber: int = 0

    #: Номер чека.
    DocNumber: int = 0

    #: Тип чека
    TaskType: int = 0

    #: Фискальный признак документа. Заполняется только для фискальных документов.
    FiscalSign: Optional[str] = None

    #: Заголовок документа.
    DocumentHeader: Optional[_DocumentHeader] = None

    #: Код результата обработки задания.
    ResultCode: int = 0

    #: Описание результата обработки задания.
    ResultDescription: Optional[str] = None
