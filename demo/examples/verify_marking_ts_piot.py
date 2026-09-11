from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class VerifyMarkingTsPiot(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Проверка КМ через ТС ПИоТ"

    def PostVerifyMarkingTsPiot(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.MarkingCodes.clear()
        kkm.MarkingCodes.append("MDEwNDY3MDU0MDE3NjA5OTIxNSdXOVVtHTkzZEdWeg==")
        kkm.VerifyMarkingTsPiot()

        return kkm
