from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetPoolList(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Список пулов"
    SortOrder = 12

    def GetGetPoolList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetPoolList()

        return kkm
