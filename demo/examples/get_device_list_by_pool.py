from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetDeviceListByPool(Sample):
    GroupPath = "Администрирование|ККТ"
    Title = "Список ККТ по пулу"
    SortOrder = 1

    def GetGetDeviceListByPool(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.PoolName = "pool"
        kkm.GetDeviceListByPool()

        return kkm
