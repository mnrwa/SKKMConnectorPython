from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetQueue(Sample):
    GroupPath = "Работа с ККМ|Очередь"
    Title = "Состояние очереди"
    NeedDevice = False

    def GetGetQueue(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetQueue()

        return kkm
