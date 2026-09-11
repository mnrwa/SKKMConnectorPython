from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.enums.device_type import DeviceType


@dataclass
class DeviceListResponse:
    """Элемент списка ККТ"""

    #: Имя устройства.
    DeviceName: Optional[str] = None

    #: Тип драйвера
    Driver: Optional[DeviceType] = None

    #: Имя пула, в который входит устройство.
    Pool: Optional[str] = None

    #: Описание статуса устройства.
    DeviceStatusDescription: Optional[str] = None
