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


class CheckSample44(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Возврат с дополнительным реквизитом"

    def PostCheckSample44(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.SaleReturn
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.AdditionalAttribute = "1352614355"

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("101"),
                Sum=Decimal("101.0"),
                Tax="0",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("101.0"))
        kkm.PrintCheck()

        return kkm
