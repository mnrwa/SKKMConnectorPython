from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckCorrection105List(Sample):
    GroupPath = "Работа с ККМ|Корректировочные чеки|Корректировки ФФД 1.0.5"
    Title = "Список чеков коррекции 1.0.5"

    def GetCheckCorrection105ListItems(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetCorrection105List()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
