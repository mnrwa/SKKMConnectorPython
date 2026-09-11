from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    FiscalLine,
    FractionalQuantity,
    Marking,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample57(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Цена ниже МРЦ"

    def PostCheckSample57(self) -> SkkmConnector:
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
                Price=Decimal("80"),
                Sum=Decimal("80.0"),
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYyOTMwODg3NzA0NDIxRHprY1l0Mh04MDA1MDkwMDAwHTkzZEdWeg=="),
                Fractional=FractionalQuantity(Numerator=1, Denominator=2),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("80.0"))
        kkm.PrintCheck()

        return kkm
