from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, PictureAlignment, SkkmConnector


class SendPicture(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Работа с картинками"
    Title = "Загрузить картинку"
    SortOrder = 0

    def PostSendPicture(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.PictureName = "demo.png"
        kkm.PictureAlignment = PictureAlignment.Center
        kkm.PictureBase64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
        kkm.SendPicture()

        return kkm
