from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from rbsoftskkm.dto.results.check_document import CheckDocument


@dataclass
class OperationHistoryItem:
    """Элемент истории обработки операции."""

    #: Время события.
    Time: datetime = datetime.min

    #: Код состояния.
    State: int = 0

    #: Описание события.
    Description: str = ""

    #: Состояние документа на этом шаге.
    Document: Optional[CheckDocument] = None
