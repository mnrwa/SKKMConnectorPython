"""Коннектор Сервера ККМ: клиент REST API службы печати РБ-Софт.

Публичные имена — классы, поля и методы — совпадают с эталонной реализацией,
поэтому пишутся в PascalCase, а не по PEP 8. Обоснование — в README.
"""

from __future__ import annotations

from rbsoftskkm.core.skkm_connector import SkkmConnector
from rbsoftskkm.dto.admin.device_settings import DeviceSettings
from rbsoftskkm.dto.admin.proxy_config import ProxyConfig
from rbsoftskkm.dto.admin.service_settings import ServiceSettings
from rbsoftskkm.dto.admin.service_user import ServiceUser
from rbsoftskkm.dto.admin.user_token import UserToken
from rbsoftskkm.dto.cashier import Cashier
from rbsoftskkm.dto.correction105_taxes import Correction105Taxes
from rbsoftskkm.dto.correction_data import CorrectionData
from rbsoftskkm.dto.customer import Customer
from rbsoftskkm.dto.electronic_payment import ElectronicPayment
from rbsoftskkm.dto.enums.agent_type import AgentType
from rbsoftskkm.dto.enums.barcode_print_text import BarcodePrintText
from rbsoftskkm.dto.enums.barcode_type import BarcodeType
from rbsoftskkm.dto.enums.check_time_zone import CheckTimeZone
from rbsoftskkm.dto.enums.check_type import CheckType
from rbsoftskkm.dto.enums.connection_method import ConnectionMethod
from rbsoftskkm.dto.enums.correction_types import CorrectionTypes
from rbsoftskkm.dto.enums.device_type import DeviceType
from rbsoftskkm.dto.enums.electronic_payment_method import ElectronicPaymentMethod
from rbsoftskkm.dto.enums.fiscalization_operation_type import FiscalizationOperationType
from rbsoftskkm.dto.enums.fiscalization_reason_code import FiscalizationReasonCode
from rbsoftskkm.dto.enums.km_confirmation_type import KmConfirmationType
from rbsoftskkm.dto.enums.line_style import LineStyle
from rbsoftskkm.dto.enums.marking_planned_status import MarkingPlannedStatus
from rbsoftskkm.dto.enums.measure_of_quantity import MeasureOfQuantity
from rbsoftskkm.dto.enums.picture_alignment import PictureAlignment
from rbsoftskkm.dto.enums.print_alignment import PrintAlignment
from rbsoftskkm.dto.enums.print_font import PrintFont
from rbsoftskkm.dto.enums.print_line_type import PrintLineType
from rbsoftskkm.dto.enums.print_template_type import PrintTemplateType
from rbsoftskkm.dto.enums.service_user_role import ServiceUserRole
from rbsoftskkm.dto.enums.shift_state import ShiftState
from rbsoftskkm.dto.enums.sign_calculation_object import SignCalculationObject
from rbsoftskkm.dto.enums.sign_method_calculation import SignMethodCalculation
from rbsoftskkm.dto.enums.tax_system import TaxSystem
from rbsoftskkm.dto.fiscalization.fiscalization_document import FiscalizationDocument
from rbsoftskkm.dto.fiscalization.fiscalization_parameters import FiscalizationParameters
from rbsoftskkm.dto.marking.code_mark_info import CodeMarkInfo
from rbsoftskkm.dto.marking.marking_verify_result import MarkingVerifyResult
from rbsoftskkm.dto.operational_attribute import OperationalAttribute
from rbsoftskkm.dto.operations.device_task_info import DeviceTaskInfo
from rbsoftskkm.dto.operations.operation_history_item import OperationHistoryItem
from rbsoftskkm.dto.operations.operation_km_row import OperationKmRow
from rbsoftskkm.dto.operations.operation_list_item import OperationListItem
from rbsoftskkm.dto.operations.sender_info import SenderInfo
from rbsoftskkm.dto.payments import Payments
from rbsoftskkm.dto.positions.agent import Agent
from rbsoftskkm.dto.positions.barcode_line import BarcodeLine
from rbsoftskkm.dto.positions.fiscal_line import FiscalLine
from rbsoftskkm.dto.positions.fractional_quantity import FractionalQuantity
from rbsoftskkm.dto.positions.industry import Industry
from rbsoftskkm.dto.positions.marking import Marking
from rbsoftskkm.dto.positions.picture_line import PictureLine
from rbsoftskkm.dto.positions.position import Position
from rbsoftskkm.dto.positions.separator_line import SeparatorLine
from rbsoftskkm.dto.positions.text_line import TextLine
from rbsoftskkm.dto.positions.vendor import Vendor
from rbsoftskkm.dto.queue.document_history_item import DocumentHistoryItem
from rbsoftskkm.dto.queue.queue_item import QueueItem
from rbsoftskkm.dto.queue.queue_task_state import QueueTaskState
from rbsoftskkm.dto.results.backlog import Backlog
from rbsoftskkm.dto.results.cash_drawer import CashDrawer
from rbsoftskkm.dto.results.check_customer import CheckCustomer
from rbsoftskkm.dto.results.check_document import CheckDocument
from rbsoftskkm.dto.results.check_item import CheckItem
from rbsoftskkm.dto.results.check_payments import CheckPayments
from rbsoftskkm.dto.results.data_kkt import DataKkt
from rbsoftskkm.dto.results.device import Device
from rbsoftskkm.dto.results.device_list_response import DeviceListResponse
from rbsoftskkm.dto.results.doc_data import DocData
from rbsoftskkm.dto.results.doc_data_payments import DocDataPayments
from rbsoftskkm.dto.results.document_header import DocumentHeader
from rbsoftskkm.dto.results.driver import Driver
from rbsoftskkm.dto.results.fiscal_output_parameters import FiscalOutputParameters
from rbsoftskkm.dto.results.fiscal_result import FiscalResult
from rbsoftskkm.dto.results.fn import Fn
from rbsoftskkm.dto.results.fn_modes import FnModes
from rbsoftskkm.dto.results.kkt_license import KktLicense
from rbsoftskkm.dto.results.kkt_status import KktStatus
from rbsoftskkm.dto.results.ofd import Ofd
from rbsoftskkm.dto.results.picture import Picture
from rbsoftskkm.dto.results.print_form_barcode import PrintFormBarcode
from rbsoftskkm.dto.results.print_form_line import PrintFormLine
from rbsoftskkm.dto.results.processing_km_result import ProcessingKmResult
from rbsoftskkm.dto.results.qr_check_data import QrCheckData
from rbsoftskkm.dto.results.reg_data import RegData
from rbsoftskkm.dto.results.request_km_result import RequestKmResult
from rbsoftskkm.dto.results.res_shift_total import ResShiftTotal
from rbsoftskkm.dto.results.response_current_status import ResponseCurrentStatus
from rbsoftskkm.dto.results.response_task_status import ResponseTaskStatus
from rbsoftskkm.dto.results.shift_counters import ShiftCounters
from rbsoftskkm.dto.results.shift_income import ShiftIncome
from rbsoftskkm.dto.results.shift_list_item import ShiftListItem
from rbsoftskkm.dto.results.warnings import Warnings
from rbsoftskkm.dto.templates.check_template import CheckTemplate
from rbsoftskkm.dto.templates.check_template_document import CheckTemplateDocument
from rbsoftskkm.dto.templates.check_template_list_item import CheckTemplateListItem
from rbsoftskkm.dto.templates.check_template_parameters import CheckTemplateParameters
from rbsoftskkm.dto.templates.print_line import PrintLine
from rbsoftskkm.dto.templates.print_template import PrintTemplate
from rbsoftskkm.dto.templates.template_item import TemplateItem
from rbsoftskkm.dto.templates.template_parameters import TemplateParameters
from rbsoftskkm.dto.user_attribute import UserAttribute

