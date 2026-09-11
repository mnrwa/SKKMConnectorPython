from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetCheckTemplateList(Sample):
    GroupPath = "Работа с ККМ|Шаблоны чека"
    Title = "Список шаблонов чека"

    def GetGetCheckTemplateList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetCheckTemplateList()

        return kkm
