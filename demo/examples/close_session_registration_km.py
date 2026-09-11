from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class CloseSessionRegistrationKM(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Закрыть сессию КМ"

    def PostCloseSessionRegistrationKM(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.CloseSessionRegistrationKM()

        return kkm
