"""Результаты последнего вызова: коды, разобранные модели, списки."""

from __future__ import annotations

from decimal import Decimal
from typing import Any, Optional

from rbsoftskkm.core.skkm_connector_base import SkkmConnectorBase
from rbsoftskkm.dto.admin.service_settings import ServiceSettings
from rbsoftskkm.dto.admin.service_user import ServiceUser
from rbsoftskkm.dto.admin.user_token import UserToken
from rbsoftskkm.dto.fiscalization.fiscalization_document import FiscalizationDocument as _FiscalizationDocument
from rbsoftskkm.dto.marking.marking_verify_result import MarkingVerifyResult
from rbsoftskkm.dto.operations.device_task_info import DeviceTaskInfo
from rbsoftskkm.dto.operations.operation_history_item import OperationHistoryItem
from rbsoftskkm.dto.operations.operation_km_row import OperationKmRow
from rbsoftskkm.dto.operations.operation_list_item import OperationListItem
from rbsoftskkm.dto.queue.queue_item import QueueItem
from rbsoftskkm.dto.queue.queue_task_state import QueueTaskState
from rbsoftskkm.dto.results.check_document import CheckDocument
from rbsoftskkm.dto.results.data_kkt import DataKkt
from rbsoftskkm.dto.results.device_list_response import DeviceListResponse
from rbsoftskkm.dto.results.fiscal_result import FiscalResult
from rbsoftskkm.dto.results.kkt_status import KktStatus
from rbsoftskkm.dto.results.picture import Picture
from rbsoftskkm.dto.results.print_form_line import PrintFormLine
from rbsoftskkm.dto.results.processing_km_result import ProcessingKmResult
from rbsoftskkm.dto.results.request_km_result import RequestKmResult
from rbsoftskkm.dto.results.res_shift_total import ResShiftTotal
from rbsoftskkm.dto.results.response_current_status import ResponseCurrentStatus
from rbsoftskkm.dto.results.response_task_status import ResponseTaskStatus
from rbsoftskkm.dto.results.shift_list_item import ShiftListItem
from rbsoftskkm.dto.templates.check_template import CheckTemplate
from rbsoftskkm.dto.templates.check_template_list_item import CheckTemplateListItem
from rbsoftskkm.dto.templates.print_template import PrintTemplate as _PrintTemplate


class SkkmConnectorState(SkkmConnectorBase):
    """Поля результата. Заполняются библиотекой после каждого вызова."""

    #: Успех последнего вызова.
    Ok: bool

    #: Код ошибки сервера. 0 — нет ошибки.
    ErrorCode: int

    #: Текст ошибки сервера.
    ErrorDescription: str

    #: Поле Result последнего ответа сервера (разобранный JSON).
    LastResult: Any

    #: Фискальный блок ответа.
    FiscalResult: Optional[FiscalResult]

    #: Список устройств.
    Devices: list[DeviceListResponse]

    #: Данные кассы.
    Kkt: Optional[DataKkt]

    #: Состояние ККМ.
    Status: Optional[KktStatus]

    #: Статус смены.
    ShiftStatus: Optional[ResponseCurrentStatus]

    #: Итоги смены.
    ShiftTotals: Optional[ResShiftTotal]

    #: Остаток наличных.
    CashBalance: Decimal

    #: Список картинок.
    Pictures: list[Picture]

    #: Ширина строки чека в символах.
    LineLength: int

    #: Ширина печатной области в пикселях.
    LineLengthPixels: int

    #: Необнуляемая сумма продаж.
    NonZeroSum: Decimal

    #: Результат локальной проверки КМ.
    MarkingCheck: Optional[RequestKmResult]

    #: Результат проверки КМ в ОИСМ.
    MarkingProcessing: Optional[ProcessingKmResult]

    #: Документ.
    Check: Optional[CheckDocument]

    #: Список документов.
    Checks: list[CheckDocument]

    #: Статус задания.
    TaskStatus: Optional[ResponseTaskStatus]

    #: Печатная форма.
    PrintForm: list[PrintFormLine]

    #: Список отчётов.
    Shifts: list[ShiftListItem]

    #: Версия сервера.
    ServerVersion: str

    #: Токен пользователя.
    UserToken: Optional[UserToken]

    #: Список пользователей.
    Users: list[ServiceUser]

    #: Настройки службы.
    ServiceSettingsResult: Optional[ServiceSettings]

    #: Список пулов.
    Pools: list[str]

    #: Очередь печати.
    Queue: list[QueueItem]

    #: Состояние задания очереди.
    QueueTask: Optional[QueueTaskState]

    #: Операция.
    Operation: Optional[DeviceTaskInfo]

    #: История операции.
    OperationHistory: list[OperationHistoryItem]

    #: TLV операции.
    OperationTlv: str

    #: Коды маркировки операции.
    OperationKm: list[OperationKmRow]

    #: Связанные операции.
    RelatedOperations: list[DeviceTaskInfo]

    #: Список операций.
    Operations: list[OperationListItem]

    #: Шаблон печати.
    PrintTemplate: Optional[_PrintTemplate]

    #: Список шаблонов печати.
    Templates: list[_PrintTemplate]

    #: Шаблон чека.
    CheckTemplate: Optional[CheckTemplate]

    #: Список шаблонов чека.
    CheckTemplates: list[CheckTemplateListItem]

    #: Документ фискализации.
    FiscalizationDocument: Optional[_FiscalizationDocument]

    #: Список фискализаций.
    Fiscalizations: list[_FiscalizationDocument]

    #: Результат проверки маркировки.
    MarkingVerify: Optional[MarkingVerifyResult]

    #: Картинка в Base64.
    PictureBase64Result: str

    def __init__(self) -> None:
        super().__init__()
        self.Ok = False
        self.ErrorCode = 0
        self.ErrorDescription = ""
        self.LastResult = None
        self.FiscalResult = None
        self.Devices = []
        self.Kkt = None
        self.Status = None
        self.ShiftStatus = None
        self.ShiftTotals = None
        self.CashBalance = Decimal("0")
        self.Pictures = []
        self.LineLength = 0
        self.LineLengthPixels = 0
        self.NonZeroSum = Decimal("0")
        self.MarkingCheck = None
        self.MarkingProcessing = None
        self.Check = None
        self.Checks = []
        self.TaskStatus = None
        self.PrintForm = []
        self.Shifts = []
        self.ServerVersion = ""
        self.UserToken = None
        self.Users = []
        self.ServiceSettingsResult = None
        self.Pools = []
        self.Queue = []
        self.QueueTask = None
        self.Operation = None
        self.OperationHistory = []
        self.OperationTlv = ""
        self.OperationKm = []
        self.RelatedOperations = []
        self.Operations = []
        self.PrintTemplate = None
        self.Templates = []
        self.CheckTemplate = None
        self.CheckTemplates = []
        self.FiscalizationDocument = None
        self.Fiscalizations = []
        self.MarkingVerify = None
        self.PictureBase64Result = ""
