from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class PrintCheckCopy(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Копия последнего чека"
    SortOrder = 2

    def PostPrintCheckCopy(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)

        # пустой FiscalSign — копия последнего чека
        kkm.PrintCheckCopy()

        return kkm
