from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class OperationListItem:
    """Краткая информация об операции в списке."""

    #: Идентификатор документа.
    DocId: str = ""

    #: Идентификатор документа-основания.
    BaseDocId: str = ""

    #: Идентификатор запроса.
    RequestId: str = ""

    #: Идентификатор терминала.
    TerminalId: str = ""

    #: Имя устройства.
    DeviceName: str = ""

    #: Идентификатор пула.
    PoolId: str = ""

    #: Дата операции.
    Date: datetime = datetime.min

    #: Дата создания записи.
    CreatedAt: datetime = datetime.min

    #: Дата последнего обновления.
    UpdateAt: datetime = datetime.min

    #: Тип задания.
    TaskType: int = 0

    #: Наименование типа задания.
    TaskName: str = ""

    #: Сумма операции.
    Sum: Decimal = Decimal("0")

    #: Номер смены.
    SessionNumber: int = 0

    #: Номер документа в смене.
    DocNumberInShift: int = 0

    #: Номер фискального документа.
    DocNumber: int = 0

    #: Дата документа по ФН.
    FnDate: datetime = datetime.min

    #: Фискальный признак документа.
    FiscalSign: str = ""

    #: Номер фискального накопителя.
    Fn: str = ""

    #: Контакт покупателя.
    ClientContact: str = ""

    #: Имя кассира.
    CashierName: str = ""

    #: Регистрационный номер ККТ.
    RnKKT: str = ""

    #: Заводской номер ККТ.
    ZnKKT: str = ""

    #: Код результата (0 — успех).
    ResultCode: int = 0

    #: Описание результата.
    ResultDescription: str = ""

    #: Признак успешной обработки операции.
    Processed: bool = False
