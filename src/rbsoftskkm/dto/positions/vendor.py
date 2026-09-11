from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Vendor:
    """Данные поставщика:

    Name - Наименование поставщика

    Phones - Телефон(ы) поставщика

    Vatin - ИНН поставщика
    """

    #: Наименование поставщика.
    Name: Optional[str] = None

    #: Телефоны поставщика.
    Phones: Optional[list[str]] = None

    #: ИНН поставщика.
    Vatin: Optional[str] = None
