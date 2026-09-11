from __future__ import annotations

from enum import IntEnum


class FiscalizationReasonCode(IntEnum):
    """Код причины перерегистрации ККТ:

    FnReplacement - Замена ФН

    OfdReplacement - Замена ОФД

    RequisitesChange - Изменение реквизитов

    SettingsChange - Изменение настроек ККТ
    """

    #: Замена ФН.
    FnReplacement = 1

    #: Замена ОФД.
    OfdReplacement = 2

    #: Изменение реквизитов.
    RequisitesChange = 3

    #: Изменение настроек ККТ.
    SettingsChange = 4
