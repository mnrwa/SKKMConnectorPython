from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, CheckType, FiscalLine, Payments, SkkmConnector, TaxSystem


class PrintCheck(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Печать чека"
    SortOrder = 0

    def PostPrintCheck(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Кофе американо",
                Quantity=Decimal("1"),
                Price=Decimal("150"),
                Sum=Decimal("150"),
                Tax="20",
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("150"))
        kkm.PrintCheck()

        return kkm
