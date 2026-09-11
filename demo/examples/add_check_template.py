from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    CheckTemplateDocument,
    CheckTemplateParameters,
    CheckType,
    FiscalLine,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class AddCheckTemplate(Sample):
    GroupPath = "Работа с ККМ|Шаблоны чека"
    Title = "Создание шаблона чека"

    def PostAddCheckTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.NewRequest()

        kkm.CheckTemplateParameters = CheckTemplateParameters(
            Name="sale_template_01",
            Document=CheckTemplateDocument(
                PaymentType=CheckType.Sale,
                TaxVariant=TaxSystem.ОСН,
                Payments=Payments(Cash=Decimal("101")),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар",
                Quantity=Decimal("1"),
                Price=Decimal("101"),
                Sum=Decimal("101"),
                Tax="0",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
            ),
        )

        kkm.AddCheckTemplate()

        return kkm
