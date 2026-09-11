from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import Cashier, SkkmConnector


class PrintSlip(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки"
    Title = "Печать нефискального документа"
    SortOrder = 0

    def PostPrintSlip(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)

        kkm.TextForPrint = (
            "[center,bold]РБ-Софт: Сервер ККМ\n"
            "[center]Нефискальный документ\n"
            "[line]\n"
            "Обычная строка текста\n"
            "[QR,center]https://www.rbsoft.ru\n"
            "[center,small]Спасибо за покупку!"
        )

        kkm.PrintSlip()

        return kkm
