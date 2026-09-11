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


class CheckSample69(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Импортный маркированный подакцизный товар с таможенной декларацией"

    def PostCheckSample69(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Коньяк 0.5л.",
                Quantity=Decimal("1"),
                Price=Decimal("2480"),
                Sum=Decimal("2480.0"),
                Tax="20",
                TaxSum=Decimal("413.33"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.АТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                ExciseAmount=Decimal("185.4"),
                CountryOfOrigin="276",
                CustomsDeclaration="10009100/140923/0001122",
                Marking=Marking(Code="MDEwNDYwNzAxMDM1MDI0NjIxNURzPkpSak5FIWpaIR05M2RHVno="),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("2480.0"))
        kkm.PrintCheck()

        return kkm
