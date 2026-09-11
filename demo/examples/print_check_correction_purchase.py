from __future__ import annotations

from datetime import date, datetime, time
from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    CorrectionData,
    CorrectionTypes,
    FiscalLine,
    Payments,
    SkkmConnector,
    TaxSystem,
)


class PrintCheckCorrectionPurchase(Sample):
    GroupPath = "Работа с ККМ|Корректировочные чеки|Корректировки ФФД 1.2"
    Title = "Коррекция расхода 1.2"

    def PostPrintCheckCorrectionPurchase(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.CorrectionPurchase
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.CorrectionData = CorrectionData(
            Type=CorrectionTypes.Самостоятельно,
            Description="Коррекция расхода",
            Date=datetime.combine(date.today(), time.min),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар по коррекции расхода",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100"),
                Tax="20",
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("100"))
        kkm.PrintCheckCorrection120()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
