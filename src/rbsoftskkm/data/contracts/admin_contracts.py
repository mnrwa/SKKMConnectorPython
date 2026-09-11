from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from rbsoftskkm.data.contracts.api_position import ApiPosition
from rbsoftskkm.dto.admin.device_settings import DeviceSettings
from rbsoftskkm.dto.admin.service_settings import ServiceSettings as _ServiceSettings
from rbsoftskkm.dto.admin.service_user import ServiceUser
from rbsoftskkm.dto.correction_data import CorrectionData as _CorrectionData
from rbsoftskkm.dto.customer import Customer as _Customer
from rbsoftskkm.dto.electronic_payment import ElectronicPayment
from rbsoftskkm.dto.operational_attribute import OperationalAttribute as _OperationalAttribute
from rbsoftskkm.dto.payments import Payments as _Payments
from rbsoftskkm.dto.positions.industry import Industry
from rbsoftskkm.dto.user_attribute import UserAttribute as _UserAttribute


@dataclass
class DeviceSettingsRequest:
    DeviceName: Optional[str] = None

    Settings: Optional[DeviceSettings] = None
@dataclass
class ServiceSettingsRequest:
    ServiceSettings: Optional[_ServiceSettings] = None
@dataclass
class UserProfileRequest:
    User: Optional[ServiceUser] = None
@dataclass
class DeviceFontSettingsRequest:
    DeviceName: Optional[str] = None

    TemplateSettingH1: Optional[str] = None

    TemplateSettingH2: Optional[str] = None

    TemplateSettingH3: Optional[str] = None

    TemplateSettingH4: Optional[str] = None

    TemplateSettingH5: Optional[str] = None
@dataclass
class CheckTemplateRequest:
    Name: Optional[str] = None

    Document: Optional[CheckTemplateDocumentRequest] = None
@dataclass
class CheckTemplateDocumentRequest:
    PaymentType: int = 0

    TaxVariant: int = 0

    Customer: Optional[_Customer] = None

    SenderEmail: Optional[str] = None

    SaleAddress: Optional[str] = None

    SaleLocation: Optional[str] = None

    Positions: Optional[list[ApiPosition]] = None

    Payments: Optional[_Payments] = None

    ElectronicPaymentInfo: Optional[list[ElectronicPayment]] = None

    Electronically: bool = False

    OperationalAttribute: Optional[_OperationalAttribute] = None

    IndustryAttribute: Optional[Industry] = None

    UserAttribute: Optional[_UserAttribute] = None

    TimeZone: Optional[int] = None

    OperationOnline: bool = False

    AdditionalAttribute: Optional[str] = None

    CorrectionData: Optional[_CorrectionData] = None
@dataclass
class CheckCopyFnParameters:
    DeviceName: Optional[str] = None

    FnNumber: Optional[str] = None

    FiscalSign: Optional[str] = None

    DocNumber: int = 0
@dataclass
class MarkingCodesRequest:
    DeviceName: Optional[str] = None

    Codes: list[str] = field(default_factory=list)
