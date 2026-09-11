from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    BarcodeLine,
    Cashier,
    CheckType,
    FiscalLine,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample40(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Все виды штрихкода"

    def PostCheckSample40(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="шт",
            ),
        )

        kkm.Positions.append(
            BarcodeLine(Type="QR", Barcode="https://shop.ru/check", Alignment="center"),
        )

        kkm.Positions.append(BarcodeLine(Type="EAN13", Barcode="4601234567893", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="EAN8", Barcode="96385074", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="CODE128", Barcode="ABC-12345", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="CODE39", Barcode="CODE39-TEST", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="CODE93", Barcode="CODE93", Alignment="center"))

        kkm.Positions.append(
            BarcodeLine(Type="PDF417", Barcode="pdf417-payload", Alignment="center"),
        )

        kkm.Positions.append(BarcodeLine(Type="UPCA", Barcode="012345678905", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="UPCE", Barcode="04252614", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="ITF", Barcode="1234567890", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="CODABAR", Barcode="A123456A", Alignment="center"))
        kkm.Positions.append(BarcodeLine(Type="CODE32", Barcode="01234567", Alignment="center"))
        kkm.Payments = Payments(Cash=Decimal("10.0"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
