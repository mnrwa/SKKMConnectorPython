from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCashInList(Sample):
    GroupPath = "Работа с ККМ|Денежный ящик"
    Title = "Список внесений"
    SortOrder = 4

    def GetCashInListByDevice(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetCashInList()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
