from rich.console import Console

from app.services.calculator import calculate_average, calculate_max, calculate_min
from app.utils.formatter import format_report


def main():
    values = [5, 4, 5, 3, 5]
    report = format_report(
        calculate_average(values),
        calculate_min(values),
        calculate_max(values),
    )
    Console().print(report)


if __name__ == "__main__":
    main()
