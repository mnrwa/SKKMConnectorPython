from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetSlipList(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки"
    Title = "Список нефискальных документов"
    SortOrder = 2

    def GetGetSlipList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetSlipList()

        return kkm
