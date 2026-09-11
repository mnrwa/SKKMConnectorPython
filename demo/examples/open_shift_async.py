from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class OpenShiftAsync(Sample):
    GroupPath = "Работа с ККМ|Кассовые смены"
    Title = "Открыть смену (async)"
    SortOrder = 3

    def PostOpenShiftAsync(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.OpenShiftAsync()

        return kkm
