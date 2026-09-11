from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckTimeZone,
    CheckType,
    Customer,
    FiscalLine,
    Industry,
    MeasureOfQuantity,
    OperationalAttribute,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
    UserAttribute,
)


class CheckSample39(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Электронный чек"

    def PostCheckSample39(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.TimeZone = CheckTimeZone.Msk
        kkm.Electronically = True
        kkm.OperationOnline = True
        kkm.SenderEmail = "ivanov@mail.ru"
        kkm.SaleAddress = "г. Москва, ул. Ленина, д. 1"
        kkm.SaleLocation = "https://shop.ru"
        kkm.AdditionalAttribute = "6702704322"
        kkm.TextBefore = "Текст до товаров"
        kkm.TextAfter = "Текст после товаров"

        kkm.Customer = Customer(
            Info="Иванов И. И.",
            Vatin="500100732259",
            Email="ivanov@mail.ru",
            Phone="+79001234567",
            DateOfBirth="01.01.1990",
            Citizenship="643",
            DocumentTypeCode="21",
            DocumentData="4509 123456",
            Address="г. Москва, ул. Ленина, д. 1",
        )

        kkm.IndustryAttribute = Industry(
            IdentifierFoiv="030",
            DocumentDate="21.11.2023",
            DocumentNumber="1944",
            AttributeValue="UUID=8f3a9d1c-7e2b-4a5f-9c8d-1e2f3a4b5c6d&Time=1746530733410",
        )

        kkm.UserAttribute = UserAttribute(Name="НомерЗаказа", Value="42")

        kkm.OperationalAttribute = OperationalAttribute(
            DateTime="03.07.2026",
            OperationId=1,
            OperationData="Оплата по договору",
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Услуга",
                Quantity=Decimal("1"),
                Price=Decimal("250"),
                Sum=Decimal("250.0"),
                Tax="20",
                TaxSum=Decimal("41.67"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Service,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("250.0"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
