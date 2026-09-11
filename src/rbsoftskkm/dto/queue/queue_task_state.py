from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from rbsoftskkm.dto.queue.document_history_item import DocumentHistoryItem


@dataclass
class QueueTaskState:
    """Состояние задания в очереди."""

    #: Название устройства.
    DeviceName: str = ""

    #: Идентификатор документа.
    DocId: str = ""

    #: Код состояния документа.
    DocState: int = 0

    #: Код состояния очереди.
    QueueState: int = 0

    #: Код результата.
    ResultCode: int = 0

    #: Описание результата.
    ResultDescription: str = ""

    #: Позиция задания в очереди на момент запроса.
    NumberInQueue: int = 0

    #: Дата и время последнего изменения статуса.
    Date: datetime = datetime.min

    #: Фискальный признак документа (для успешно обработанных фискальных заданий).
    FiscalSign: str = ""

    #: Описание текущего этапа обработки задания.
    PrintStatusDescription: str = ""

    #: История обработки задания.
    History: list[DocumentHistoryItem] = field(default_factory=list)
