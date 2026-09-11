"""Входные свойства запроса: чек, коррекция, наличные, слип, картинки, маркировка."""

from __future__ import annotations

from datetime import date, datetime, time, timedelta
from decimal import Decimal
from typing import Optional

from rbsoftskkm.core.skkm_connector_connection import SkkmConnectorConnection
from rbsoftskkm.dto.correction105_taxes import Correction105Taxes
from rbsoftskkm.dto.correction_data import CorrectionData
from rbsoftskkm.dto.customer import Customer
from rbsoftskkm.dto.electronic_payment import ElectronicPayment
from rbsoftskkm.dto.enums.agent_type import AgentType
from rbsoftskkm.dto.enums.check_time_zone import CheckTimeZone
from rbsoftskkm.dto.enums.check_type import CheckType
from rbsoftskkm.dto.enums.km_confirmation_type import KmConfirmationType
from rbsoftskkm.dto.enums.marking_planned_status import MarkingPlannedStatus
from rbsoftskkm.dto.enums.measure_of_quantity import MeasureOfQuantity
from rbsoftskkm.dto.enums.picture_alignment import PictureAlignment
from rbsoftskkm.dto.enums.shift_state import ShiftState
from rbsoftskkm.dto.enums.tax_system import TaxSystem
from rbsoftskkm.dto.operational_attribute import OperationalAttribute
from rbsoftskkm.dto.payments import Payments
from rbsoftskkm.dto.positions.agent import Agent
from rbsoftskkm.dto.positions.industry import Industry
from rbsoftskkm.dto.positions.position import Position
from rbsoftskkm.dto.positions.vendor import Vendor
from rbsoftskkm.dto.results.warnings import Warnings
from rbsoftskkm.dto.user_attribute import UserAttribute


def today() -> datetime:
    """Начало текущих суток — аналог DateTime.Today."""
    return datetime.combine(date.today(), time.min)


