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


class CheckSample35(Sample):
    GroupPath = "Работа с ККМ|Печать чеков|Примеры чеков"
    Title = "Все признаки предмета расчета"

    def PostCheckSample35(self) -> SkkmConnector:
        kkm = self.kkm
        kkm.DeviceName = self.deviceName
        kkm.Cashier = Cashier(Name=self.cashierName, Vatin=self.cashierVatin)
        kkm.NewRequest()
        kkm.PaymentType = CheckType.Sale
        kkm.TaxVariant = TaxSystem.ОСН

        kkm.Positions.append(
            FiscalLine(
                Name="Товар",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Goods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Подакцизный товар",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ExcisableGoods,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Работа",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Work,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Услуга",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Service,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Ставка азартной игры",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.GamblingStake,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Выигрыш азартной игры",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.GamblingPrize,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Лотерейный билет",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.LotteryTicket,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Выигрыш лотереи",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.LotteryPrize,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Предоставление РИД",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.IntellectualProperty,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Платёж",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Advance,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Агентское вознаграждение",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.AgentFee,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Составной предмет расчёта",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Payout,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Иной предмет расчёта",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Other,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Имущественное право",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.PropertyRight,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Внереализационный доход",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.NonOperatingIncome,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Страховые взносы",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.OtherPayments,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Торговый сбор",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.TradeFee,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Курортный сбор",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.TouristTax,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Залог",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Deposit,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Расход",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.Expense,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОПС ИП",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.PensionContributionIp,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОПС",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.PensionContribution,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОМС ИП",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.MedicalContributionIp,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОМС",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.MedicalContribution,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Взносы на ОСС",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.SocialContribution,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Платёж казино",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.CasinoPayment,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="Выдача денежных средств",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.CashWithdrawalByAgent,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="АТНМ",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.АТНМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="АТМ",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.АТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="ТНМ",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТНМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Positions.append(
            FiscalLine(
                Name="ТМ",
                Quantity=Decimal("1"),
                Price=Decimal("1"),
                Sum=Decimal("1.0"),
                Tax="none",
                TaxSum=Decimal("0"),
                SignMethodCalculation=SignMethodCalculation.FullPayment,
                SignCalculationObject=SignCalculationObject.ТМ,
                MeasureOfQuantity=MeasureOfQuantity.Piece,
            ),
        )

        kkm.Payments = Payments(Cash=Decimal("31.0"))
        kkm.PrintCheck()

        return kkm
