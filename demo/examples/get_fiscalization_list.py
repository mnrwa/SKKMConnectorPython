from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetFiscalizationList(Sample):
    GroupPath = "Работа с ККМ|Фискализация"
    Title = "Список фискализаций"
    SortOrder = 3

    def GetGetFiscalizationList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetFiscalizationList()

        return kkm