__all__ = [
    "Agent",
    "AgentType",
    "Backlog",
    "BarcodeLine",
    "BarcodePrintText",
    "BarcodeType",
    "CashDrawer",
    "Cashier",
    "CheckCustomer",
    "CheckDocument",
    "CheckItem",
    "CheckPayments",
    "CheckTemplate",
    "CheckTemplateDocument",
    "CheckTemplateListItem",
    "CheckTemplateParameters",
    "CheckTimeZone",
    "CheckType",
    "CodeMarkInfo",
    "ConnectionMethod",
    "Correction105Taxes",
    "CorrectionData",
    "CorrectionTypes",
    "Customer",
    "DataKkt",
    "Device",
    "DeviceListResponse",
    "DeviceSettings",
    "DeviceTaskInfo",
    "DeviceType",
    "DocData",
    "DocDataPayments",
    "DocumentHeader",
    "DocumentHistoryItem",
    "Driver",
    "ElectronicPayment",
    "ElectronicPaymentMethod",
    "FiscalLine",
    "FiscalOutputParameters",
    "FiscalResult",
    "FiscalizationDocument",
    "FiscalizationOperationType",
    "FiscalizationParameters",
    "FiscalizationReasonCode",
    "Fn",
    "FnModes",
    "FractionalQuantity",
    "Industry",
    "KktLicense",
    "KktStatus",
    "KmConfirmationType",
    "LineStyle",
    "Marking",
    "MarkingPlannedStatus",
    "MarkingVerifyResult",
    "MeasureOfQuantity",
    "Ofd",
    "OperationHistoryItem",
    "OperationKmRow",
    "OperationListItem",
    "OperationalAttribute",
    "Payments",
    "Picture",
    "PictureAlignment",
    "PictureLine",
    "Position",
    "PrintAlignment",
    "PrintFont",
    "PrintFormBarcode",
    "PrintFormLine",
    "PrintLine",
    "PrintLineType",
    "PrintTemplate",
    "PrintTemplateType",
    "ProcessingKmResult",
    "ProxyConfig",
    "QrCheckData",
    "QueueItem",
    "QueueTaskState",
    "RegData",
    "RequestKmResult",
    "ResShiftTotal",
    "ResponseCurrentStatus",
    "ResponseTaskStatus",
    "SenderInfo",
    "SeparatorLine",
    "ServiceSettings",
    "ServiceUser",
    "ServiceUserRole",
    "ShiftCounters",
    "ShiftIncome",
    "ShiftListItem",
    "ShiftState",
    "SignCalculationObject",
    "SignMethodCalculation",
    "SkkmConnector",
    "TaxSystem",
    "TemplateItem",
    "TemplateParameters",
    "TextLine",
    "UserAttribute",
    "UserToken",
    "Vendor",
    "Warnings",
]
