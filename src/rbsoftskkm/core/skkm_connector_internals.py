"""Транспортная инфраструктура: выбор соединения, вызов и разбор ответа."""

from __future__ import annotations

from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any, Optional, TypeVar

from rbsoftskkm.core.skkm_connector_check_input import SkkmConnectorCheckInput, today
from rbsoftskkm.data import json_codec
from rbsoftskkm.data.kkm_transport import CancelToken, KkmTransport, escape_data
from rbsoftskkm.data.response_result import ResponseResult
from rbsoftskkm.dto.operations.device_task_info import DeviceTaskInfo
from rbsoftskkm.dto.results.backlog import Backlog
from rbsoftskkm.dto.results.check_document import CheckDocument
from rbsoftskkm.dto.results.fiscal_output_parameters import FiscalOutputParameters
from rbsoftskkm.dto.results.fiscal_result import FiscalResult
from rbsoftskkm.dto.results.shift_list_item import ShiftListItem
from rbsoftskkm.dto.templates.print_template import PrintTemplate

T = TypeVar("T")


class SkkmConnectorInternals(SkkmConnectorCheckInput):
    """Внутренние помощники запроса и разбора ответа."""

    @property
    def _device_query(self) -> str:
        return f"device={escape_data(self.DeviceName)}"

    @property
    def _id_query(self) -> str:
        return f"id={escape_data(self.DocumentId)}"

    @property
    def _doc_id_query(self) -> str:
        return f"docId={escape_data(self.DocumentId)}"

    def _transport(self) -> KkmTransport:
        self._http.Host = self.Host
        self._http.Port = self.Port
        self._http.UseHttps = self.UseHttps
        self._http.Token = self.Token
        self._http.TerminalId = self.TerminalId
        self._http.BasicAuthUser = self.AuthUserName
        self._http.BasicAuthPassword = self.AuthPassword
        self._http.Timeout = self.Timeout
        return self._http

    def _apply(self, result: ResponseResult) -> None:
        self.Ok = result.Success
        self.ErrorCode = result.Code
        self.ErrorDescription = result.Description or ""
        self.LastResult = result.Result
        self.FiscalResult = None

        self.FiscalSign = ""
        if isinstance(self.LastResult, str):
            self.DocumentId = ""
            if self.Ok and self.LastResult:
                self.DocumentId = self.LastResult
            return

        self._extract_fiscal_result(self.LastResult)

    def _extract_fiscal_result(self, result: Any) -> None:
        """Разбор Result: заполняет FiscalResult и плоские свойства."""
        if not isinstance(result, dict):
            return

        fiscal = self._read_value(FiscalResult, result)
        if fiscal is None:
            return

        has_fiscal = (
            bool(fiscal.FiscalSign)
            or fiscal.FiscalNumber > 0
            or fiscal.ShiftNumber > 0
            or bool(fiscal.DocId)
            or bool(fiscal.FnNumber)
            or bool(fiscal.RnNumber)
            or fiscal.CashSum is not None
            or fiscal.CashDrawer is not None
            or fiscal.Backlog is not None
            or fiscal.OutputParameters is not None
            or fiscal.ShiftState is not None
            or bool(fiscal.DateTime)
            or bool(fiscal.FiscalDateTime)
            or bool(fiscal.FnsUrl)
        )
        if not has_fiscal:
            return

        self.FiscalResult = fiscal

        if fiscal.DocId:
            self.DocumentId = fiscal.DocId
        if fiscal.ShiftNumber > 0:
            self.ShiftNumber = fiscal.ShiftNumber
        if fiscal.FiscalNumber > 0:
            self.CheckNumber = fiscal.FiscalNumber
        if fiscal.ShiftState is not None:
            self.CurrentShiftState = fiscal.ShiftState
        if fiscal.FnsUrl:
            self.FnsUrl = fiscal.FnsUrl
        if fiscal.FnNumber:
            self.FnNumber = fiscal.FnNumber
            self.IsFnPresent = True
        elif fiscal.FnNumber is not None:
            self.IsFnPresent = False
        if fiscal.RnNumber:
            self.RnNumber = fiscal.RnNumber
            self.IsFiscal = True
        elif fiscal.RnNumber is not None:
            self.IsFiscal = False
        if fiscal.FiscalSign:
            self.FiscalSign = fiscal.FiscalSign
        if fiscal.DateTime:
            self.ServerDateTime = fiscal.DateTime
        if fiscal.FiscalDateTime:
            self.FiscalDateTime = fiscal.FiscalDateTime
            self.DeviceDateTime = fiscal.FiscalDateTime

        if fiscal.CashDrawer is not None:
            self.CashBalance = fiscal.CashDrawer.Sum
        elif fiscal.CashSum is not None:
            self.CashBalance = fiscal.CashSum

        self._apply_backlog(fiscal.Backlog)
        self._apply_output_parameters(fiscal.OutputParameters)

    def _apply_backlog(self, backlog: Optional[Backlog]) -> None:
        if backlog is None:
            return

        self.BacklogDocumentsCount = backlog.DocumentsCounter
        if backlog.DocumentsCounter > 0:
            self.BacklogFirstDocumentNumber = backlog.DocumentFirstNumber
            if backlog.DocumentFirstDateTime != datetime.min:
                self.BacklogFirstDocumentDateTime = backlog.DocumentFirstDateTime
        else:
            self.BacklogFirstDocumentNumber = 0
            self.BacklogFirstDocumentDateTime = None

    def _apply_output_parameters(self, output: Optional[FiscalOutputParameters]) -> None:
        if output is None:
            return

        if output.NumberOfChecks > 0:
            self.CheckNumberInShift = output.NumberOfChecks
        if output.DateTime:
            self.FiscalDateTime = output.DateTime
            self.DeviceDateTime = output.DateTime
        if output.ShiftNumber > 0:
            self.ShiftNumber = output.ShiftNumber
        if output.CheckNumber > 0:
            self.CheckNumber = output.CheckNumber
        self.CashBalance = output.CashBalance
        if output.FnValidityDate:
            self.FnValidityDate = output.FnValidityDate
        if output.ResourcesFn > 0:
            self.FnDaysResources = output.ResourcesFn
        elif self.FnValidityDate:
            valid_until = json_codec.parse_datetime(self.FnValidityDate)
            if valid_until is not None:
                days = (valid_until.replace(tzinfo=None, hour=0, minute=0, second=0, microsecond=0) - today()).days
                self.FnDaysResources = 0 if days < 0 else days

        self._apply_backlog(output.Backlog)

        if output.FnWarnings is not None:
            self.FnWarnings = output.FnWarnings

    def _read_template_list(self) -> list[PrintTemplate]:
        if not isinstance(self.LastResult, list):
            return []

        result: list[PrintTemplate] = []
        for item in self.LastResult:
            if isinstance(item, str):
                result.append(PrintTemplate(Name=item))
            else:
                parsed = self._read_value(PrintTemplate, item)
                if parsed is not None:
                    result.append(parsed)
        return result

    def _read_value(self, target: type[T], value: Any) -> Optional[T]:
        try:
            parsed = json_codec.from_json(target, value)
        except (TypeError, ValueError):
            return None
        return parsed if isinstance(parsed, target) else None

    def _read_result(self, target: type[T]) -> Optional[T]:
        if self.LastResult is None:
            return None
        return self._read_value(target, self.LastResult)

    def _read_result_list(self, target: type[T]) -> list[T]:
        if not isinstance(self.LastResult, list):
            return []
        items = [self._read_value(target, item) for item in self.LastResult]
        return [item for item in items if item is not None]

    def _read_result_strings(self) -> list[str]:
        if not isinstance(self.LastResult, list):
            return []
        return [item for item in self.LastResult if isinstance(item, str)]

    def _apply_operation(self, operation: Optional[DeviceTaskInfo]) -> None:
        self.Operation = operation
        if operation is not None and operation.DocId:
            self.DocumentId = operation.DocId

    def _apply_document(self, document: Optional[CheckDocument]) -> None:
        self.Check = document
        if document is None:
            return

        if document.FiscalSign:
            self.FiscalSign = document.FiscalSign
        if document.DocNumber > 0:
            self.CheckNumber = document.DocNumber
        if document.ShiftNumber > 0:
            self.ShiftNumber = document.ShiftNumber
        if document.DocId:
            self.DocumentId = document.DocId
        if document.DocNumberInShift > 0:
            self.CheckNumberInShift = document.DocNumberInShift

        header = document.DocumentHeader
        if header is not None and header.Fn:
            self.FnNumber = header.Fn
            self.IsFnPresent = True
        if header is not None and header.RnNumber:
            self.RnNumber = header.RnNumber
            self.IsFiscal = True
        if header is not None and header.FnsUrl:
            self.FnsUrl = header.FnsUrl

        self.FiscalResult = FiscalResult(
            DateTime=document.Date.isoformat(),
            DeviceName=document.DeviceName,
            DocId=document.DocId,
            FnsUrl=header.FnsUrl if header is not None else None,
            FnNumber=header.Fn if header is not None else None,
            RnNumber=header.RnNumber if header is not None else None,
            FiscalDateTime=document.FiscalDate.strftime("%Y%m%d%H%M%S"),
            FiscalSign=document.FiscalSign,
            ShiftNumber=document.ShiftNumber,
            FiscalNumber=document.DocNumber,
        )
        if self.FiscalResult.DateTime:
            self.ServerDateTime = self.FiscalResult.DateTime
        if self.FiscalResult.FiscalDateTime:
            self.FiscalDateTime = self.FiscalResult.FiscalDateTime
            self.DeviceDateTime = self.FiscalResult.FiscalDateTime

    def _begin_call(self) -> CancelToken:
        token = CancelToken()
        with self._call_lock:
            self._call_cancel = token
        return token

    def _end_call(self, token: CancelToken) -> None:
        with self._call_lock:
            if self._call_cancel is token:
                self._call_cancel = None

    def _get(self, path: str, use_basic_auth: bool = False) -> None:
        token = self._begin_call()
        try:
            self._apply(self._transport().Get(path, use_basic_auth, token))
        finally:
            self._end_call(token)

    def _post(self, path: str, body: Any = None) -> None:
        token = self._begin_call()
        try:
            self._apply(self._transport().Post(path, body, token))
        finally:
            self._end_call(token)

    def _put(self, path: str, body: Any = None) -> None:
        token = self._begin_call()
        try:
            self._apply(self._transport().Put(path, body, token))
        finally:
            self._end_call(token)

    def _delete(self, path: str) -> None:
        token = self._begin_call()
        try:
            self._apply(self._transport().Delete(path, token))
        finally:
            self._end_call(token)

    def _date_query(self, date_from: datetime, date_to: datetime) -> str:
        return f"from={date_from:%Y-%m-%d}&to={date_to:%Y-%m-%d}"

    def _get_document_by_id(self, path: str) -> None:
        """GET документа по DocumentId."""
        self._get(f"{path}?{self._id_query}")
        self._apply_document(self._read_result(CheckDocument))

    def _get_check_list(self, path: str) -> None:
        """GET списка документов по кассе."""
        self._get(f"{path}?{self._device_query}")
        self.Checks = self._read_result_list(CheckDocument)

    def _get_report_list(self, path: str, extra_query: Optional[str] = None) -> None:
        """GET списка отчётов за период ShiftsFrom..ShiftsTo."""
        query = f"{self._device_query}&{self._date_query(self.ShiftsFrom, self.ShiftsTo)}"
        if extra_query and extra_query.strip():
            query += f"&{extra_query}"
        self._get(f"{path}?{query}")
        self.Shifts = self._read_result_list(ShiftListItem)


__all__ = ["SkkmConnectorInternals", "Decimal", "timedelta"]
