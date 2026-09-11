from __future__ import annotations

from enum import IntEnum


class DeviceType(IntEnum):
    """Тип драйвера устройства:

    Shtrih - Shtrih

    Native1C - 1С(4.7)

    AtolFRv10 - Atol

    RrElectro - RrElectro

    Native1C5000 - 1С(5.0)

    EmulatorFR - Эмулятор
    """

    #: Shtrih.
    Shtrih = 1

    #: 1С(4.7).
    Native1C = 2

    #: Atol.
    AtolFRv10 = 3

    #: RrElectro.
    RrElectro = 4

    #: 1С(5.0).
    Native1C5000 = 5

    #: Эмулятор.
    EmulatorFR = 100
