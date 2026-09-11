from __future__ import annotations

from dataclasses import dataclass, field

from rbsoftskkm.dto.enums.print_template_type import PrintTemplateType
from rbsoftskkm.dto.templates.template_item import TemplateItem


@dataclass
class PrintTemplate:
    """Шаблон печати, полученный с сервера."""

    #: Имя шаблона. Уникальный идентификатор на сервере.
    Name: str = ""

    #: Тип шаблона.
    Type: PrintTemplateType = PrintTemplateType.Advertisement

    #: Строки шаблона (текст, штрихкод, картинка, разделитель).
    TemplateItems: list[TemplateItem] = field(default_factory=list)
