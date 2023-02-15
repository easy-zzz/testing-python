"""Загрузите входные данные для одной части головоломки с кодом, если это возможно

Использование https://pypi.org/project/advent-of-code-data / если это доступно.
В противном случае ничего не делает.
"""

# Импорт стандартных библиотек
import pathlib
import sys

# Сторонний импорт
try:
    from aocd.models import Puzzle
except ImportError:
    pypi_url = "https://pypi.org/project/advent-of-code-data/"
    print(f"Установите {pypi_url} для автоматической загрузки входных файлов")
    raise SystemExit()


def download(year, day):
    """Получите входные данные и запишите их в input.txt внутри папки с головоломками"""
    puzzle = Puzzle(year=year, day=day)

    # Скачать вход
    year_path = pathlib.Path(__file__).parent / str(year)
    output_path = next(year_path.glob(f"{day:02d}*")) / "input.txt"
    output_path.write_text(puzzle.input_data)

    # Добавить readme по ссылке на текст головоломки
    readme_path = output_path.with_name("README.md")
    readme_path.write_text(
        f"# {puzzle.title}\n\n"
        f"**Появление кода: День {day}, {year}**\n\n"
        f"Смотреть {puzzle.url}\n"
    )


if __name__ == "__main__":
    try:
        # Читать год и день из командной строки
        download(year=int(sys.argv[1]), day=int(sys.argv[2]))
    except Exception as err:
        # Поймайте исключения, чтобы копиер не очищал каталоги
        print(f"Загрузка ввода не удалась: {err}")
        raise SystemExit()
