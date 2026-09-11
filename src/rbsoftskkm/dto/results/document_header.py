from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class DocumentHeader:
    """Заголовок фискального документа"""

    #: Название организации.
    OrganizationInfo: Optional[str] = None

    #: Заводской номер ККТ.
    SerialNumber: Optional[str] = None

    #: ИНН организации.
    Vatin: Optional[str] = None

    #: Кассир.
    Cashier: Optional[str] = None

    #: Регистрационный номер ККТ.
    RnNumber: Optional[str] = None

    #: Фискальный накопитель.
    Fn: Optional[str] = None

    #: Адрес сайта уполномоченного органа (ФНС) в сети «Интернет».
    FnsUrl: Optional[str] = None

    #: Номер смены.
    ShiftNumber: int = 0

    #: Номер фискального документа.
    DocNumber: int = 0

    #: Фискальный признак документа.
    FiscalSign: Optional[str] = None

    #: Наименование провайдера ОФД.
    OfdOrganizationName: Optional[str] = None

    #: ИНН провайдера ОФД.
    OfdVatin: Optional[str] = None
