import requests
import json
from pathlib import Path
from datetime import date


def get_input(day_num: int = date.today().day, year: int = date.today().year):
    file_path = Path.cwd() / 'inputs' / f"day{day_num}.txt"
    if file_path.exists():
        with open(file_path) as f:
            data = f.read()
    else:
        with open(Path.cwd() / 'aoc_cookies.json') as f:
            aoc_cookies = json.load(f)
        res = requests.get(f"https://adventofcode.com/{year}/day/{day_num}/input", verify=False, cookies=aoc_cookies)
        assert res.ok, f"{res.status_code}\n{res.text}"
        data = res.text
        with open(file_path, 'w') as f:
            f.write(data)
    return data
