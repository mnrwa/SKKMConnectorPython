from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class ChecksByShift(Sample):
    GroupPath = "Работа с ККМ|Печать чеков"
    Title = "Чеки за смену"
    SortOrder = 7

    def GetChecksByShift(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.ShiftNumber = 1
        kkm.GetChecksByShift()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
