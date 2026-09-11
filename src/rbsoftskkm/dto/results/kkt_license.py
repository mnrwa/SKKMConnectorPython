from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class KktLicense:
    """Лицензия ККТ"""

    #: Номер лицензии.
    Number: int = 0

    #: Наименование лицензии.
    Name: Optional[str] = None

    #: Действует с.
    ValidFrom: datetime = datetime.min

    #: Действует до.
    ValidUntil: datetime = datetime.min

    #: Версия узла
    UnitVersion: Optional[str] = None

    #: Описание лицензии.
    Description: Optional[str] = None

    #: Признак активной лицензии.
    IsActive: bool = False
