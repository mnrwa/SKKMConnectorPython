from __future__ import annotations

from enum import IntEnum


class CheckType(IntEnum):
    """Тип чека:

    Text - Текст

    Sale - Продажа (приход)

    SaleReturn - Возврат (возврат прихода)

    Purchase - Покупка (расход)

    PurchaseReturn - Возврат покупки (возврат расхода)

    CorrectionSale - Чек коррекции прихода

    CorrectionSaleReturn - Чек коррекции возврата прихода

    CorrectionPurchase - Чек коррекции расхода

    CorrectionPurchaseReturn - Чек коррекции возврата расхода

    Slip - Слип, нефискальный документ

    Fiscalization - Фискализация

    OpenShift - Чек коррекции прихода

    CloseShift - Z-отчёт

    ReportX - X-отчёт

    ReportSettlement - Отчёт о состоянии расчётов

    CashOut - Выемка

    CashIn - Внесение

    OpenCashDrawer - Открытие денежного ящика

    CopyFromFn - Копия из ФН

    DocumentCopy - Дубликат документа
    """

    #: Текст.
    Text = 0

    #: Продажа (приход).
    Sale = 1

    #: Возврат (возврат прихода).
    SaleReturn = 2

    #: Покупка (расход).
    Purchase = 3

    #: Возврат покупки (возврат расхода).
    PurchaseReturn = 4

    #: Чек коррекции прихода.
    CorrectionSale = 5

    #: Чек коррекции возврата прихода.
    CorrectionSaleReturn = 6

    #: Чек коррекции расхода.
    CorrectionPurchase = 7

    #: Чек коррекции возврата расхода.
    CorrectionPurchaseReturn = 8

    #: Слип.
    Slip = 9

    #: Фискализация.
    Fiscalization = 10

    #: Открытие смены.
    OpenShift = 11

    #: Z-отчёт.
    CloseShift = 12

    #: X-отчёт.
    ReportX = 13

    #: Отчёт о состоянии расчётов.
    ReportSettlement = 14

    #: Выемка.
    CashOut = 20

    #: Внесение.
    CashIn = 21

    #: Открытие денежного ящика.
    OpenCashDrawer = 22

    #: Копия из ФН.
    CopyFromFn = 23

    #: Дубликат документа.
    DocumentCopy = 24
