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


class CheckSample49(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Подакцизный товар с указанием суммы акциза."

    def PostCheckSample49(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Сигареты",
                Quantity=Decimal("1"),
                Price=Decimal("200"),
                Sum=Decimal("200.0"),
                Tax="20",
                TaxSum=Decimal("33.33"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ExcisableGoods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                ExciseAmount=Decimal("48.5"),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("200.0"))
        kkm.PrintCheck()

        return kkm
