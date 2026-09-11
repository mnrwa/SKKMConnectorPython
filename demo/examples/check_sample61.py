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


class CheckSample61(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "100 маркированных позиций"

    def PostCheckSample61(self) -> SkkmConnector:
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwMTIxUzAwMDAwMR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwMjIxUzAwMDAwMh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwMzIxUzAwMDAwMx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwNDIxUzAwMDAwNB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwNTIxUzAwMDAwNR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwNjIxUzAwMDAwNh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwNzIxUzAwMDAwNx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwODIxUzAwMDAwOB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAwOTIxUzAwMDAwOR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxMDIxUzAwMDAxMB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxMTIxUzAwMDAxMR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxMjIxUzAwMDAxMh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxMzIxUzAwMDAxMx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxNDIxUzAwMDAxNB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxNTIxUzAwMDAxNR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxNjIxUzAwMDAxNh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxNzIxUzAwMDAxNx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxODIxUzAwMDAxOB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAxOTIxUzAwMDAxOR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyMDIxUzAwMDAyMB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyMTIxUzAwMDAyMR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyMjIxUzAwMDAyMh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyMzIxUzAwMDAyMx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyNDIxUzAwMDAyNB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyNTIxUzAwMDAyNR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyNjIxUzAwMDAyNh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyNzIxUzAwMDAyNx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyODIxUzAwMDAyOB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAyOTIxUzAwMDAyOR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzMDIxUzAwMDAzMB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzMTIxUzAwMDAzMR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzMjIxUzAwMDAzMh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzMzIxUzAwMDAzMx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzNDIxUzAwMDAzNB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzNTIxUzAwMDAzNR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzNjIxUzAwMDAzNh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzNzIxUzAwMDAzNx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzODIxUzAwMDAzOB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDAzOTIxUzAwMDAzOR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0MDIxUzAwMDA0MB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0MTIxUzAwMDA0MR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0MjIxUzAwMDA0Mh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0MzIxUzAwMDA0Mx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0NDIxUzAwMDA0NB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0NTIxUzAwMDA0NR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0NjIxUzAwMDA0Nh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0NzIxUzAwMDA0Nx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0ODIxUzAwMDA0OB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA0OTIxUzAwMDA0OR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1MDIxUzAwMDA1MB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1MTIxUzAwMDA1MR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1MjIxUzAwMDA1Mh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1MzIxUzAwMDA1Mx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1NDIxUzAwMDA1NB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1NTIxUzAwMDA1NR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1NjIxUzAwMDA1Nh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1NzIxUzAwMDA1Nx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1ODIxUzAwMDA1OB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA1OTIxUzAwMDA1OR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2MDIxUzAwMDA2MB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2MTIxUzAwMDA2MR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2MjIxUzAwMDA2Mh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2MzIxUzAwMDA2Mx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2NDIxUzAwMDA2NB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2NTIxUzAwMDA2NR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2NjIxUzAwMDA2Nh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2NzIxUzAwMDA2Nx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2ODIxUzAwMDA2OB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA2OTIxUzAwMDA2OR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3MDIxUzAwMDA3MB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3MTIxUzAwMDA3MR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3MjIxUzAwMDA3Mh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3MzIxUzAwMDA3Mx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3NDIxUzAwMDA3NB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3NTIxUzAwMDA3NR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3NjIxUzAwMDA3Nh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3NzIxUzAwMDA3Nx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3ODIxUzAwMDA3OB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA3OTIxUzAwMDA3OR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4MDIxUzAwMDA4MB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4MTIxUzAwMDA4MR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4MjIxUzAwMDA4Mh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4MzIxUzAwMDA4Mx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4NDIxUzAwMDA4NB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4NTIxUzAwMDA4NR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4NjIxUzAwMDA4Nh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4NzIxUzAwMDA4Nx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4ODIxUzAwMDA4OB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA4OTIxUzAwMDA4OR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5MDIxUzAwMDA5MB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5MTIxUzAwMDA5MR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5MjIxUzAwMDA5Mh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5MzIxUzAwMDA5Mx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5NDIxUzAwMDA5NB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5NTIxUzAwMDA5NR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5NjIxUzAwMDA5Nh05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5NzIxUzAwMDA5Nx05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5ODIxUzAwMDA5OB05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDA5OTIxUzAwMDA5OR05M1RFU1Q="),
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
                Marking=Marking(Code="MDEwNDYwMDAwMDAwMDEwMDIxUzAwMDEwMB05M1RFU1Q="),
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("100.0"))
        kkm.PrintCheck()

        return kkm
