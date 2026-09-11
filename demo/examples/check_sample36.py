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


class CheckSample36(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Все признаки способа расчета"

    def PostCheckSample36(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Предоплата 100%",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPrepayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Предоплата",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPrepayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Аванс",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.Advance,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Полный расчёт",
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
                Name="Частичный расчёт",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.PartialPaymentAndCredit,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Передача в кредит",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditTransfer,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Оплата кредита",
                Quantity=Decimal("1"),
                Price=Decimal("10"),
                Sum=Decimal("10.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.CreditPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("70.0"))
        kkm.PrintCheck()

        return kkm
