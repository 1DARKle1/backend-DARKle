# Расходы в поездке

Программа считает число записей, сумму и среднюю трату по списку расходов и печатает отчёт.

## Команды

Windows, PowerShell, из папки `trip`:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
py trip.py
```

macOS и Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 trip.py
```

## Что печатает программа

```text
ОТЧЁТ ПО ПОЕЗДКЕ
--------------------------------
записей: 10
всего потрачено: 7900 ₽
средняя трата: 790.00 ₽
```

Заголовок «ОТЧЁТ ПО ПОЕЗДКЕ» выводится жирным зелёным через Rich. Числа те же, что у заготовки из одного файла. Папку `.venv` в репозиторий не кладут: её создают заново командой выше.
