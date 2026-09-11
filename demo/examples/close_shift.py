from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class CloseShift(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Закрыть смену"
    SortOrder = 4

    def PostCloseShift(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.CloseShift()

        return kkm
