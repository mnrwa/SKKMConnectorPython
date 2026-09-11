from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class LineLength(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Ширина строки"
    SortOrder = 6

    def GetLineLength(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetLineLength()

        return kkm
