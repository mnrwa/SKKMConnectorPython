from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from rbsoftskkm.dto.results.warnings import Warnings as _Warnings


@dataclass
class KktStatus:
    """Состояние ККТ"""

    #: Присутствует ли фискальный накопитель.
    IsFnPresent: bool = False

    #: Находится ли фискальный накопитель в состоянии ошибки.
    IsFnError: bool = False

    #: Доступна ли информационная система маркировки.
    IsIsmDisconnected: bool = False

    #: Доступен ли оператор фискальных данных.
    IsOfdDisconnected: bool = False

    #: Предупреждения ФН
    Warnings: Optional[_Warnings] = None

    #: Номер смены.
    ShiftNumber: int = 0

    #: Номер фискального документа.
    DocNumber: int = 0

    #: Фискальный режим.
    IsFiscal: bool = False

    #: Смена открыта.
    IsShiftOpened: bool = False

    #: Смена истекла.
    IsShiftExpired: bool = False

    #: Время получения данных.
    ComputerTime: datetime = datetime.min

    #: Время в часах устройства.
    DeviceTime: datetime = datetime.min

    #: Открыт денежный ящик.
    IsDrawerOpened: bool = False

    #: Наличие чековой ленты.
    IsCheckPaperPresent: bool = False

    #: Открыта ли крышка.
    IsCoverOpened: bool = False

    #: Аккумулятор разряжен.
    IsBatteryLow: bool = False

    #: Открытый документ.
    IsOpenDocument: bool = False

    #: Ширина чековой ленты.
    LineLength: int = 0
