"""Строки отчёта по оценкам. Расчёты остаются в services."""


def format_average(value: float) -> str:
    """Форматирует среднюю оценку.

    Args:
        value: Среднее значение.

    Returns:
        Строка с двумя знаками после точки.
    """
    return f"Средний результат: {value:.2f}"


def format_report(average: float, minimum: int, maximum: int) -> str:
    """Собирает три строки отчёта.

    Args:
        average: Средняя оценка. В строке будет два знака после точки.
        minimum: Наименьшая оценка.
        maximum: Наибольшая оценка.

    Returns:
        Текст из трёх строк, без перевода строки в конце.
    """
    return "\n".join(
        [
            format_average(average),
            f"Минимальная оценка: {minimum}",
            f"Максимальная оценка: {maximum}",
        ]
    )
