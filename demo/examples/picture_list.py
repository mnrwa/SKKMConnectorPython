from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class PictureList(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Работа с картинками"
    Title = "Список картинок"
    SortOrder = 2

    def GetPictureList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.GetPictureList()

        return kkm
