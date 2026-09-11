from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class OpenShift(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Открыть смену"
    SortOrder = 0

    def PostOpenShift(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.OpenShift()

        return kkm
