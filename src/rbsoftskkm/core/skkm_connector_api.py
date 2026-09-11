"""Публичные методы коннектора: один метод — один запрос к серверу ККМ."""

from __future__ import annotations

import uuid
from datetime import timedelta
from decimal import Decimal

from rbsoftskkm.core.skkm_connector_check_input import today
from rbsoftskkm.core.skkm_connector_requests import SkkmConnectorRequests
from rbsoftskkm.data.contracts.admin_contracts import (
    CheckCopyFnParameters,
    DeviceFontSettingsRequest,
    DeviceSettingsRequest,
    MarkingCodesRequest,
    ServiceSettingsRequest,
    UserProfileRequest,
)
from rbsoftskkm.data.contracts.cash_sum import CashSum
from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.data.contracts.fiscalization_request import FiscalizationRequest
from rbsoftskkm.data.contracts.line_length_v2 import LineLengthV2
from rbsoftskkm.data.contracts.overall_totals import OverallTotals
from rbsoftskkm.data.contracts.request_confirm_km import RequestConfirmKm
from rbsoftskkm.data.contracts.request_km import RequestKm
from rbsoftskkm.data.contracts.request_km_parameters import RequestKmParameters
from rbsoftskkm.data.contracts.upload_picture import UploadPicture
from rbsoftskkm.data.kkm_transport import escape_data
from rbsoftskkm.dto.admin.device_settings import DeviceSettings
from rbsoftskkm.dto.admin.service_settings import ServiceSettings
from rbsoftskkm.dto.admin.service_user import ServiceUser
from rbsoftskkm.dto.admin.user_token import UserToken
from rbsoftskkm.dto.enums.check_type import CheckType
from rbsoftskkm.dto.enums.km_confirmation_type import KmConfirmationType
from rbsoftskkm.dto.enums.marking_planned_status import MarkingPlannedStatus
from rbsoftskkm.dto.enums.measure_of_quantity import MeasureOfQuantity
from rbsoftskkm.dto.enums.picture_alignment import PictureAlignment
from rbsoftskkm.dto.enums.tax_system import TaxSystem
from rbsoftskkm.dto.fiscalization.fiscalization_document import FiscalizationDocument
from rbsoftskkm.dto.marking.marking_verify_result import MarkingVerifyResult
from rbsoftskkm.dto.operations.device_task_info import DeviceTaskInfo
from rbsoftskkm.dto.operations.operation_history_item import OperationHistoryItem
from rbsoftskkm.dto.operations.operation_km_row import OperationKmRow
from rbsoftskkm.dto.operations.operation_list_item import OperationListItem
from rbsoftskkm.dto.payments import Payments
from rbsoftskkm.dto.queue.queue_item import QueueItem
from rbsoftskkm.dto.queue.queue_task_state import QueueTaskState
from rbsoftskkm.dto.results.check_document import CheckDocument
from rbsoftskkm.dto.results.data_kkt import DataKkt
from rbsoftskkm.dto.results.device_list_response import DeviceListResponse
from rbsoftskkm.dto.results.kkt_status import KktStatus
from rbsoftskkm.dto.results.picture import Picture
from rbsoftskkm.dto.results.print_form_line import PrintFormLine
from rbsoftskkm.dto.results.processing_km_result import ProcessingKmResult
from rbsoftskkm.dto.results.request_km_result import RequestKmResult
from rbsoftskkm.dto.results.res_shift_total import ResShiftTotal
from rbsoftskkm.dto.results.response_current_status import ResponseCurrentStatus
from rbsoftskkm.dto.results.response_task_status import ResponseTaskStatus
from rbsoftskkm.dto.templates.check_template import CheckTemplate
from rbsoftskkm.dto.templates.check_template_list_item import CheckTemplateListItem
from rbsoftskkm.dto.templates.print_template import PrintTemplate


