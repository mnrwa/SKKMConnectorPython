from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DocumentHistoryItem:
    """Запись истории обработки документа в очереди."""

    #: Время события.
    Time: datetime = datetime.min

    #: Код состояния.
    State: int = 0

    #: Описание события.
    Description: str = ""

    #: Дополнительная информация о событии.
    Info: str = ""
