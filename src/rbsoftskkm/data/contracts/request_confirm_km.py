from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class RequestConfirmKm:
    """Тело запроса подтверждения кода маркировки."""

    #: Имя кассы.
    DeviceName: Optional[str] = None

    #: Идентификатор запроса проверки кода маркировки.
    GUID: Optional[str] = None

    #: Тип подтверждения: 0 - включить в документ, 1 - не включать.
    ConfirmationType: int = 0
