from __future__ import annotations

from datetime import date, datetime, time
from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    Correction105Taxes,
    CorrectionData,
    CorrectionTypes,
    FiscalLine,
    Payments,
    SkkmConnector,
    TaxSystem,
)


class PrintCheckCorrection105(Sample):
    GroupPath = "Работа с ККМ|Корректировочные чеки|Корректировки ФФД 1.0.5"
    Title = "Печать чека коррекции 1.0.5"

    def PostPrintCheckCorrection105(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.CorrectionSale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.CorrectionData = CorrectionData(
            Type=CorrectionTypes.Самостоятельно,
            Description="Основание коррекции",
            Date=datetime.combine(date.today(), time.min),
        )

        kkm.Correction105Taxes = Correction105Taxes(SumTax20=Decimal("16.67"))

        kkm.Positions.append(
            FiscalLine(
                Name="Товар по коррекции 1.05",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100"),
                Tax="20",
                TaxSum=Decimal("16.67"),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("100"))
        kkm.PrintCheckCorrection105()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
