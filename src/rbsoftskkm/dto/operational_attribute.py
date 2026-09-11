from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class OperationalAttribute:
    """Операционный реквизит чека:

    DateTime - Дата и время операции

    OperationId - Идентификатор операции

    OperationData - Данные операции
    """

    #: Дата, время операции.
    DateTime: Optional[str] = None

    #: Идентификатор операции.
    OperationId: Optional[int] = None

    #: Данные операции.
    OperationData: Optional[str] = None
