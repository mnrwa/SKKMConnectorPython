"""Сборка тел запросов из входных свойств коннектора."""

from __future__ import annotations

from typing import Iterable, Optional

from rbsoftskkm.core.skkm_connector_internals import SkkmConnectorInternals
from rbsoftskkm.data import slip_text_parser
from rbsoftskkm.data.contracts.admin_contracts import CheckTemplateDocumentRequest, CheckTemplateRequest
from rbsoftskkm.data.contracts.api_position import ApiPosition
from rbsoftskkm.data.contracts.cashdraw_parameters import CashdrawParameters
from rbsoftskkm.data.contracts.check_parameters import CheckParameters
from rbsoftskkm.data.contracts.checkbase_parameters import CheckbaseParameters
from rbsoftskkm.data.contracts.correction105_parameters import Correction105Parameters
from rbsoftskkm.data.contracts.correction120_parameters import Correction120Parameters
from rbsoftskkm.data.contracts.document_parameters import DocumentParameters
from rbsoftskkm.dto.positions.barcode_line import BarcodeLine
from rbsoftskkm.dto.positions.fiscal_line import FiscalLine
from rbsoftskkm.dto.positions.picture_line import PictureLine
from rbsoftskkm.dto.positions.position import Position
from rbsoftskkm.dto.positions.separator_line import SeparatorLine
from rbsoftskkm.dto.positions.text_line import TextLine
from rbsoftskkm.dto.templates.check_template_parameters import CheckTemplateParameters


