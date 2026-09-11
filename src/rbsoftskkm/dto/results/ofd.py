from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Ofd:
    """Оператор фискальных данных (Ofd)."""

    #: Имя ОФД.
    Name: Optional[str] = None

    #: ИНН ОФД.
    Vatin: Optional[str] = None
