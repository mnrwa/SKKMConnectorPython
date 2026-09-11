from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class CheckCustomer:
    """Сведения о покупателе из ответа"""

    #: Наименование организации или фамилия, имя, отчество (при наличии).
    Info: Optional[str] = None

    #: ИНН организации или покупателя (клиента).
    Inn: Optional[str] = None

    #: Электронная почта.
    Email: Optional[str] = None

    #: Номер телефона.
    Phone: Optional[str] = None

    #: Дата рождения покупателя
    DateOfBirth: Optional[str] = None

    #: Код страны (ОКСМ).
    Citizenship: Optional[str] = None

    #: Числовой код вида документа, удостоверяющего личность.
    DocumentTypeCode: Optional[int] = None

    #: Данные документа, удостоверяющего личность.
    DocumentData: Optional[str] = None

    #: Адрес покупателя.
    Address: Optional[str] = None
