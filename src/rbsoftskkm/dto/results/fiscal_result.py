from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.enums.shift_state import ShiftState as _ShiftState
from rbsoftskkm.dto.results.backlog import Backlog as _Backlog
from rbsoftskkm.dto.results.cash_drawer import CashDrawer as _CashDrawer
from rbsoftskkm.dto.results.fiscal_output_parameters import FiscalOutputParameters


@dataclass
class FiscalResult:
    """Фискальный блок ответа сервера"""

    #: Время операции на сервере.
    DateTime: Optional[str] = field(default=None, metadata={"json": "datetime"})

    #: Название устройства.
    DeviceName: Optional[str] = field(default=None, metadata={"json": "deviceName"})

    #: Идентификатор документа.
    DocId: Optional[str] = field(default=None, metadata={"json": "docId"})

    #: Адрес сайта уполномоченного органа (ФНС) в сети «Интернет».
    FnsUrl: Optional[str] = field(default=None, metadata={"json": "fnsUrl"})

    #: Номер фискального накопителя.
    FnNumber: Optional[str] = field(default=None, metadata={"json": "fnNumber"})

    #: Регистрационный номер ККТ.
    RnNumber: Optional[str] = field(default=None, metadata={"json": "rnNumber"})

    #: Дата и время документа по часам ФН.
    FiscalDateTime: Optional[str] = field(default=None, metadata={"json": "fiscalDatetime"})

    #: Фискальный признак документа.
    FiscalSign: Optional[str] = field(default=None, metadata={"json": "fiscalSign"})

    #: Номер смены.
    ShiftNumber: int = field(default=0, metadata={"json": "shiftNumber"})

    #: Номер фискального документа.
    FiscalNumber: int = field(default=0, metadata={"json": "fiscalNumber"})

    #: Состояние смены. Используйте enum ShiftState.
    ShiftState: Optional[_ShiftState] = None

    #: Сумма наличных в ящике
    CashSum: Optional[Decimal] = None

    #: Состояние денежного ящика.
    CashDrawer: Optional[_CashDrawer] = None

    #: Очередь непереданных в ОФД документов.
    Backlog: Optional[_Backlog] = None

    #: Дополнительные параметры вывода (статус ККТ вложенный в Result).
    OutputParameters: Optional[FiscalOutputParameters] = None
