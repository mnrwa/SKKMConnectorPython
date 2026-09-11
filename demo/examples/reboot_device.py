from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class RebootDevice(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Перезапуск ККТ"
    SortOrder = 10

    def PostRebootDevice(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.RebootDevice()

        return kkm
