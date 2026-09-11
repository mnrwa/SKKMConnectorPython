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


class CheckSample53(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Частичная оплата чека"

    def PostCheckSample53(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPaymentAndCredit,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("40"), Credit=Decimal("60"))
        kkm.PrintCheck()

        return kkm
