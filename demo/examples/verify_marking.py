from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class VerifyMarking(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Проверка КМ (verify)"

    def PostVerifyMarking(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.MarkingCodes.clear()
        kkm.MarkingCodes.append("0104670540176099215'W9Um93dGVz")
        kkm.VerifyMarking()

        return kkm
