from __future__ import annotations

from enum import IntEnum


class PrintTemplateType(IntEnum):
    """Тип печатного шаблона:

    Advertisement - Реклама

    CheckLines - Строки чека

    HeaderOrFooter - Шапка или подвал чека
    """

    #: Реклама.
    Advertisement = 0

    #: Строки чека.
    CheckLines = 1

    #: Шапка или подвал чека.
    HeaderOrFooter = 2
