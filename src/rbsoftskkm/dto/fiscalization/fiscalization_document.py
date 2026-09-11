from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.fiscalization_operation_type import FiscalizationOperationType


@dataclass
class FiscalizationDocument:
    """Результат фискализации."""

    #: Тип выполненной операции.
    OperationType: Optional[FiscalizationOperationType] = None

    #: Регистрационный номер ККТ.
    RnNumber: str = ""

    #: Коды систем налогообложения.
    TaxationSystems: str = ""

    #: ИНН организации.
    Vatin: str = ""

    #: Название организации.
    CompanyName: str = ""

    #: Версия ФФД ККТ.
    FfdVersionKkt: str = ""

    #: Версия ФФД ФН.
    FfdVersionFn: str = ""

    #: Признак фискального режима.
    IsFiscal: bool = False

    #: Идентификатор документа фискализации.
    DocId: str = ""

    #: Название устройства.
    DeviceName: str = ""

    #: Номер смены.
    ShiftNumber: int = 0

    #: Номер фискального документа.
    DocNumber: int = 0

    #: Фискальный признак документа.
    FiscalSign: str = ""
