from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    AgentType,
    BarcodeLine,
    Cashier,
    CheckTimeZone,
    CheckType,
    Customer,
    ElectronicPayment,
    ElectronicPaymentMethod,
    FiscalLine,
    FractionalQuantity,
    Industry,
    LineStyle,
    Marking,
    MeasureOfQuantity,
    OperationalAttribute,
    Payments,
    PictureAlignment,
    PictureLine,
    SeparatorLine,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
    TextLine,
    UserAttribute,
    Vendor,
)


class CheckSample64(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Комплексный чек: заголовочные реквизиты и атрибуты"

    def PostCheckSample64(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.TimeZone = CheckTimeZone.MskPlus5
        kkm.Electronically = True
        kkm.OperationOnline = True
        kkm.SenderEmail = "ivanov@mail.ru"
        kkm.SaleAddress = "г. Москва, ул. Ленина, д. 1"
        kkm.SaleLocation = "https://shop.ru"
        kkm.AdditionalAttribute = "fp-src"
        kkm.TextBefore = "before"
        kkm.TextAfter = "after"

        kkm.Customer = Customer(
            Info="ООО Ромашка",
            Vatin="7701234560",
            Email="ivanov@mail.ru",
            Phone="+79001234567",
        )

        kkm.IndustryAttribute = Industry(
            IdentifierFoiv="030",
            DocumentDate="21.11.2023",
            DocumentNumber="1944",
            AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
        )

        kkm.UserAttribute = UserAttribute(Name="НомерЗаказа", Value="42")

        kkm.OperationalAttribute = OperationalAttribute(
            DateTime="19.08.2026",
            OperationId=42,
            OperationData="Оплата по договору",
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("100"),
                PaymentMethod=ElectronicPaymentMethod.FullPayment,
                Identifiers="RRN=1",
                AdditionalInformation="Карта *1234",
            ),
        )

        kkm.Positions.append(TextLine(Text="Комплексный чек", Font="Big", Alignment="center"))

        kkm.Positions.append(
            FiscalLine(
                Name="Сыр",
                Quantity=Decimal("0.5"),
                Price=Decimal("200"),
                Sum=Decimal("100"),
                Tax="10",
                TaxSum=Decimal("9.09"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="11",
                MeasureOfQuantity=MeasureOfQuantity.Kilogram,
                AgentSign=AgentType.Agent,
                Vendor=Vendor(Name="ООО Ромашка", Phones=["+79001234567"], Vatin="7701234560"),
                Marking=Marking(Code="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno="),
                Industry=Industry(
                    IdentifierFoiv="030",
                    DocumentDate="21.11.2023",
                    DocumentNumber="1944",
                    AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
                ),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("80"),
                Sum=Decimal("80"),
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Fractional=FractionalQuantity(Numerator=1, Denominator=4),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("2"),
                Price=Decimal("15"),
                Sum=Decimal("30"),
                Tax="22",
                TaxSum=Decimal("5.41"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(BarcodeLine(Type="QR", Barcode="https://shop.ru", Alignment="center"))

        kkm.Positions.append(
            PictureLine(
                Value="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
                Alignment=PictureAlignment.Right,
            ),
        )

        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Double))

        kkm.Payments = Payments(
            Cash=Decimal("50"),
            ElectronicPayment=Decimal("100"),
            AdvancePayment=Decimal("50"),
            Credit=Decimal("80"),
            CashProvision=Decimal("65"),
        )

        kkm.PrintCheck()
        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
