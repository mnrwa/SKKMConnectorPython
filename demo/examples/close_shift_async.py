from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class CloseShiftAsync(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Асинхронное закрытие смены"
    SortOrder = 5

    def PostCloseShiftAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.CloseShiftAsync()

        return kkm
