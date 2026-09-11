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


class CheckSample56(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "512 некорректный код маркировки - Код маркировки заблокирован по постановлению"

    def PostCheckSample56(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Сыр",
                Quantity=Decimal("0.353"),
                Price=Decimal("200"),
                Sum=Decimal("70.6"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasurementUnit="11",
                MeasureOfQuantity=MeasureOfQuantity.Kilogram,
                Marking=Marking(Code="MDEwNDYwMjIyMDAwNjU0OTIxNW9wRmNtSx05M2RHVno="),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("70.6"))
        kkm.PrintCheck()

        return kkm
