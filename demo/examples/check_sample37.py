from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample37(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Все значения мер количества"

    def PostCheckSample37(self) -> SkkmConnector:
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
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Сахар 500г.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="10",
                MeasureOfQuantity=MeasureOfQuantity.Gram,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Мука 0.5кг.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="11",
                MeasureOfQuantity=MeasureOfQuantity.Kilogram,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Песок 0.5т.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="12",
                MeasureOfQuantity=MeasureOfQuantity.Tonne,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Ткань 0.5см.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="20",
                MeasureOfQuantity=MeasureOfQuantity.Centimeter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Ткань 0.5дм.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="21",
                MeasureOfQuantity=MeasureOfQuantity.Decimeter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Ткань 0.5м.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="22",
                MeasureOfQuantity=MeasureOfQuantity.Meter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Плитка 0.5кв.см",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="30",
                MeasureOfQuantity=MeasureOfQuantity.SquareCentimeter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Плитка 0.5кв.дм",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="31",
                MeasureOfQuantity=MeasureOfQuantity.SquareDecimeter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Плитка 0.5кв.м",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="32",
                MeasureOfQuantity=MeasureOfQuantity.SquareMeter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Масло 0.5мл.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="40",
                MeasureOfQuantity=MeasureOfQuantity.Milliliter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 0.5л.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="41",
                MeasureOfQuantity=MeasureOfQuantity.Liter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Газ 0.5м3",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="42",
                MeasureOfQuantity=MeasureOfQuantity.CubicMeter,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Электроэнергия",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="50",
                MeasureOfQuantity=MeasureOfQuantity.KilowattHour,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Тепло",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="51",
                MeasureOfQuantity=MeasureOfQuantity.Gigacalorie,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Аренда, сутки",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="70",
                MeasureOfQuantity=MeasureOfQuantity.Day,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Аренда, час",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="71",
                MeasureOfQuantity=MeasureOfQuantity.Hour,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Аренда, мин.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="72",
                MeasureOfQuantity=MeasureOfQuantity.Minute,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Аренда, сек.",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="73",
                MeasureOfQuantity=MeasureOfQuantity.Second,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Файл, КБ",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="80",
                MeasureOfQuantity=MeasureOfQuantity.Kilobyte,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Файл, МБ",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="81",
                MeasureOfQuantity=MeasureOfQuantity.Megabyte,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Файл, ГБ",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="82",
                MeasureOfQuantity=MeasureOfQuantity.Gigabyte,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Файл, ТБ",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="83",
                MeasureOfQuantity=MeasureOfQuantity.Terabyte,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Прочее",
                Quantity=Decimal("0.5"),
                Price=Decimal("10"),
                Sum=Decimal("5.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasurementUnit="255",
                MeasureOfQuantity=MeasureOfQuantity.Other,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("125.0"))
        kkm.PrintCheck()

        return kkm