class SkkmConnectorRequests(SkkmConnectorInternals):
    """Тела запросов: чек, коррекция, слип, наличные, шаблон чека."""

    def _fill_base(self, check: CheckbaseParameters) -> None:
        """Касса и кассир."""
        check.DeviceName = self.DeviceName
        check.Cashier = self.Cashier

    def _check_base(self) -> CheckbaseParameters:
        """Смена, X/Z-отчёт, отчёт о расчётах, денежный ящик."""
        check = CheckbaseParameters()
        self._fill_base(check)
        return check

    def _check_body(self) -> CheckParameters:
        """Обычный чек."""
        check = CheckParameters()
        self._fill_check(check)
        return check

    def _correction120_body(self) -> Correction120Parameters:
        """Чек коррекции ФФД 1.2."""
        check = Correction120Parameters(CorrectionData=self.CorrectionData)
        self._fill_check(check)
        return check

    def _fill_check(self, check: CheckParameters) -> None:
        """Заполнение полей чека."""
        self._fill_base(check)
        check.PaymentType = int(self.PaymentType)
        check.TaxVariant = int(self.TaxVariant)
        check.Customer = self.Customer
        check.SenderEmail = self.SenderEmail
        check.SaleAddress = self.SaleAddress
        check.SaleLocation = self.SaleLocation
        check.AgentSign = int(self.AgentSign) if self.AgentSign is not None else None
        check.AgentData = self.Agent
        check.Vendor = self.Vendor
        check.Positions = self._build_positions()
        check.Payments = self.Payments
        check.ElectronicPaymentInfo = None if not self.ElectronicPayments else list(self.ElectronicPayments)
        check.TextBefore = self.TextBefore
        check.TextAfter = self.TextAfter
        check.Electronically = self.Electronically
        check.OperationalAttribute = self.OperationalAttribute
        check.IndustryAttribute = self.IndustryAttribute
        check.UserAttribute = self.UserAttribute
        check.TimeZone = int(self.TimeZone) if self.TimeZone is not None else None
        check.OperationOnline = True if self.OperationOnline else None
        check.AdditionalAttribute = self.AdditionalAttribute

    def _correction105_body(self) -> Correction105Parameters:
        """Чек коррекции ФФД 1.05."""
        taxes = self.Correction105Taxes
        check = Correction105Parameters(
            CorrectionData=self.CorrectionData,
            PaymentType=int(self.PaymentType),
            TaxVariant=int(self.TaxVariant),
            Payments=self.Payments,
            SumTaxNone=taxes.SumTaxNone if taxes else None,
            SumTax0=taxes.SumTax0 if taxes else None,
            SumTax5=taxes.SumTax5 if taxes else None,
            SumTax7=taxes.SumTax7 if taxes else None,
            SumTax10=taxes.SumTax10 if taxes else None,
            SumTax105=taxes.SumTax105 if taxes else None,
            SumTax107=taxes.SumTax107 if taxes else None,
            SumTax110=taxes.SumTax110 if taxes else None,
            SumTax118=taxes.SumTax118 if taxes else None,
            SumTax18=taxes.SumTax18 if taxes else None,
            SumTax20=taxes.SumTax20 if taxes else None,
            SumTax120=taxes.SumTax120 if taxes else None,
            SumTax22=taxes.SumTax22 if taxes else None,
            SumTax122=taxes.SumTax122 if taxes else None,
            AdditionalAttribute=self.AdditionalAttribute,
        )
        self._fill_base(check)
        return check

    def _slip_body(self) -> DocumentParameters:
        """Слип."""
        check = DocumentParameters(Positions=slip_text_parser.Parse(self.TextForPrint))
        self._fill_base(check)
        return check

    def _cash_body(self) -> CashdrawParameters:
        """Внесение / выемка."""
        check = CashdrawParameters(Sum=self.CashAmount)
        self._fill_base(check)
        return check

    def _build_positions(self) -> list[ApiPosition]:
        """Позиции чека в модель запроса."""
        return self._to_api_positions(self.Positions)

    def _check_template_body(self) -> CheckTemplateRequest:
        """Тело POST/PUT checkTemplate: позиции в обёртке FiscalString, как у печати чека."""
        source = self.CheckTemplateParameters or CheckTemplateParameters()
        document = source.Document
        if document is None:
            return CheckTemplateRequest(Name=source.Name, Document=None)

        return CheckTemplateRequest(
            Name=source.Name,
            Document=CheckTemplateDocumentRequest(
                PaymentType=int(document.PaymentType),
                TaxVariant=int(document.TaxVariant),
                Customer=document.Customer,
                SenderEmail=document.SenderEmail if (document.SenderEmail or "").strip() else None,
                SaleAddress=document.SaleAddress if (document.SaleAddress or "").strip() else None,
                SaleLocation=document.SaleLocation if (document.SaleLocation or "").strip() else None,
                Positions=self._to_api_positions(document.Positions if document.Positions else self.Positions),
                Payments=document.Payments,
                ElectronicPaymentInfo=None
                if not document.ElectronicPayments
                else list(document.ElectronicPayments),
                Electronically=document.Electronically,
                OperationalAttribute=document.OperationalAttribute,
                IndustryAttribute=document.IndustryAttribute,
                UserAttribute=document.UserAttribute,
                TimeZone=int(document.TimeZone) if document.TimeZone is not None else None,
                OperationOnline=document.OperationOnline,
                AdditionalAttribute=document.AdditionalAttribute
                if (document.AdditionalAttribute or "").strip()
                else None,
                CorrectionData=document.CorrectionData,
            ),
        )

    def _to_api_positions(self, positions: Optional[Iterable[Position]]) -> list[ApiPosition]:
        if positions is None:
            return []
        return [self._to_api(position) for position in positions]

    def _to_api(self, position: Position) -> ApiPosition:
        """Одна позиция чека в модель запроса по её типу."""
        if isinstance(position, FiscalLine):
            return ApiPosition(FiscalString=position)
        if isinstance(position, TextLine):
            return self._text_to_api(position)
        if isinstance(position, BarcodeLine):
            return ApiPosition(Barcode=position)
        if isinstance(position, SeparatorLine):
            return ApiPosition(SeparatorLine=position)
        if isinstance(position, PictureLine):
            return ApiPosition(Picture=position)
        raise ValueError(
            f"Неизвестный тип позиции «{type(position).__name__}». "
            "Допустимы FiscalLine, TextLine, BarcodeLine, SeparatorLine, PictureLine."
        )

    def _text_to_api(self, text: TextLine) -> ApiPosition:
        """Текст с префиксом стиля линии ([dotted], [line], [line,dashed]) уходит как SeparatorLine."""
        parsed = slip_text_parser.ParseLine(text.Text, text.Font, text.Alignment)
        return ApiPosition(
            TextString=parsed.TextString,
            Barcode=parsed.Barcode,
            SeparatorLine=parsed.SeparatorLine,
            Picture=parsed.Picture,
        )
