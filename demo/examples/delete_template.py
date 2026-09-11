from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class DeleteTemplate(Sample):
    GroupPath = "Работа с ККМ|Нефискальные чеки|Рекламные чеки"
    Title = "Удаление шаблона печати"
    SortOrder = 2

    def DeleteDeleteTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.TemplateName = "name1221212121220"
        kkm.DeleteTemplate()

        return kkm
