from __future__ import annotations

from decimal import Decimal

from demo.examples.sample import Sample
from rbsoftskkm import (
    Agent,
    AgentType,
    Cashier,
    CheckType,
    FiscalLine,
    MeasureOfQuantity,
    Payments,
    SignCalculationObject,
    SignMethodCalculation,
    SkkmConnector,
    TaxSystem,
    Vendor,
)


class CheckSample22(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Данные платёжного агента и поставщика в заголовке"

    def PostCheckSample22(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН
        kkm.AgentSign = AgentType.PaymentAgent

        kkm.Agent = Agent(
            PayingAgentOperation="Приём платежей",
            PayingAgentPhone=["+79001234567"],
            ReceivePaymentsOperatorPhone=["+79001234567"],
        )

        kkm.Vendor = Vendor(Name="ООО Ромашка", Phones=["+79001234567"], Vatin="7701234560")

        kkm.Positions.append(
            FiscalLine(
                Name="Услуга",
                Quantity=Decimal("1"),
                Price=Decimal("90"),
                Sum=Decimal("90.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Service,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
                AgentSign=AgentType.PaymentAgent,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("90.0"))
        kkm.PrintCheck()

        if not kkm.Ok:
            raise RuntimeError(kkm.ErrorDescription)

        return kkm
