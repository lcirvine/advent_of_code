import requests
import json
from pathlib import Path
from datetime import date


def get_input(day_num: int = date.today().day, year: int = date.today().year, test=False) -> str:
    """
    Get the puzzle input for the day and year provided.

    Args:
        day_num (int): Day number (i.e. 1 for the first, 2 for the second, etc.), defaults to current day number
        year (int): Year in YYYY format, defaults to current year
        test (bool): True - Return test input, False - return puzzle input, defaults to False

    Returns:
        String with puzzle input, rows should be split with new line character
    """
    input_folder = Path.cwd() / 'inputs'
    if not input_folder.exists():
        input_folder.mkdir()
    if test:
        file_path = input_folder / f"day{day_num}_test.txt"
    else:
        file_path = input_folder / f"day{day_num}.txt"
    if file_path.exists():
        with open(file_path) as f:
            data = f.read()
    else:
        with open(Path.cwd() / 'aoc_cookies.json') as f:
            aoc_cookies = json.load(f)
        res = requests.get(f"https://adventofcode.com/{year}/day/{day_num}/input", verify=False, cookies=aoc_cookies)
        assert res.ok, f"{res.status_code}\n{res.text}"
        data = res.text.strip()
        with open(file_path, 'w') as f:
            f.write(data)
    return data
