from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    FiscalLine,
    Marking,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample62(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "128 маркированных позиций"

    def PostCheckSample62(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwMDIxUzAwMDIwMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwMTIxUzAwMDIwMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwMjIxUzAwMDIwMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwMzIxUzAwMDIwMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwNDIxUzAwMDIwNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwNTIxUzAwMDIwNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwNjIxUzAwMDIwNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwNzIxUzAwMDIwNx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwODIxUzAwMDIwOB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIwOTIxUzAwMDIwOR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxMDIxUzAwMDIxMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxMTIxUzAwMDIxMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxMjIxUzAwMDIxMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxMzIxUzAwMDIxMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxNDIxUzAwMDIxNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxNTIxUzAwMDIxNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxNjIxUzAwMDIxNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxNzIxUzAwMDIxNx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxODIxUzAwMDIxOB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIxOTIxUzAwMDIxOR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyMDIxUzAwMDIyMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyMTIxUzAwMDIyMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyMjIxUzAwMDIyMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyMzIxUzAwMDIyMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyNDIxUzAwMDIyNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyNTIxUzAwMDIyNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyNjIxUzAwMDIyNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyNzIxUzAwMDIyNx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyODIxUzAwMDIyOB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIyOTIxUzAwMDIyOR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzMDIxUzAwMDIzMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzMTIxUzAwMDIzMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzMjIxUzAwMDIzMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzMzIxUzAwMDIzMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzNDIxUzAwMDIzNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzNTIxUzAwMDIzNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzNjIxUzAwMDIzNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzNzIxUzAwMDIzNx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzODIxUzAwMDIzOB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDIzOTIxUzAwMDIzOR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0MDIxUzAwMDI0MB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0MTIxUzAwMDI0MR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0MjIxUzAwMDI0Mh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0MzIxUzAwMDI0Mx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0NDIxUzAwMDI0NB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0NTIxUzAwMDI0NR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0NjIxUzAwMDI0Nh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0NzIxUzAwMDI0Nx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0ODIxUzAwMDI0OB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI0OTIxUzAwMDI0OR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1MDIxUzAwMDI1MB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1MTIxUzAwMDI1MR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1MjIxUzAwMDI1Mh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1MzIxUzAwMDI1Mx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1NDIxUzAwMDI1NB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1NTIxUzAwMDI1NR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1NjIxUzAwMDI1Nh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1NzIxUzAwMDI1Nx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1ODIxUzAwMDI1OB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI1OTIxUzAwMDI1OR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2MDIxUzAwMDI2MB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2MTIxUzAwMDI2MR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2MjIxUzAwMDI2Mh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2MzIxUzAwMDI2Mx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2NDIxUzAwMDI2NB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2NTIxUzAwMDI2NR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2NjIxUzAwMDI2Nh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2NzIxUzAwMDI2Nx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2ODIxUzAwMDI2OB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI2OTIxUzAwMDI2OR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3MDIxUzAwMDI3MB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3MTIxUzAwMDI3MR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3MjIxUzAwMDI3Mh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3MzIxUzAwMDI3Mx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3NDIxUzAwMDI3NB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3NTIxUzAwMDI3NR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3NjIxUzAwMDI3Nh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3NzIxUzAwMDI3Nx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3ODIxUzAwMDI3OB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI3OTIxUzAwMDI3OR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4MDIxUzAwMDI4MB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4MTIxUzAwMDI4MR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4MjIxUzAwMDI4Mh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4MzIxUzAwMDI4Mx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4NDIxUzAwMDI4NB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4NTIxUzAwMDI4NR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4NjIxUzAwMDI4Nh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4NzIxUzAwMDI4Nx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4ODIxUzAwMDI4OB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI4OTIxUzAwMDI4OR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5MDIxUzAwMDI5MB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5MTIxUzAwMDI5MR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5MjIxUzAwMDI5Mh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5MzIxUzAwMDI5Mx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5NDIxUzAwMDI5NB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5NTIxUzAwMDI5NR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5NjIxUzAwMDI5Nh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5NzIxUzAwMDI5Nx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5ODIxUzAwMDI5OB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDI5OTIxUzAwMDI5OR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwMDIxUzAwMDMwMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwMTIxUzAwMDMwMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwMjIxUzAwMDMwMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwMzIxUzAwMDMwMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwNDIxUzAwMDMwNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwNTIxUzAwMDMwNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwNjIxUzAwMDMwNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwNzIxUzAwMDMwNx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwODIxUzAwMDMwOB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMwOTIxUzAwMDMwOR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxMDIxUzAwMDMxMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxMTIxUzAwMDMxMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxMjIxUzAwMDMxMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxMzIxUzAwMDMxMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxNDIxUzAwMDMxNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxNTIxUzAwMDMxNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxNjIxUzAwMDMxNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxNzIxUzAwMDMxNx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxODIxUzAwMDMxOB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMxOTIxUzAwMDMxOR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyMDIxUzAwMDMyMB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyMTIxUzAwMDMyMR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyMjIxUzAwMDMyMh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyMzIxUzAwMDMyMx05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyNDIxUzAwMDMyNB05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyNTIxUzAwMDMyNR05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyNjIxUzAwMDMyNh05M1RFU1Q="),
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Молоко 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDMyNzIxUzAwMDMyNx05M1RFU1Q="),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("128.0"))
        kkm.PrintCheck()

        return kkm
