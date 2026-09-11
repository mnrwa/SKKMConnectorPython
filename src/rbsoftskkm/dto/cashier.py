from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Cashier:
    """Сведения о кассире (продавце):

    Name - ФИО кассира

    Vatin - ИНН кассира (при наличии)
    """

    #: Имя кассира.
    Name: Optional[str] = None

    #: ИНН кассира.
    Vatin: Optional[str] = None
