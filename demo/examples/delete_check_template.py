from __future__ import annotations

from demo.examples.sample import Sample
from rbsoftskkm import SkkmConnector


class DeleteCheckTemplate(Sample):
    GroupPath = "Работа с ККМ|Шаблоны чека"
    Title = "Удаление шаблона чека"

    def DeleteDeleteCheckTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.TemplateName = "sale_template_01"
        kkm.DeleteCheckTemplate()

        return kkm
