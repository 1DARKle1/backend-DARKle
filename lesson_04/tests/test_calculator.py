import pytest

from app.services.calculator import (
    calculate_average,
    calculate_max,
    calculate_min,
    grade_bounds,
)
from app.services.report_file import save_report
from app.utils.formatter import format_average


def test_average():
    assert calculate_average([5, 4, 5, 3, 5]) == pytest.approx(4.4)


def test_format():
    assert format_average(4.4) == "Средний результат: 4.40"


def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])


def test_min():
    assert calculate_min([5, 4, 5, 3, 5]) == 3


def test_min_empty():
    with pytest.raises(ValueError):
        calculate_min([])


def test_max():
    assert calculate_max([5, 4, 5, 3, 5]) == 5


def test_max_empty():
    with pytest.raises(ValueError):
        calculate_max([])


def test_grade_bounds():
    assert grade_bounds([5, 4, 5, 3, 5]) == (3, 5)


def test_grade_bounds_empty():
    with pytest.raises(ValueError):
        grade_bounds([])


def test_save_new_file(tmp_path):
    path = tmp_path / "report.txt"
    count = save_report(path, ["Средний результат: 4.40", "Минимальная оценка: 3"])
    assert count == 2
    assert path.read_text(encoding="utf-8") == (
        "Средний результат: 4.40\nМинимальная оценка: 3\n"
    )


def test_save_overwrites(tmp_path):
    path = tmp_path / "report.txt"
    path.write_text("старое\n", encoding="utf-8")
    count = save_report(path, ["новое"])
    assert count == 1
    assert path.read_text(encoding="utf-8") == "новое\n"
