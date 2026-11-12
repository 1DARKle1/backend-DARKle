"""Запись готового отчёта в текстовый файл."""

from pathlib import Path


def save_report(path: Path, lines: list[str]) -> int:
    """Записывает готовый отчёт в текстовый файл.

    Args:
        path: Куда записать отчёт. Родительская папка должна существовать.
            Если файл уже есть, он перезаписывается целиком.
        lines: Строки отчёта без символа перевода строки на конце.

    Returns:
        Число записанных строк.

    Raises:
        OSError: Если папки для файла нет или запись невозможна.
    """
    text = "\n".join(lines)
    if lines:
        text += "\n"
    path.write_text(text, encoding="utf-8")
    return len(lines)
