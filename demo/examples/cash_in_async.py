from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class CashInAsync(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Асинхронное внесение наличных"
    SortOrder = 3

    def PostCashInAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.CashAmount = Decimal("1000")
        kkm.CashInAsync()

        return kkm
