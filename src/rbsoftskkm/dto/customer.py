from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Customer:
    """Сведения о покупателе (клиенте):

    Info - Наименование организации или ФИО

    Vatin - ИНН покупателя

    Email - Электронная почта

    Phone - Телефон

    DateOfBirth - Дата рождения

    Citizenship - Код страны гражданства

    DocumentTypeCode - Код вида документа (таблица 116 ФФД)

    DocumentData - Данные документа, удостоверяющего личность

    Address - Адрес покупателя

    Заполните только нужные поля.
    """

    #: Наименование организации или фамилия, имя, отчество (при наличии).
    Info: Optional[str] = None

    #: ИНН покупателя.
    Vatin: Optional[str] = None

    #: Электронная почта покупателя.
    Email: Optional[str] = None

    #: Номер телефона.
    Phone: Optional[str] = None

    #: Дата рождения покупателя (клиента).
    DateOfBirth: Optional[str] = None

    #: Числовой код страны.
    Citizenship: Optional[str] = None

    #: Числовой код вида документа, удостоверяющего личность (таблица 116).
    DocumentTypeCode: Optional[str] = None

    #: Данные документа, удостоверяющего личность.
    DocumentData: Optional[str] = None

    #: Адрес покупателя.
    Address: Optional[str] = None
