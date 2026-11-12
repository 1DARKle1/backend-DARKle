# Student Tools

**Студент:** Груздев Николай
**Группа:** РПО2/25

Программа считает среднюю, минимальную и максимальную оценку списка `[5, 4, 5, 3, 5]`, печатает отчёт и записывает его в `report.txt`. К расчётам темы 02 добавлены `grade_bounds` и `save_report`.

Рецензия практикума «Младший разработчик» лежит в файле `podpisi_Груздев_Николай.md`. Этот файл к проекту Student Tools не относится, его не удалять.

## Версия Python

На компьютере установлен Python 3.13.7. В курсе указан Python 3.12, отдельной установки 3.12 нет.

```text
C:\Users\voerc\Desktop\backend-DARKle\lesson_04\.venv\Scripts\python.exe
```

## Структура

```text
app/services/calculator.py    средняя, минимум, максимум, пара границ
app/services/report_file.py   запись готового отчёта в файл UTF-8
app/utils/formatter.py        текст отчёта
main.py                       печать и вызов обеих новых функций
tests/                        11 тестов
pyproject.toml                mypy и Ruff
.vscode/settings.json         формат докстрингов и режим basic
docs/help.txt                 вывод help() по двум модулям
```

## Команды

Windows, PowerShell, из папки `lesson_04`:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
python -m pytest -v
mypy app
ruff check app
```

## Ожидаемый результат

На экране три строки:

```text
Средний результат: 4.40
Минимальная оценка: 3
Максимальная оценка: 5
```

В `report.txt` те же три строки и четвёртая: `Границы: 3 и 5`. Файл создаётся при запуске и в Git не входит. Проверка: `11 passed`.

## Формат докстрингов

Формат Google. В `.vscode/settings.json` для генератора записан `google-notypes`: типы остаются в аннотациях и в тексте докстринга не повторяются. Краткая строка стоит в первой строке докстринга, иначе Ruff выдаёт замечание `D212`.

## Проверка

```text
mypy app
Success: no issues found in 6 source files

ruff check app
All checks passed!
```

`.venv` не входит в репозиторий: это локальная папка с библиотеками для этого компьютера. На другом компьютере её создают заново и ставят зависимости из `requirements.txt`.
