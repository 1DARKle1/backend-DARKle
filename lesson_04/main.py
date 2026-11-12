"""Точка входа Student Tools.

Считает отчёт по фиксированному списку оценок, печатает его и записывает
в файл ``report.txt`` в текущей папке.
"""

from pathlib import Path

from rich.console import Console

from app.services.calculator import (
    calculate_average,
    calculate_max,
    calculate_min,
    grade_bounds,
)
from app.services.report_file import save_report
from app.utils.formatter import format_report


def main() -> None:
    """Печатает отчёт и записывает его в ``report.txt``."""
    values = [5, 4, 5, 3, 5]
    report = format_report(
        calculate_average(values),
        calculate_min(values),
        calculate_max(values),
    )
    Console().print(report)
    low, high = grade_bounds(values)
    lines = [
        *report.splitlines(),
        f"Границы: {low} и {high}",
    ]
    save_report(Path("report.txt"), lines)


if __name__ == "__main__":
    main()
