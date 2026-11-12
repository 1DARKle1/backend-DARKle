"""Расчёты по списку оценок.

Здесь нет чтения файлов и печати. Пустой список — ошибка вызова.
"""


def calculate_average(values: list[int]) -> float:
    """Считает среднюю оценку.

    Args:
        values: Оценки от 2 до 5. Список не должен быть пустым.

    Returns:
        Среднее значение без дополнительного округления.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return sum(values) / len(values)


def calculate_min(values: list[int]) -> int:
    """Возвращает наименьшую оценку.

    Args:
        values: Оценки от 2 до 5. Список не должен быть пустым.

    Returns:
        Наименьшее значение списка.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return min(values)


def calculate_max(values: list[int]) -> int:
    """Возвращает наибольшую оценку.

    Args:
        values: Оценки от 2 до 5. Список не должен быть пустым.

    Returns:
        Наибольшее значение списка.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return max(values)


def grade_bounds(values: list[int]) -> tuple[int, int]:
    """Возвращает наименьшую и наибольшую оценку.

    Args:
        values: Оценки от 2 до 5. Список не должен быть пустым.

    Returns:
        Пара из минимума и максимума, в этом порядке.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not values:
        raise ValueError("Список оценок не должен быть пустым")
    return min(values), max(values)
