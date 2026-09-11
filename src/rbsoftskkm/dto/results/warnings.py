from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Warnings:
    """Предупреждения ФН"""

    #: Критическая ошибка ФН.
    CriticalError: bool = False

    #: Память ФН переполнена.
    MemoryOverflow: bool = False

    #: Требуется срочная замена ФН.
    NeedReplacement: bool = False

    #: Превышено время ожидания ответа от ОФД.
    OfdTimeout: bool = False

    #: Исчерпан ресурс ФН.
    ResourceExhausted: bool = False
