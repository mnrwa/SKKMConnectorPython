from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetPicture(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Работа с картинками"
    Title = "Получение изображения"
    SortOrder = 1

    def GetGetPicture(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.PictureId = "demo.bmp"
        kkm.GetPicture()

        return kkm
