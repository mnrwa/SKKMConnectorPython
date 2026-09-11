from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.results.device import Device as _Device
from rbsoftskkm.dto.results.driver import Driver as _Driver
from rbsoftskkm.dto.results.fn import Fn as _Fn
from rbsoftskkm.dto.results.kkt_status import KktStatus


@dataclass
class DataKkt:
    #: Версия сервера ККМ.
    ServerVersion: Optional[str] = None

    #: Описание фискального накопителя
    Fn: Optional[_Fn] = None

    #: Описание ККМ
    Device: Optional[_Device] = None

    #: Описание драйвера ККМ
    Driver: Optional[_Driver] = None

    #: Состояние ККТ
    Status: Optional[KktStatus] = None
