from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Cashier,
    CheckType,
    ElectronicPayment,
    ElectronicPaymentMethod,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
)


class CheckSample47(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Все способы электронной оплаты (0-6)"

    def PostCheckSample47(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.FullPrepayment,
                Identifiers="M=0",
                AdditionalInformation="Способ 0",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.PartialPrepayment,
                Identifiers="M=1",
                AdditionalInformation="Способ 1",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.Advance,
                Identifiers="M=2",
                AdditionalInformation="Способ 2",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.FullPayment,
                Identifiers="M=3",
                AdditionalInformation="Способ 3",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.PartialPaymentAndCredit,
                Identifiers="M=4",
                AdditionalInformation="Способ 4",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.CreditTransfer,
                Identifiers="M=5",
                AdditionalInformation="Способ 5",
            ),
        )

        kkm.ElectronicPayments.append(
            ElectronicPayment(
                Amount=Decimal("10"),
                PaymentMethod=ElectronicPaymentMethod.CreditPayment,
                Identifiers="M=6",
                AdditionalInformation="Способ 6",
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Вода 1л.",
                Quantity=Decimal("1"),
                Price=Decimal("70"),
                Sum=Decimal("70.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(ElectronicPayment=Decimal("70"))
        kkm.PrintCheck()

        return kkm