class SkkmConnectorCheckInput(SkkmConnectorConnection):
    """Данные документа, которые уходят в тело запроса."""

    # Документы / смены

    #: Идентификатор документа (docId).
    DocumentId: str

    #: Фискальный признак документа.
    FiscalSign: str

    #: Номер смены.
    ShiftNumber: int

    #: Номер фискального документа (ФД).
    CheckNumber: int

    #: Номер чека за смену.
    CheckNumberInShift: int

    #: Регистрационный номер ККТ (РНМ).
    RnNumber: str

    #: Адрес сайта ФНС.
    FnsUrl: str

    #: Время на сервере ККМ.
    ServerDateTime: str

    #: Дата и время документа по часам ФН.
    FiscalDateTime: str

    #: Время ККТ.
    DeviceDateTime: str

    #: Состояние смены. Используйте enum ShiftState.
    CurrentShiftState: Optional[ShiftState]

    #: Количество непереданных в ОФД документов.
    BacklogDocumentsCount: int

    #: Номер первого непереданного документа.
    BacklogFirstDocumentNumber: int

    #: Дата и время первого непереданного документа.
    BacklogFirstDocumentDateTime: Optional[datetime]

    #: Срок действия ФН.
    FnValidityDate: str

    #: Остаток ресурса ФН в днях.
    FnDaysResources: int

    #: ФН присутствует.
    IsFnPresent: bool

    #: Фискальный режим.
    IsFiscal: bool

    #: Предупреждения ФН из ответа.
    FnWarnings: Optional[Warnings]

    #: Начало периода отбора отчётов, чеков и операций.
    ShiftsFrom: datetime

    #: Конец периода отбора отчётов, чеков и операций.
    ShiftsTo: datetime

    # Наличные

    #: Сумма внесения или выемки.
    CashAmount: Decimal

    # Картинки

    #: Название изображения.
    PictureName: str

    #: Изображение, закодированное в Base64.
    PictureBase64: str

    #: Выравнивание изображения при печати. Используйте enum PictureAlignment.
    PictureAlignment: PictureAlignment

    # Слип

    #: Текст нефискального документа.
    TextForPrint: str

    # Чек

    #: Тип чека / задания. Используйте enum CheckType.
    PaymentType: CheckType

    #: Только обработанные операции. Параметр isProcessed в GetOperationLast.
    IsProcessed: bool

    #: Система налогообложения. Используйте enum TaxSystem.
    TaxVariant: TaxSystem

    #: Часовая зона. Используйте enum CheckTimeZone.
    TimeZone: Optional[CheckTimeZone]

    #: Чек только в электронном виде (без печати на бумаге).
    #: True — не печатать; для обычной печати оставляйте False.
    Electronically: bool

    #: Текст для печати перед товарной частью.
    TextBefore: str

    #: Текст для печати после товарной части чека.
    TextAfter: str

    #: Место проведения расчётов.
    SaleLocation: str

    #: Адрес проведения расчётов.
    SaleAddress: str

    #: Адрес электронной почты отправителя чека.
    SenderEmail: str

    #: Признак применения ККТ при осуществлении расчета в безналичном порядке в сети «Интернет».
    OperationOnline: bool

    #: Дополнительный реквизит чека (БСО), тег 1192.
    AdditionalAttribute: str

    #: Отраслевой реквизит чека. Создайте объект Industry
    #: (IdentifierFoiv, DocumentDate, DocumentNumber, AttributeValue).
    IndustryAttribute: Optional[Industry]

    #: Дополнительный реквизит пользователя. Создайте объект UserAttribute (Name, Value).
    UserAttribute: Optional[UserAttribute]

    #: Операционный реквизит чека. Создайте объект OperationalAttribute
    #: (DateTime, OperationId, OperationData).
    OperationalAttribute: Optional[OperationalAttribute]

    #: Детализация безналичных оплат. Добавляйте объекты ElectronicPayment
    #: (Amount, PaymentMethod, Identifiers, AdditionalInformation).
    ElectronicPayments: list[ElectronicPayment]

    #: Признак агента. Используйте enum AgentType.
    AgentSign: Optional[AgentType]

    #: Данные агента. Создайте объект Agent и заполните нужные поля.
    Agent: Optional[Agent]

    #: Данные поставщика. Создайте объект Vendor (Name, Phones, Vatin).
    Vendor: Optional[Vendor]

    #: Сведения о покупателе. Создайте объект Customer и заполните нужные поля.
    Customer: Optional[Customer]

    #: Суммы оплаты. Создайте объект Payments
    #: (Cash, ElectronicPayment, AdvancePayment, Credit, CashProvision).
    Payments: Payments

    #: Позиции чека. Добавляйте наследники Position:
    #: FiscalLine, TextLine, BarcodeLine, PictureLine, SeparatorLine.
    Positions: list[Position]

    # Коррекция

    #: Данные коррекции. Создайте объект CorrectionData (Type, Description, Date, Number).
    CorrectionData: Optional[CorrectionData]

    #: Суммы НДС по ставкам для чека коррекции ФФД 1.05.
    #: Создайте объект Correction105Taxes и заполните нужные ставки.
    Correction105Taxes: Optional[Correction105Taxes]

    # Маркировка (вход)

    #: Код маркировки в кодировке Base64.
    MarkingCode: str

    #: Планируемый статус товара. Используйте enum MarkingPlannedStatus.
    PlannedStatus: MarkingPlannedStatus

    #: Количество товара.
    MarkingQuantity: Decimal

    #: Мера количества предмета расчёта. Используйте enum MeasureOfQuantity.
    MeasureOfQuantity: MeasureOfQuantity

    #: Числитель дробного количества товара.
    FractionalQuantityNumerator: int

    #: Знаменатель дробного количества товара.
    FractionalQuantityDenominator: int

    #: Не отправлять результат проверки на сервер ОИСМ.
    NotSendToServer: bool

    #: Признак ожидания ответа ОИСМ.
    WaitForResult: bool

    #: Уникальный код запроса КМ.
    RequestKmGuid: str

    #: Признак подтверждения кода маркировки. Используйте enum KmConfirmationType.
    ConfirmationType: KmConfirmationType

    def __init__(self) -> None:
        super().__init__()
        self.DocumentId = ""
        self.FiscalSign = ""
        self.ShiftNumber = 0
        self.CheckNumber = 0
        self.CheckNumberInShift = 0
        self.RnNumber = ""
        self.FnsUrl = ""
        self.ServerDateTime = ""
        self.FiscalDateTime = ""
        self.DeviceDateTime = ""
        self.CurrentShiftState = None
        self.BacklogDocumentsCount = 0
        self.BacklogFirstDocumentNumber = 0
        self.BacklogFirstDocumentDateTime = None
        self.FnValidityDate = ""
        self.FnDaysResources = 0
        self.IsFnPresent = False
        self.IsFiscal = False
        self.FnWarnings = None
        self.ShiftsFrom = today() - timedelta(days=7)
        self.ShiftsTo = today()
        self.CashAmount = Decimal("0")
        self.PictureName = ""
        self.PictureBase64 = ""
        self.PictureAlignment = PictureAlignment.Center
        self.TextForPrint = ""
        self.PaymentType = CheckType.Sale
        self.IsProcessed = False
        self.TaxVariant = TaxSystem.ОСН
        self.TimeZone = None
        self.Electronically = False
        self.TextBefore = ""
        self.TextAfter = ""
        self.SaleLocation = ""
        self.SaleAddress = ""
        self.SenderEmail = ""
        self.OperationOnline = False
        self.AdditionalAttribute = ""
        self.IndustryAttribute = None
        self.UserAttribute = None
        self.OperationalAttribute = None
        self.ElectronicPayments = []
        self.AgentSign = None
        self.Agent = None
        self.Vendor = None
        self.Customer = None
        self.Payments = Payments()
        self.Positions = []
        self.CorrectionData = None
        self.Correction105Taxes = None
        self.MarkingCode = ""
        self.PlannedStatus = MarkingPlannedStatus.Sold
        self.MarkingQuantity = Decimal("1")
        self.MeasureOfQuantity = MeasureOfQuantity.Piece
        self.FractionalQuantityNumerator = 0
        self.FractionalQuantityDenominator = 0
        self.NotSendToServer = False
        self.WaitForResult = False
        self.RequestKmGuid = ""
        self.ConfirmationType = KmConfirmationType.Included
