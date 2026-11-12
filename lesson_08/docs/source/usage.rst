Запуск и проверки
=================

Программа показывает отчёт по списку оценок ``[5, 4, 5, 3, 5]``
и записывает его в файл.

Как запустить
-------------

Команды выполняются из папки ``lesson_08``.

.. code-block:: text

   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python main.py

Что проверить
-------------

- ``python -m pytest -v`` — тесты
- ``mypy app`` — аннотации
- ``ruff check app`` — докстринги

Средняя оценка считается функцией
:func:`app.services.calculator.calculate_average`.
