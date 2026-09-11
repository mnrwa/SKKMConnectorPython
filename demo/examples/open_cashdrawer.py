from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class OpenCashdrawer(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Открыть ящик"
    SortOrder = 0

    def PostOpenCashdrawer(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.OpenCashdrawer()

        return kkm
