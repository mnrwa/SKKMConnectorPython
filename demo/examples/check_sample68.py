from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    FiscalLine,
    Marking,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample68(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Маркированный товар без указания типа маркировки"

    def PostCheckSample68(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("101"),
                Sum=Decimal("101.0"),
                Tax="0",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(
                    Gtin="04670540176099",
                    Code="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno=",
                ),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("101.0"))
        kkm.PrintCheck()

        return kkm
