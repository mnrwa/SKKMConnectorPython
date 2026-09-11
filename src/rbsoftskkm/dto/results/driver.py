from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Driver:
    """Описание драйвера ККМ"""

    #: Тип драйвера.
    Type: Optional[str] = None

    #: Версия драйвера
    Version: Optional[str] = None

    #: Данные поставщика.
    Vendor: Optional[str] = None
