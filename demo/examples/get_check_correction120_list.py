from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckCorrection120List(Sample):
    GroupPath = "Работа с ККМ|Корректировочные чеки|Корректировки ФФД 1.2"
    Title = "Список чеков коррекции 1.2"

    def GetCheckCorrection120ListItems(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetCorrection120List()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
