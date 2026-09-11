from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

from rbsoftskkm.dto.correction_data import CorrectionData as _CorrectionData
from rbsoftskkm.dto.results.check_customer import CheckCustomer
from rbsoftskkm.dto.results.check_item import CheckItem
from rbsoftskkm.dto.results.check_payments import CheckPayments
from rbsoftskkm.dto.results.device import Device
from rbsoftskkm.dto.results.document_header import DocumentHeader as _DocumentHeader
from rbsoftskkm.dto.results.qr_check_data import QrCheckData
from rbsoftskkm.dto.results.res_shift_total import ResShiftTotal


@dataclass
class CheckDocument:
    """Сохранённый документ с сервера"""

    #: Позиции чека.
    CheckItems: Optional[list[CheckItem]] = None

    #: Подтверждён в ФН.
    TrustedInFn: bool = False

    #: Фискальный документ.
    IsFiscal: bool = False

    #: Сдача.
    Change: Decimal = Decimal("0")

    #: Сумма с учётом скидки.
    Sum: Decimal = Decimal("0")

    #: Признак применения ККТ при осуществлении расчёта в безналичном порядке в сети «Интернет».
    OperationOnline: bool = False

    #: Номер телефона или электронная почта клиента.
    ClientContact: Optional[str] = None

    #: Сведения о покупателе (клиенте).
    CustomerDetail: Optional[CheckCustomer] = None

    #: Данные для отображения QR-кода чека.
    QrData: Optional[QrCheckData] = None

    #: Оплаты.
    Payments: Optional[CheckPayments] = None

    #: Заголовок документа.
    DocumentHeader: Optional[_DocumentHeader] = None

    #: Регистрация чека без печати на ленте.
    Electronically: bool = False

    #: Код налогообложения (СНО): 0 — ОСН, 1 — УСН, 2 — УСНД_Р, 3 — ЕНВД, 4 — ЕСН, 5 — ПСН.
    TaxType: int = 0

    #: Часовая зона: 0 — авто; 1 — МСК-1 / UTC+2; … 11 — МСК+9 / UTC+12.
    TimeZone: int = 0

    #: Данные коррекции (чеки коррекции 1.2 и 1.05).
    CorrectionData: Optional[_CorrectionData] = None

    #: Дополнительный реквизит чека (тег 1192).
    AdditionalAttribute: Optional[str] = None

    #: Номер сессии. Используется для GET check/list.
    ShiftNumber: int = 0

    #: Номер фискального документа.
    DocNumber: int = 0

    #: Номер фискального документа за смену.
    DocNumberInShift: int = 0

    #: Фискальный признак документа.
    FiscalSign: Optional[str] = None

    #: Серийный номер фискального накопителя.
    Fn: Optional[str] = None

    #: Время регистрации операции по часам ККМ.
    FiscalDate: datetime = datetime.min

    #: Имя кассира.
    CashierName: Optional[str] = None

    #: ИНН кассира.
    CashierVatin: Optional[str] = None

    #: Адрес проведения расчётов.
    SaleAddress: Optional[str] = None

    #: Место проведения расчётов.
    SaleLocation: Optional[str] = None

    #: Версия ФФД.
    FfdVersion: Optional[str] = None

    #: Структура значений тегов документа.
    Tlv: Optional[str] = None

    #: Тип чека
    TaskType: int = 0

    #: Идентификатор документа.
    DocId: Optional[str] = None

    #: Дата создания документа.
    Date: datetime = datetime.min

    #: Идентификатор терминала, с которого пришёл документ.
    TerminalId: Optional[str] = None

    #: Имя устройства.
    DeviceName: Optional[str] = None

    #: Пул, который назначен чеку.
    PoolId: Optional[str] = None

    #: Результат обработки.
    ResultCode: int = 0

    #: Описание результата.
    ResultDescription: Optional[str] = None

    #: Признак удачного завершения обработки.
    Processed: bool = False

    #: Версия сервера ККМ.
    ServerVersion: Optional[str] = None

    #: Сведения о ККТ на момент документа.
    DeviceInfo: Optional[Device] = None

    #: Сменные итоги (X/Z-отчёт).
    ShiftTotal: Optional[ResShiftTotal] = None

    #: Количество аннулирований (X/Z-отчёт).
    AnullatesCount: int = 0

    #: Сумма НДС 0% (коррекция 1.05).
    TaxSum0: Decimal = Decimal("0")

    #: Сумма НДС 5% (коррекция 1.05).
    TaxSum5: Decimal = Decimal("0")

    #: Сумма НДС 7% (коррекция 1.05).
    TaxSum7: Decimal = Decimal("0")

    #: Сумма НДС 10% (коррекция 1.05).
    TaxSum10: Decimal = Decimal("0")

    #: Сумма НДС 18% (коррекция 1.05).
    TaxSum18: Decimal = Decimal("0")

    #: Сумма НДС 20% (коррекция 1.05).
    TaxSum20: Decimal = Decimal("0")

    #: Сумма НДС 22% (коррекция 1.05).
    TaxSum22: Decimal = Decimal("0")

    #: Сумма без НДС (коррекция 1.05).
    TaxSumNone: Decimal = Decimal("0")

    #: Сумма НДС 5/105 (коррекция 1.05).
    TaxSum105: Decimal = Decimal("0")

    #: Сумма НДС 7/107 (коррекция 1.05).
    TaxSum107: Decimal = Decimal("0")

    #: Сумма НДС 10/110 (коррекция 1.05).
    TaxSum110: Decimal = Decimal("0")

    #: Сумма НДС 18/118 (коррекция 1.05).
    TaxSum118: Decimal = Decimal("0")

    #: Сумма НДС 20/120 (коррекция 1.05).
    TaxSum120: Decimal = Decimal("0")

    #: Сумма НДС 22/122 (коррекция 1.05).
    TaxSum122: Decimal = Decimal("0")
