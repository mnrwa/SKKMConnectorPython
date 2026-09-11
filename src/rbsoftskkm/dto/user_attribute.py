from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class UserAttribute:
    """Дополнительный реквизит пользователя чека:

    Name - Имя реквизита

    Value - Значение реквизита
    """

    #: Имя реквизита.
    Name: Optional[str] = None

    #: Значение реквизита.
    Value: Optional[str] = None
