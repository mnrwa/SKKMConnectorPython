from __future__ import annotations

from rbsoftskkm.data.contracts.admin_contracts import (
    CheckCopyFnParameters,
    CheckTemplateDocumentRequest,
    CheckTemplateRequest,
    DeviceFontSettingsRequest,
    DeviceSettingsRequest,
    MarkingCodesRequest,
    ServiceSettingsRequest,
    UserProfileRequest,
)
from rbsoftskkm.data.contracts.api_position import ApiPosition
from rbsoftskkm.data.contracts.cash_sum import CashSum
from rbsoftskkm.data.contracts.cashdraw_parameters import CashdrawParameters
from rbsoftskkm.data.contracts.check_parameters import CheckParameters
from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.data.contracts.correction105_parameters import Correction105Parameters
from rbsoftskkm.data.contracts.correction120_parameters import Correction120Parameters
from rbsoftskkm.data.contracts.doc_position import DocPosition
from rbsoftskkm.data.contracts.document_parameters import DocumentParameters
from rbsoftskkm.data.contracts.fiscalization_request import FiscalizationRequest
from rbsoftskkm.data.contracts.line_length_v2 import LineLengthV2
from rbsoftskkm.data.contracts.overall_totals import OverallTotals
from rbsoftskkm.data.contracts.request_confirm_km import RequestConfirmKm
from rbsoftskkm.data.contracts.request_km import RequestKm
from rbsoftskkm.data.contracts.request_km_parameters import RequestKmParameters
from rbsoftskkm.data.contracts.text_string import TextString
from rbsoftskkm.data.contracts.upload_picture import UploadPicture

__all__ = [
    "ApiPosition",
    "CashSum",
    "CashdrawParameters",
    "CheckCopyFnParameters",
    "CheckParameters",
    "CheckTemplateDocumentRequest",
    "CheckTemplateRequest",
    "CheckbaseParameters",
    "Correction105Parameters",
    "Correction120Parameters",
    "DeviceFontSettingsRequest",
    "DeviceSettingsRequest",
    "DocPosition",
    "DocumentParameters",
    "FiscalizationRequest",
    "LineLengthV2",
    "MarkingCodesRequest",
    "OverallTotals",
    "RequestConfirmKm",
    "RequestKm",
    "RequestKmParameters",
    "ServiceSettingsRequest",
    "TextString",
    "UploadPicture",
    "UserProfileRequest",
]
