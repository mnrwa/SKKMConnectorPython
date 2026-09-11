from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class ProcessingKMResult(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Результат ОИСМ"

    def GetProcessingKMResult(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetProcessingKMResult()

        return kkm
