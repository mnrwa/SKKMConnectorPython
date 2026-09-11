from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class GetTemplate(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Рекламные чеки"
    Title = "Получение шаблона печати"
    SortOrder = 4

    def GetGetTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.TemplateName = "Template32"
        kkm.GetTemplate()

        return kkm
