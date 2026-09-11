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


class UpdateCheckTemplate(Sample):
    GroupPath = "Работа с ККМ|Шаблоны чека"
    Title = "Изменение шаблона чека"

    def PutUpdateCheckTemplate(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.NewRequest()

        kkm.CheckTemplateParameters = CheckTemplateParameters(
            Name="sale_template_01",
            Document=CheckTemplateDocument(
                PaymentType=CheckType.Sale,
                TaxVariant=TaxSystem.ОСН,
                Payments=Payments(Cash=Decimal("12")),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар1",
                Quantity=Decimal("1"),
                Price=Decimal("12"),
                Sum=Decimal("12"),
                Tax="0",
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
            ),
        )

        kkm.UpdateCheckTemplate()

        return kkm
