from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetTemplateList(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Рекламные чеки"
    Title = "Список шаблонов печати"
    SortOrder = 3

    def GetGetTemplateList(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.GetTemplateList()

        return kkm
