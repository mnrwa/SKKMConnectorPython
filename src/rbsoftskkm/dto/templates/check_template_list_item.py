from __future__ import annotations

from dataclasses import dataclass

from rbsoftskkm.dto.enums.check_type import CheckType


@dataclass
class CheckTemplateListItem:
    """Элемент списка шаблонов чека."""

    #: Имя шаблона чека.
    Name: str = ""

    #: Тип чека шаблона
    TaskType: CheckType = CheckType.Text
