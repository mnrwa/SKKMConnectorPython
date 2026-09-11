from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample30(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Позиция с акцизом, страной происхождения, таможенной декларацией и скидкой"

    def PostCheckSample30(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Сигареты",
                ProductCode="2402 20 900 0",
                Quantity=Decimal("2"),
                Price=Decimal("50"),
                Sum=Decimal("90"),
                DiscountSum=Decimal("10"),
                Department=1,
                Tax="20",
                TaxSum=Decimal("15"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ExcisableGoods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                ExciseAmount=Decimal("5.5"),
                CountryOfOrigin="643",
                CustomsDeclaration="10009100/220211/0001122",
                AdditionalAttribute="Доп. реквизит",
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("90.0"))
        kkm.PrintCheck()

        return kkm
