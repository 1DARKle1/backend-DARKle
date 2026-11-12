def format_average(value: float) -> str:
    return f"Средний результат: {value:.2f}"


def format_report(average: float, minimum: int, maximum: int) -> str:
    return "\n".join(
        [
            format_average(average),
            f"Минимальная оценка: {minimum}",
            f"Максимальная оценка: {maximum}",
        ]
    )
