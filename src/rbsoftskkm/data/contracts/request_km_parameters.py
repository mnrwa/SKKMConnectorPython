from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from rbsoftskkm.data.contracts.request_km import RequestKm


@dataclass
class RequestKmParameters:
    """Тело запроса проверки кода маркировки."""

    #: Имя кассы.
    DeviceName: Optional[str] = None

    #: Параметры проверяемого кода маркировки.
    RequestKM: RequestKm = field(default_factory=RequestKm)
