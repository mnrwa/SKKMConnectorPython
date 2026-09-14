# SKKM Connector Python — коротко

Библиотека `rbsoftskkm` — программная обёртка над REST API **Сервера ККМ** для приложений на Python.
Полное описание — в [README.md](README.md), справочник по методам — в [API.md](API.md).

## 1. Установка

```powershell
python -m pip install rbsoftskkm-1.27.0-py3-none-any.whl
```

Из репозитория проекта:

```powershell
python -m pip install git+https://github.com/mnrwa/SKKMConnectorPython.git
```

Из каталога с исходниками (правки видны сразу):

```powershell
python -m pip install -e C:\Users\user\Documents\Connector
```

Требуется Python 3.10 и новее; единственная зависимость — `httpx`.

## 2. Подключение

```python
from rbsoftskkm import Cashier, SkkmConnector

with SkkmConnector() as kkm:
    kkm.Host = "localhost"          # адрес Сервера ККМ
    kkm.Port = 4398                 # порт службы печати
    kkm.Token = "api_key"           # нужен, если анонимный доступ выключен
    kkm.DeviceName = "Emu"          # имя кассы на сервере
    kkm.Cashier = Cashier(Name="Иванов А.И.", Vatin="7722345678")

    kkm.Connect()
    print(kkm.Ok, kkm.ErrorCode, kkm.ErrorDescription)
```

Схема работы всегда одна: заполнить свойства, вызвать метод, прочитать результат из свойств.
`kkm.Ok` — успех вызова, `kkm.ErrorCode` и `kkm.ErrorDescription` — ошибка сервера или транспорта.

## 3. Чек

```python
from decimal import Decimal

from rbsoftskkm import CheckType, FiscalLine, Payments, TaxSystem

kkm.NewRequest()                     # очистка позиций, оплат и прошлого результата
kkm.PaymentType = CheckType.Sale
kkm.TaxVariant = TaxSystem.ОСН

kkm.Positions.append(
    FiscalLine(
        Name="Кофе американо",
        Quantity=Decimal("1"),
        Price=Decimal("150"),
        Sum=Decimal("150"),
        Tax="20",
        TaxSum=Decimal("25"),
    )
)
kkm.Payments = Payments(Cash=Decimal("150"))

kkm.PrintCheck()

if kkm.Ok:
    print(kkm.FiscalSign, kkm.ShiftNumber, kkm.DocumentId)
else:
    print(kkm.ErrorCode, kkm.ErrorDescription)
```

Денежные суммы — `decimal.Decimal`: округление `float` даёт значения, которые сервер отвергает.

## 4. Смена и наличные

```python
kkm.OpenShift()          # открытие смены
kkm.ReportX()            # X-отчёт
kkm.CloseShift()         # Z-отчёт

kkm.CashAmount = Decimal("1000")
kkm.CashIn()             # внесение; CashOut() — выемка

kkm.GetCash()            # остаток в ящике: kkm.CashBalance
```

## 5. Ошибки и отмена

| `ErrorCode` | Что произошло                     |
| ----------- | --------------------------------- |
| `0`         | Успех, `Ok = True`.               |
| `> 0`       | Ошибка сервера ККМ или ККТ.       |
| `-1`        | Нет соединения с сервером.        |
| `-2`        | Превышено время ожидания ответа.  |
| `-3`        | Запрос отменён через `Cancel()`.  |

```python
import threading

threading.Timer(2.0, kkm.Cancel).start()   # отмена из другого потока
kkm.PrintCheck()
```

Таймаут задаётся свойством `Timeout` (по умолчанию 60 секунд):

```python
from datetime import timedelta

kkm.Timeout = timedelta(seconds=15)
```

## 6. Что дальше

- [README.md](README.md) — все свойства, типы данных и варианты интеграции.
- [API.md](API.md) — методы коннектора и эндпоинты REST API.
- [READMEDemo.md](READMEDemo.md) — демо-приложение со 182 готовыми примерами.
