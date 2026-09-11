from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class OpenSessionRegistrationKM(Sample):
    GroupPath = "Работа с ККМ|Работа с маркировкой"
    Title = "Открыть сессию КМ"

    def PostOpenSessionRegistrationKM(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.OpenSessionRegistrationKM()

        return kkm
