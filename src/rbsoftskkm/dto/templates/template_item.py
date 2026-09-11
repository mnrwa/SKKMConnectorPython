from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rbsoftskkm.dto.templates.print_line import PrintLine as _PrintLine


@dataclass
class TemplateItem:
    """Элемент шаблона печати. Создайте объект и задайте PrintLine."""

    #: Строка печати: текст, штрихкод, изображение или разделительная линия.
    PrintLine: Optional[_PrintLine] = None
