from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class DeletePicture(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Работа с картинками"
    Title = "Удаление изображения"
    SortOrder = 3

    def DeleteDeletePicture(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.PictureId = "demo.bmp"
        kkm.DeletePicture()

        return kkm
