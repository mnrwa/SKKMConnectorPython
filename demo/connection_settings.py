"""Параметры подключения из левой панели и их проверка."""

from __future__ import annotations

from datetime import date, datetime, time, timedelta

DATE_FORMAT = "%Y-%m-%d"
DATE_HINT = "yyyy-MM-dd"

HINT_HOST = "localhost"
HINT_PORT = "4398"
HINT_TOKEN = "api_key"
HINT_DEVICE = "Emu"
HINT_CASHIER = "Иванов А.И."
HINT_CASHIER_VATIN = "7722345678"


def today() -> datetime:
    return datetime.combine(date.today(), time.min)


class ConnectionSettings:
    """Значения полей подключения; From и To разбираются из текста."""

    def __init__(self) -> None:
        self.Host = ""
        self.Port = 0
        self.Token = ""
        self.Device = ""
        self.Cashier = ""
        self.CashierVatin = ""
        self.DocumentId = ""
        self.FromText = ""
        self.ToText = ""
        self.From = today() - timedelta(days=7)
        self.To = today()

    def try_read(self, need_document_id: bool) -> str:
        """Пустая строка — всё в порядке, иначе текст ошибки для панели «Ответ»."""
        if not self.Host.strip():
            return "Укажите хост сервера ККМ."
        if not 1 <= self.Port <= 65535:
            return "Укажите порт сервера ККМ."
        if need_document_id and not self.DocumentId.strip():
            return "Укажите Id документа."

        date_from, error = parse_date(self.FromText, today() - timedelta(days=7), "с")
        if error:
            return error
        date_to, error = parse_date(self.ToText, today(), "по")
        if error:
            return error
        if date_from > date_to:
            return "Дата «с» позже даты «по»."

        self.From = date_from
        self.To = date_to
        return ""


def parse_date(text: str, fallback: datetime, label: str) -> tuple[datetime, str]:
    value = text.strip()
    if not value:
        return fallback, ""
    try:
        return datetime.strptime(value, DATE_FORMAT), ""
    except ValueError:
        return fallback, f"Укажите дату «{label}» в формате {DATE_HINT}."
