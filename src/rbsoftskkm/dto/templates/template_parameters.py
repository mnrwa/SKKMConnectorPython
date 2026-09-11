from __future__ import annotations

from dataclasses import dataclass, field

from rbsoftskkm.dto.enums.print_template_type import PrintTemplateType
from rbsoftskkm.dto.templates.template_item import TemplateItem


@dataclass
class TemplateParameters:
    """Параметры создания или изменения шаблона печати:

    Name - Уникальное имя шаблона на сервере

    Type - Тип шаблона. Используйте enum PrintTemplateType

    TemplateItems - Строки шаблона (TemplateItem / PrintLine)
    """

    #: Имя шаблона. Уникальный идентификатор на сервере.
    #: Разрешены символы a-z, A-Z, 0-9, _, -, (, ). Пробелы запрещены.
    Name: str = ""

    #: Тип шаблона. Используйте enum PrintTemplateType.
    Type: PrintTemplateType = PrintTemplateType.Advertisement

    #: Строки шаблона (текст, штрихкод, картинка, разделительная линия).
    TemplateItems: list[TemplateItem] = field(default_factory=list)
