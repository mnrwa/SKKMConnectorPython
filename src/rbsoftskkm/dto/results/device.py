from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.results.kkt_license import KktLicense


@dataclass
class Device:
    """Описание ККМ"""

    #: Часовая зона
    TimeZone: int = 0

    #: Фискальный режим.
    IsFiscal: bool = False

    #: Ширина чековой ленты.
    LineLength: int = 0

    #: Ширина чековой ленты в пикселях.
    LineLengthPixels: int = 0

    #: Версия ФФД.
    FfdVersion: Optional[str] = None

    #: Версия ФФД ФН.
    FnFfdVersion: Optional[str] = None

    #: Тип устройства
    DeviceClass: int = 0

    #: Название модели.
    Model: Optional[str] = None

    #: Заводской номер ККТ.
    SerialNumber: Optional[str] = None

    #: Версия прошивки.
    FirmwareVersion: Optional[str] = None

    #: Версия конфигурации прошивки устройства.
    ConfigurationVersion: Optional[str] = None

    #: Массив лицензий ККТ.
    KktLicenses: Optional[list[KktLicense]] = None
