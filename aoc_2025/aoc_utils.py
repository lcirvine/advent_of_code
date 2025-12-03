import requests
import json
from pathlib import Path
from datetime import date
from bs4 import BeautifulSoup


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
        res = requests.get(f"https://adventofcode.com/{year}/day/{day_num}/input", cookies=aoc_cookies)
        assert res.ok, f"{res.status_code}\n{res.text}"
        data = res.text.strip()
        with open(file_path, 'w') as f:
            f.write(data)
    return data


def submit_answer(answer_1=None, answer_2=None, day_num: int = date.today().day, year: int = date.today().year, submit=False):
    """
    Submits the answer(s) or, if submit=False, prints the answer(s) to the terminal

    Args:
        answer_1: The answer to part 1 of the puzzle
        answer_2: The answer to part 2 of the puzzle
        day_num (int): Day number (i.e. 1 for the first, 2 for the second, etc.), defaults to current day number
        year (int): Year in YYYY format, defaults to current year
        submit (bool): Should the answer(s) be submitted to AoC? If not, they will be printed to the terminal.
    """
    if submit:
        with open('aoc_cookies.json') as f:
            aoc_cookies = json.load(f)
        if answer_2:
            answer_data = {'level': 2, 'answer': answer_2}
            print(f"Part 2 answer to submit:\n\n{answer_2}\n\n")
        elif answer_1:
            answer_data = {'level': 1, 'answer': answer_1}
            print(f"Part 1 answer to submit:\n\n{answer_1}\n\n")
        res = requests.post(f"https://adventofcode.com/{year}/day/{day_num}/answer", data=answer_data, cookies=aoc_cookies)
        assert res.ok, f"{res.status_code}\n{res.text}"
        soup = BeautifulSoup(res.text, 'html.parser')
        print(soup.text.strip())
    else:
        print(answer_1)
        print(answer_2)
