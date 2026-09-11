from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Industry:
    """Отраслевой реквизит предмета расчёта:

    IdentifierFoiv - Идентификатор ФОИВ

    DocumentDate - Дата документа-основания

    DocumentNumber - Номер документа-основания

    AttributeValue - Значение отраслевого реквизита
    """

    #: Идентификатор ФОИВ.
    IdentifierFoiv: Optional[str] = None

    #: Дата документа основания.
    DocumentDate: Optional[str] = None

    #: Номер документа основания.
    DocumentNumber: Optional[str] = None

    #: Значение отраслевого реквизита.
    AttributeValue: Optional[str] = None
