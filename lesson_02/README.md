# Student Tools

**Студент:** Груздев Николай
**Группа:** РПО2/25

Программа считает среднюю, минимальную и максимальную оценку и печатает отчёт через Rich.

Папка `trip/` в этом же занятии — отдельная работа из `homework_02.md`: расходы в поездке. Ниже описан проект Student Tools из главы 2.8 сайта. Корень проекта — эта папка: `app/` лежит прямо в `lesson_02`.

## Версия Python

На этом компьютере `py --version` печатает Python 3.13.7. В задании курса указан Python 3.12, отдельной установки 3.12 здесь нет.

Интерпретатор окружения проекта:

```text
C:\Users\voerc\Desktop\backend-DARKle\lesson_02\.venv\Scripts\python.exe
```

Это путь `sys.executable` после `py -m venv .venv`. Он указывает внутрь `.venv`, а не на общий Python системы.

## Структура и обязанности

```text
lesson_02/
├── app/main.py                  соединяет расчёты, формат и вывод
├── app/services/calculator.py   средняя, минимум и максимум; пустой список — ValueError
├── app/utils/formatter.py       текст отчёта, без вычислений
├── tests/test_calculator.py     три исходных теста и четыре новых
├── requirements.txt             версии зависимостей
├── .gitignore                   окружение, кэш и .env не попадают в Git
└── trip/                        работа из homework_02.md
```

## Команды

Windows, PowerShell, из папки `lesson_02`:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

Если активация в PowerShell запрещена, команды можно запускать через `.\.venv\Scripts\python.exe` без активации.

macOS и Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m app.main
python -m pytest -v
```

## Ожидаемый результат

Для списка `[5, 4, 5, 3, 5]`:

```text
Средний результат: 4.40
Минимальная оценка: 3
Максимальная оценка: 5
```

Проверка на этом компьютере: `7 passed`.

## Почему .venv не входит в репозиторий

Окружение содержит установленные библиотеки и привязано к этому компьютеру и к пути папки. На другом компьютере его создают заново и ставят библиотеки из `requirements.txt`. В Git передают список зависимостей, а не саму папку `.venv`.
