from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    BarcodeLine,
    Cashier,
    CheckType,
    FiscalLine,
    LineStyle,
    MeasureOfQuantity,
    Payments,
    PictureAlignment,
    PictureLine,
    SeparatorLine,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
    TextLine,
)


class CheckSample42(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Чек с нефискальными строками"

    def PostCheckSample42(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.Positions.append(TextLine(Text="Заголовок чека", Font="H1", Alignment="center"))
        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Solid))

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("50"),
                Sum=Decimal("50.0"),
                Tax="20",
                TaxSum=Decimal("8.33"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(TextLine(Text="Спасибо за покупку", Font="Small", Alignment="center"))

        kkm.Positions.append(
            BarcodeLine(Type="QR", Barcode="https://shop.ru/loyalty", Alignment="center"),
        )

        kkm.Positions.append(BarcodeLine(Type="EAN13", Barcode="4601234567890", Alignment="left"))

        kkm.Positions.append(
            PictureLine(
                Value="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
                Alignment=PictureAlignment.Center,
                Width=1,
                Height=1,
            ),
        )

        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Bold))
        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Dashed))
        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Dotted))
        kkm.Positions.append(SeparatorLine(LineStyle=LineStyle.Double))
        kkm.Positions.append(TextLine(Text="https://nalog.gov.ru"))
        kkm.Payments = Payments(Cash=Decimal("50.0"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