class SkkmConnectorApi(SkkmConnectorRequests):
    """Методы Сервера ККМ."""

    def NewRequest(self) -> None:
        """Очистка входных данных перед новым запросом и результатов прошлого вызова."""
        self.PaymentType = CheckType.Sale
        self.IsProcessed = False
        self.TaxVariant = TaxSystem.ОСН
        self.Electronically = False
        self.OperationOnline = False
        self.TimeZone = None
        self.TextBefore = ""
        self.TextAfter = ""
        self.SaleLocation = ""
        self.SaleAddress = ""
        self.SenderEmail = ""
        self.AdditionalAttribute = ""
        self.IndustryAttribute = None
        self.UserAttribute = None
        self.OperationalAttribute = None
        self.ElectronicPayments.clear()
        self.AgentSign = None
        self.Agent = None
        self.Vendor = None
        self.Customer = None
        self.Payments = Payments()
        self.Positions.clear()
        self.CorrectionData = None
        self.Correction105Taxes = None
        self.CashAmount = Decimal("0")
        self.TextForPrint = ""
        self.PictureName = ""
        self.PictureBase64 = ""
        self.PictureAlignment = PictureAlignment.Center
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
        self.ShiftsFrom = today() - timedelta(days=7)
        self.ShiftsTo = today()
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
        self.ShiftTotals = None
        self.NonZeroSum = Decimal("0")
        self.Ok = False
        self.ErrorCode = 0
        self.ErrorDescription = ""
        self.LastResult = None
        self.FiscalResult = None
        self.MarkingCheck = None
        self.MarkingProcessing = None
        self.Check = None
        self.Checks = []
        self.TaskStatus = None
        self.PrintForm = []
        self.Shifts = []

    def Ping(self) -> None:
        """Проверка доступности сервера ККМ. Не требует передачи ключа доступа (api_key)."""
        self._get("ping")

    def GetDeviceList(self) -> None:
        """Получение списка зарегистрированных ККТ."""
        self._get("kkt/list")
        self.Devices = self._read_result_list(DeviceListResponse)

    def Connect(self) -> None:
        """Получение подробной информации об устройстве ККТ."""
        self._get(f"kkt?{self._device_query}")
        self.Kkt = self._read_result(DataKkt)
        if self.Kkt is not None and self.Kkt.Status is not None:
            self.Status = self.Kkt.Status
        if self.Kkt is not None and self.Kkt.Device is not None:
            self.LineLength = self.Kkt.Device.LineLength
        elif self.Kkt is not None and self.Kkt.Status is not None:
            self.LineLength = self.Kkt.Status.LineLength
        if self.Kkt is not None and self.Kkt.Fn is not None and (self.Kkt.Fn.SaleLocation or "").strip():
            self.SaleLocation = self.Kkt.Fn.SaleLocation or ""

    def GetStatus(self) -> None:
        """Получение расширенного статуса ККТ."""
        self._get(f"kkt/status?{self._device_query}")
        self.Status = self._read_result(KktStatus)
        if self.Status is None:
            return
        self.LineLength = self.Status.LineLength
        self.ShiftNumber = self.Status.ShiftNumber
        self.CheckNumber = self.Status.DocNumber

    def GetShiftStatus(self) -> None:
        """Получение краткого статуса смены и очереди ОФД."""
        self._get(f"kkt/shift/status?{self._device_query}")
        self.ShiftStatus = self._read_result(ResponseCurrentStatus)
        if self.ShiftStatus is None:
            return
        self.ShiftNumber = self.ShiftStatus.ShiftNumber
        self.CheckNumber = self.ShiftStatus.CheckNumber

    def OpenShift(self) -> None:
        """Открытие кассовой смены."""
        self._post("shift/open", self._check_base())

    def CloseShift(self) -> None:
        """Закрытие кассовой смены (Z-отчёт)."""
        self._post("shift/z", self._check_base())

    def ReportX(self) -> None:
        """Формирование X-отчёта (без закрытия смены)."""
        self._post("shift/x", self._check_base())

    def ReportSettlement(self) -> None:
        """Формирование отчёта о текущем состоянии расчётов."""
        self._post("report/settlement", self._check_base())

    def GetReportX(self) -> None:
        """Возвращает X-отчёт по идентификатору документа (docId)."""
        self._get_document_by_id("shift/x")

    def GetReportZ(self) -> None:
        """Возвращает Z-отчёт по идентификатору документа (docId)."""
        self._get_document_by_id("shift/z")

    def GetOpenShift(self) -> None:
        """Возвращает результат открытия смены по идентификатору документа (docId)."""
        self._get_document_by_id("shift/open")

    def GetReportSettlement(self) -> None:
        """Возвращает отчёт о состоянии расчётов по идентификатору документа (docId)."""
        self._get_document_by_id("report/settlement")

    def GetOverAll(self) -> None:
        """Получение необнуляемых (накопительных) счётчиков ККТ."""
        self._get(f"kkt/counters/overall?{self._device_query}")
        totals = self._read_result(OverallTotals)
        sales = totals.Counters.Sales if totals is not None and totals.Counters is not None else None
        self.NonZeroSum = sales.Sum if sales is not None else Decimal("0")

    def GetLineLength(self) -> None:
        """Получение максимальной ширины строки чека устройства."""
        self._get(f"kkt/lineLength?{self._device_query}")
        length = self._read_result(LineLengthV2)
        if length is None:
            return
        self.LineLength = length.LineLength
        self.LineLengthPixels = length.LineLengthPixels

    def GetTotals(self) -> None:
        """Получение счётчиков за смену."""
        self._get(f"kkt/counters/shift?{self._device_query}")
        self.ShiftTotals = self._read_result(ResShiftTotal)

    def GetShiftList(self) -> None:
        """Получение списка Z-отчётов за период."""
        extra = f"reportType={self.ReportType}" if self.ReportType > 0 else None
        self._get_report_list("shift/z/list", extra)

    def GetOpenShiftList(self) -> None:
        """Получение списка открытий смен за период."""
        self._get_report_list("shift/open/list")

    def GetReportXList(self) -> None:
        """Получение списка X-отчётов за период."""
        self._get_report_list("shift/x/list")

    def GetReportSettlementList(self) -> None:
        """Список отчётов о состоянии расчётов по устройству за период."""
        self._get_report_list("report/settlement/list")

    def PrintCheck(self) -> None:
        """Печать кассового чека."""
        self._post("check", self._check_body())

    def PrintCheckAsync(self) -> None:
        """Асинхронно поставить фискальный чек в очередь печати."""
        self._post("check/async", self._check_body())

    def PrintCheckCorrection120(self) -> None:
        """Печать чека коррекции для ФФД 1.2."""
        self._post("correction120", self._correction120_body())

    def PrintCheckCorrection120Async(self) -> None:
        """Асинхронно печатает чек коррекции для ФФД 1.2."""
        self._post("correction120/async", self._correction120_body())

    def PrintCheckCorrection105(self) -> None:
        """Печать чека коррекции для ФФД 1.0.5."""
        self._post("correction105", self._correction105_body())

    def PrintCheckCorrection105Async(self) -> None:
        """Асинхронно ставит печать чека коррекции для ФФД 1.0.5."""
        self._post("correction105/async", self._correction105_body())

    def GetCorrection120(self) -> None:
        """Возвращает чек коррекции ФФД 1.2 по идентификатору документа (docId)."""
        self._get_document_by_id("correction120")

    def GetCorrection120List(self) -> None:
        """Получение списка чеков коррекции ФФД 1.2."""
        self._get_check_list("correction120/list")

    def GetCorrection105(self) -> None:
        """Возвращает чек коррекции ФФД 1.0.5 по идентификатору документа (docId)."""
        self._get_document_by_id("correction105")

    def GetCorrection105List(self) -> None:
        """Получение списка чеков коррекции ФФД 1.0.5."""
        self._get_check_list("correction105/list")

    def GetChecksByShift(self) -> None:
        """Получение списка чеков за смену."""
        self._get(f"check/list?{self._device_query}&shift={self.ShiftNumber}")
        self.Checks = self._read_result_list(CheckDocument)

    def GetTaskStatus(self) -> None:
        """Возвращает статус выполнения задания по идентификатору документа (docId)."""
        self._get(f"task/status?{self._id_query}")
        self.TaskStatus = self._read_result(ResponseTaskStatus)
        if self.TaskStatus is None:
            return
        if self.TaskStatus.FiscalSign:
            self.FiscalSign = self.TaskStatus.FiscalSign
        if self.TaskStatus.DocNumber > 0:
            self.CheckNumber = self.TaskStatus.DocNumber
        if self.TaskStatus.ShiftNumber > 0:
            self.ShiftNumber = self.TaskStatus.ShiftNumber
        if self.TaskStatus.DocId:
            self.DocumentId = self.TaskStatus.DocId

    def GetCheck(self) -> None:
        """Возвращает результат операции по идентификатору документа (docId)."""
        self._get_document_by_id("check")

    def GetFiscalSign(self) -> None:
        """Получение фискального признака (ФП) по номеру фискального документа (ФД)."""
        self._get(f"check/fiscalSign?docNumber={self.CheckNumber}&{self._device_query}")
        if self.Ok and isinstance(self.LastResult, str):
            self.FiscalSign = self.LastResult

    def PrintCheckCopy(self) -> None:
        """Печать копии чека."""
        if not self.DocumentId.strip():
            self._post(f"check/copy/last?{self._device_query}")
        else:
            self._post("check/copy", CheckbaseParameters(DeviceName=self.DeviceName, DocId=self.DocumentId))

    def GetPrintForm(self) -> None:
        """Возвращает печатную форму документа по его идентификатору (docId)."""
        self._get(f"task/form?{self._id_query}")
        self.PrintForm = self._read_result_list(PrintFormLine)

    def CashIn(self) -> None:
        """Регистрация операции внесения наличных в денежный ящик."""
        self._post("cashin", self._cash_body())

    def CashOut(self) -> None:
        """Регистрация операции выемки наличных из денежного ящика."""
        self._post("cashout", self._cash_body())

    def OpenCashdrawer(self) -> None:
        """Открытие денежного ящика."""
        self._post("cash/open", self._check_base())

    def GetCash(self) -> None:
        """Получение остатка наличных в денежном ящике."""
        self._get(f"cash?{self._device_query}")
        cash = self._read_result(CashSum)
        self.CashBalance = cash.Sum if cash is not None else Decimal("0")

    def GetCashIn(self) -> None:
        """Возвращает результат операции внесения наличных по идентификатору операции (docId)."""
        self._get_document_by_id("cashin")

    def GetCashInList(self) -> None:
        """Получение списка операций внесения наличных по имени устройства."""
        self._get_check_list("cashin/list")

    def GetCashOut(self) -> None:
        """Возвращает результат операции выемки наличных по идентификатору операции (docId)."""
        self._get_document_by_id("cashout")

    def SendPicture(self) -> None:
        """Загрузка изображения в выбранную ККТ."""
        self._post(
            "picture",
            UploadPicture(
                DeviceName=self.DeviceName,
                PictureName=self.PictureName,
                Base64=self.PictureBase64,
                Alignment=int(self.PictureAlignment),
            ),
        )

    def GetPictureList(self) -> None:
        """Получение списка изображений."""
        self._get(f"picture/list?{self._device_query}")
        self.Pictures = self._read_result_list(Picture)

    def OpenSessionRegistrationKM(self) -> None:
        """Открытие сессии регистрации (проверки) кодов маркировки на ККТ."""
        self._post("marking/session/open", CheckbaseParameters(DeviceName=self.DeviceName))

    def CloseSessionRegistrationKM(self) -> None:
        """Закрытие сессии регистрации (проверки) кодов маркировки на ККТ."""
        self._post("marking/session/close", CheckbaseParameters(DeviceName=self.DeviceName))

    def RequestKM(self) -> None:
        """Локальная проверка кода маркировки на ККТ (ФФД 1.2)."""
        if not self.RequestKmGuid.strip():
            self.RequestKmGuid = str(uuid.uuid4())

        self._post(
            "marking/km/request",
            RequestKmParameters(
                DeviceName=self.DeviceName,
                RequestKM=RequestKm(
                    Guid=self.RequestKmGuid,
                    NotSendToServer=self.NotSendToServer,
                    WaitForResult=self.WaitForResult,
                    MarkingCode=self.MarkingCode,
                    PlannedStatus=int(self.PlannedStatus),
                    Quantity=self.MarkingQuantity,
                    MeasureOfQuantity=int(self.MeasureOfQuantity),
                    FractionalQuantityNumerator=self.FractionalQuantityNumerator
                    if self.FractionalQuantityNumerator > 0
                    else None,
                    FractionalQuantityDenominator=self.FractionalQuantityDenominator
                    if self.FractionalQuantityDenominator > 0
                    else None,
                ),
            ),
        )
        self.MarkingCheck = self._read_result(RequestKmResult)

    def GetProcessingKMResult(self) -> None:
        """Получение результата проверки кода маркировки в ОИСМ."""
        self._get(f"marking/km/result?{self._device_query}")
        self.MarkingProcessing = self._read_result(ProcessingKmResult)
        if self.MarkingProcessing is not None and (self.MarkingProcessing.Guid or "").strip():
            self.RequestKmGuid = self.MarkingProcessing.Guid or ""

    def ConfirmKM(self) -> None:
        """Подтверждение, будет ли ранее проверенный код маркировки фактически включён в документ реализации.

        Действительно только в рамках открытой сессии регистрации.
        """
        self._post(
            "marking/km/confirm",
            RequestConfirmKm(
                DeviceName=self.DeviceName,
                GUID=self.RequestKmGuid,
                ConfirmationType=int(self.ConfirmationType),
            ),
        )

    def PrintSlip(self) -> None:
        """Печать нефискального документа."""
        self._post("slip", self._slip_body())

    def PrintSlipAsync(self) -> None:
        """Асинхронно поставить нефискальный документ в очередь печати."""
        self._post("slip/async", self._slip_body())

    def GetVersion(self) -> None:
        """Версия сервера ККМ."""
        self._get("version")
        if isinstance(self.LastResult, str):
            self.ServerVersion = self.LastResult
        else:
            self.ServerVersion = "" if self.LastResult is None else str(self.LastResult)

    def GetUserToken(self) -> None:
        """Получение токена авторизации по логину и паролю.

        Нужны AuthUserName и AuthPassword (по умолчанию Admin / Admin).
        """
        if not self.AuthUserName.strip() or not self.AuthPassword.strip():
            self.Ok = False
            self.ErrorCode = -1
            self.ErrorDescription = "Укажите AuthUserName и AuthPassword для получения токена."
            return

        self._get("user/token", use_basic_auth=True)
        self.UserToken = self._read_result(UserToken)
        if self.UserToken is not None and (self.UserToken.TokenId or "").strip():
            self.Token = self.UserToken.TokenId or ""

    def GetUserList(self) -> None:
        """Список пользователей сервера ККМ."""
        self._get("user/list")
        self.Users = self._read_result_list(ServiceUser)

    def AddUser(self) -> None:
        """Добавление пользователя."""
        self._post("user", UserProfileRequest(User=self.ServiceUser))

    def UpdateUser(self) -> None:
        """Изменение пользователя."""
        self._put(f"user?id={escape_data(self.UserId)}", self.ServiceUser)

    def DeleteUser(self) -> None:
        """Удаление пользователя."""
        self._delete(f"user?id={escape_data(self.UserId)}")

    def GetServiceSettings(self) -> None:
        """Получение настроек службы печати."""
        self._get("service/settings")
        self.ServiceSettingsResult = self._read_result(ServiceSettings)

    def SaveServiceSettings(self) -> None:
        """Сохранение настроек службы печати."""
        self._post("service/settings", ServiceSettingsRequest(ServiceSettings=self.ServiceSettings))

    def AddDevice(self) -> None:
        """Добавление кассы на сервер."""
        settings = self.DeviceSettings or DeviceSettings()
        settings.DeviceName = self.DeviceName if not (settings.DeviceName or "").strip() else settings.DeviceName
        self._post("kkt", DeviceSettingsRequest(DeviceName=settings.DeviceName, Settings=settings))

    def UpdateDevice(self) -> None:
        """Изменение настроек кассы."""
        settings = self.DeviceSettings or DeviceSettings()
        settings.DeviceName = self.DeviceName if not (settings.DeviceName or "").strip() else settings.DeviceName
        self._put("kkt", DeviceSettingsRequest(DeviceName=settings.DeviceName, Settings=settings))

    def DeleteDevice(self) -> None:
        """Удаление кассы с сервера."""
        self._delete(f"kkt?device={escape_data(self.DeviceName)}")

    def RebootDevice(self) -> None:
        """Перезагрузка кассы."""
        self._post("kkt/reboot", self._check_base())

    def SetDeviceFont(self) -> None:
        """Настройка шрифтов шаблона кассы."""
        settings = self.DeviceSettings
        self._post(
            "kkt/font/setting",
            DeviceFontSettingsRequest(
                DeviceName=self.DeviceName,
                TemplateSettingH1=settings.TemplateSettingH1 if settings is not None else None,
                TemplateSettingH2=settings.TemplateSettingH2 if settings is not None else None,
                TemplateSettingH3=settings.TemplateSettingH3 if settings is not None else None,
                TemplateSettingH4=settings.TemplateSettingH4 if settings is not None else None,
                TemplateSettingH5=settings.TemplateSettingH5 if settings is not None else None,
            ),
        )

    def GetPoolList(self) -> None:
        """Список пулов устройств."""
        self._get("pool/list")
        self.Pools = self._read_result_strings()

    def GetDeviceListByPool(self) -> None:
        """Список касс в пуле."""
        self._get(f"kkt/list/byPool?pool={escape_data(self.PoolName)}")
        self.Devices = self._read_result_list(DeviceListResponse)

    def OpenShiftAsync(self) -> None:
        """Асинхронное открытие смены."""
        self._post("shift/open/async", self._check_base())

    def CloseShiftAsync(self) -> None:
        """Асинхронное закрытие смены."""
        self._post("shift/z/async", self._check_base())

    def ReportXAsync(self) -> None:
        """Асинхронный X-отчёт."""
        self._post("shift/x/async", self._check_base())

    def ReportSettlementAsync(self) -> None:
        """Асинхронный отчёт о состоянии расчётов."""
        self._post("report/settlement/async", self._check_base())

    def CashInAsync(self) -> None:
        """Асинхронное внесение наличных."""
        self._post("cashin/async", self._cash_body())

    def CashOutAsync(self) -> None:
        """Асинхронная выемка наличных."""
        self._post("cashout/async", self._cash_body())

    def GetCheckList(self) -> None:
        """Список чеков за период или смену."""
        query = f"{self._device_query}&{self._date_query(self.ShiftsFrom, self.ShiftsTo)}"
        if self.ShiftNumber > 0:
            query += f"&shift={self.ShiftNumber}"
        self._get(f"check/list?{query}")
        self.Checks = self._read_result_list(CheckDocument)

    def PrintCheckCopyFn(self) -> None:
        """Печать копии чека по данным фискального накопителя."""
        self._post(
            "check/copy/fn",
            CheckCopyFnParameters(
                DeviceName=self.DeviceName,
                FnNumber=self.FnNumber,
                FiscalSign=self.FiscalSign,
                DocNumber=self.CheckNumber,
            ),
        )

    def GetSlip(self) -> None:
        """Получение слипа по идентификатору документа."""
        self._get_document_by_id("slip")

    def GetSlipList(self) -> None:
        """Список слипов по кассе."""
        self._get_check_list("slip/list")

    def GetPicture(self) -> None:
        """Получение картинки по имени."""
        self._get(f"picture?{self._device_query}&id={escape_data(self.PictureId)}")
        if self.Ok and isinstance(self.LastResult, str):
            self.PictureBase64Result = self.LastResult

    def DeletePicture(self) -> None:
        """Удаление картинки."""
        self._delete(f"picture?{self._device_query}&id={escape_data(self.PictureId)}")

    def AddTemplate(self) -> None:
        """Создание шаблона печати."""
        self._post("template", self.TemplateParameters)

    def UpdateTemplate(self) -> None:
        """Изменение шаблона печати."""
        self._put("template", self.TemplateParameters)

    def DeleteTemplate(self) -> None:
        """Удаление шаблона печати."""
        self._delete(f"template?id={escape_data(self.TemplateName)}")

    def GetTemplateList(self) -> None:
        """Список шаблонов печати."""
        self._get("template/list")
        self.Templates = self._read_template_list()

    def GetTemplate(self) -> None:
        """Получение шаблона печати по имени."""
        self._get(f"template?name={escape_data(self.TemplateName)}")
        self.PrintTemplate = self._read_result(PrintTemplate)

    def AddCheckTemplate(self) -> None:
        """Создание шаблона чека."""
        self._post("checkTemplate", self._check_template_body())

    def UpdateCheckTemplate(self) -> None:
        """Изменение шаблона чека."""
        self._put("checkTemplate", self._check_template_body())

    def DeleteCheckTemplate(self) -> None:
        """Удаление шаблона чека."""
        self._delete(f"checkTemplate?id={escape_data(self.TemplateName)}")

    def GetCheckTemplateList(self) -> None:
        """Список шаблонов чека."""
        self._get("checkTemplate/list")
        self.CheckTemplates = self._read_result_list(CheckTemplateListItem)

    def GetCheckTemplate(self) -> None:
        """Получение шаблона чека по имени."""
        self._get(f"checkTemplate?id={escape_data(self.TemplateName)}")
        self.CheckTemplate = self._read_result(CheckTemplate)

    def GetQueue(self) -> None:
        """Состояние очереди печати."""
        self._get("queue")
        self.Queue = self._read_result_list(QueueItem)

    def GetQueueTask(self) -> None:
        """Состояние задания в очереди."""
        self._get(f"queue/task?taskId={escape_data(self.QueueTaskId)}")
        self.QueueTask = self._read_result(QueueTaskState)

    def GetQueueTaskHistory(self) -> None:
        """История обработки задания в очереди."""
        self._get(f"queue/task/history?taskId={escape_data(self.QueueTaskId)}")
        self.QueueTask = self._read_result(QueueTaskState)
        if self.QueueTask is not None:
            self.OperationHistory = [
                OperationHistoryItem(Time=item.Time, State=item.State, Description=item.Description)
                for item in self.QueueTask.History
            ]

    def CancelQueueTask(self) -> None:
        """Отмена задания в очереди."""
        self._delete(f"queue/task?taskId={escape_data(self.QueueTaskId)}")

    def VerifyMarking(self) -> None:
        """Проверка кода маркировки через внешний сервис."""
        self._post(
            "marking/km/verify",
            MarkingCodesRequest(DeviceName=self.DeviceName, Codes=list(self.MarkingCodes)),
        )
        self.MarkingVerify = self._read_result(MarkingVerifyResult)

    def VerifyMarkingTsPiot(self) -> None:
        """Проверка кода маркировки через ТС ПИоТ."""
        self._post(
            "marking/km/tspiot/verify",
            MarkingCodesRequest(DeviceName=self.DeviceName, Codes=list(self.MarkingCodes)),
        )
        self.MarkingVerify = self._read_result(MarkingVerifyResult)

    def VerifyMarkingLmcz(self) -> None:
        """Проверка кода маркировки через ЛМ ЧЗ."""
        self._post(
            "marking/km/lmcz/verify",
            MarkingCodesRequest(DeviceName=self.DeviceName, Codes=list(self.MarkingCodes)),
        )
        self.MarkingVerify = self._read_result(MarkingVerifyResult)

    def Fiscalization(self) -> None:
        """Фискализация кассы."""
        self._post("fiscalization", self._fiscalization_body())

    def FiscalizationAsync(self) -> None:
        """Асинхронная фискализация кассы."""
        self._post("fiscalization/async", self._fiscalization_body())

    def GetFiscalization(self) -> None:
        """Результат фискализации по идентификатору документа."""
        self._get_document_by_id("fiscalization")
        self.FiscalizationDocument = self._read_result(FiscalizationDocument)

    def GetFiscalizationList(self) -> None:
        """Список операций фискализации по кассе."""
        self._get(f"fiscalization/list?{self._device_query}")
        self.Fiscalizations = self._read_result_list(FiscalizationDocument)

    def GetOperationLast(self) -> None:
        """Последняя операция из базы.

        tasktype — PaymentType (CheckType), isProcessed — IsProcessed.
        """
        processed = "true" if self.IsProcessed else "false"
        self._get(f"operation/last?tasktype={int(self.PaymentType)}&isProcessed={processed}")
        self._apply_operation(self._read_result(DeviceTaskInfo))

    def GetOperation(self) -> None:
        """Операция по идентификатору документа."""
        self._get(f"operation?{self._doc_id_query}")
        self._apply_operation(self._read_result(DeviceTaskInfo))

    def GetOperationHistory(self) -> None:
        """История операции по идентификатору документа."""
        self._get(f"operation/history?{self._doc_id_query}")
        self.OperationHistory = self._read_result_list(OperationHistoryItem)

    def GetOperationTlv(self) -> None:
        """TLV-данные операции."""
        self._get(f"operation/tlv?{self._doc_id_query}")
        if self.Ok and isinstance(self.LastResult, str):
            self.OperationTlv = self.LastResult

    def GetOperationKm(self) -> None:
        """Данные маркировки операции."""
        self._get(f"operation/km?{self._doc_id_query}")
        self.OperationKm = self._read_result_list(OperationKmRow)

    def GetOperationRelated(self) -> None:
        """Связанные операции."""
        self._get(f"operation/related?{self._doc_id_query}")
        self.RelatedOperations = self._read_result_list(DeviceTaskInfo)

    def GetOperationList(self) -> None:
        """Список операций за период."""
        self._get(f"operation/list?{self._date_query(self.ShiftsFrom, self.ShiftsTo)}")
        self.Operations = self._read_result_list(OperationListItem)

    def _fiscalization_body(self) -> FiscalizationRequest:
        source = self.FiscalizationParameters
        body = FiscalizationRequest(
            DeviceName=self.DeviceName,
            Cashier=self.Cashier,
            RnNumber=source.RnNumber if source else None,
            TaxationSystems=source.TaxationSystems if source else None,
            Vatin=source.Vatin if source else None,
            CompanyName=source.CompanyName if source else None,
            Fn=source.Fn if source else None,
            FfdVersionKkt=source.FfdVersionKkt if source else None,
            FfdVersionFn=source.FfdVersionFn if source else None,
            RegistrationLabelCodes=source.RegistrationLabelCodes if source else None,
            OfdAddress=source.OfdAddress if source else None,
            OfdPort=source.OfdPort if source else None,
            AutomaticNumber=source.AutomaticNumber if source else None,
            SenderEmail=source.SenderEmail if source else None,
            ReasonCode=source.ReasonCode if source else None,
            IsmHost=source.IsmHost if source else None,
            IsmPort=source.IsmPort if source else None,
            FnsUrl=source.FnsUrl if source else None,
            OfdVatin=source.OfdVatin if source else None,
            OfdName=source.OfdName if source else None,
            AgentTypes=source.AgentTypes if source else None,
            IsBsoSign=source.IsBsoSign if source else None,
            IsMarking=source.IsMarking if source else None,
            IsPawnshop=source.IsPawnshop if source else None,
            IsAssurance=source.IsAssurance if source else None,
            IsAutomatic=source.IsAutomatic if source else None,
            IsVending=source.IsVending if source else None,
            IsAutomaticPrinter=source.IsAutomaticPrinter if source else None,
            IsOnline=source.IsOnline if source else None,
            IsLottery=source.IsLottery if source else None,
            IsGambling=source.IsGambling if source else None,
            IsExcisable=source.IsExcisable if source else None,
            IsService=source.IsService if source else None,
            IsEncrypted=source.IsEncrypted if source else None,
            IsOffline=source.IsOffline if source else None,
            IsCateringServices=source.IsCateringServices if source else None,
            IsWholesaleTrade=source.IsWholesaleTrade if source else None,
            SaleAddress=source.SaleAddress if source else None,
            SaleLocation=source.SaleLocation if source else None,
        )
        self._fill_base(body)
        return body
