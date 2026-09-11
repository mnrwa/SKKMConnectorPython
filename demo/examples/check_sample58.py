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


class CheckSample58(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Два одинаковых кода маркировки в двух позициях"

    def PostCheckSample58(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Сыр",
                Quantity=Decimal("0.2"),
                Price=Decimal("300"),
                Sum=Decimal("60.0"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="11",
                MeasureOfQuantity=MeasureOfQuantity.Kilogram,
                Marking=Marking(Code="MDEwNDYwMjIyMDAwNjU0OTIxNW9wRmNtSx05M2RHVno="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Сыр",
                Quantity=Decimal("0.15"),
                Price=Decimal("300"),
                Sum=Decimal("45.0"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="11",
                MeasureOfQuantity=MeasureOfQuantity.Kilogram,
                Marking=Marking(Code="MDEwNDYwMjIyMDAwNjU0OTIxNW9wRmNtSx05M2RHVno="),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("105.0"))
        kkm.PrintCheck()

        return kkm
