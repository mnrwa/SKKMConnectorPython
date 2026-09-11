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


class CheckSample12(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Все ставки НДС"

    def PostCheckSample12(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Товар без НДС",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 0%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="0",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 5%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="5",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 5/105",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="5/105",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 7%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="7",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 7/107",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="7/107",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 10%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="10",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 10/110",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="10/110",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 18%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="18",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 18/118",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="18/118",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 20%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="20",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 20/120",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="20/120",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 22%",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="22",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Товар НДС 22/122",
                Quantity=Decimal("1"),
                Price=Decimal("100"),
                Sum=Decimal("100.0"),
                Tax="22/122",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("1400.0"))
        kkm.PrintCheck()

        return kkm
