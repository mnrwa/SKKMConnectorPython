from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class CashOutAsync(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Асинхронная выемка наличных"
    SortOrder = 7

    def PostCashOutAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.CashAmount = Decimal("500")
        kkm.CashOutAsync()

        return kkm
