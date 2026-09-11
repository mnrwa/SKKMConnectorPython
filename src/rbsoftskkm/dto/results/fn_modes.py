from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FnModes:
    """Режимы работы ККТ"""

    #: Принтер в автомате
    PrinterAutomatic: bool = False

    #: Автономный режим (без передачи в ОФД)
    OfflineMode: bool = False

    #: Признак расчетов за услуги
    ServiceSign: bool = False

    #: Признак формирования БСО
    BsoSign: bool = False

    #: ККТ для расчетов только в Интернет
    CalcOnlineSign: bool = False

    #: Шифрование данных
    DataEncryption: bool = False

    #: Продажа подакцизного товара
    SaleExcisableGoods: bool = False

    #: Признак проведения азартных игр
    SignOfGambling: bool = False

    #: Признак проведения лотереи
    SignOfLottery: bool = False

    #: Ломбард
    Pawnshop: bool = False

    #: Страхование
    Assurance: bool = False

    #: Продажа маркированного товара
    Marking: bool = False

    #: Вендинговый автомат
    VendingMachine: bool = False

    #: Общественное питание
    CateringServices: bool = False

    #: Оптовая торговля
    WholesaleTrade: bool = False

    #: Автоматический режим
    AutomaticMode: bool = False
