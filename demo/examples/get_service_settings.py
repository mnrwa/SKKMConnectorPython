from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetServiceSettings(Sample):
    GroupPath = "Администрирование|Служба"
    Title = "Получение настроек службы"
    SortOrder = 0

    def GetGetServiceSettings(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetServiceSettings()

        return kkm
