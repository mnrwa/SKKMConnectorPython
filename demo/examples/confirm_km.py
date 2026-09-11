from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import KmConfirmationType, SkkmConnector


class ConfirmKM(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Подтвердить КМ"

    def PostConfirmKM(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.RequestKmGuid = "guid-из-проверки-КМ"
        kkm.ConfirmationType = KmConfirmationType.Included
        kkm.ConfirmKM()

        return kkm
