import re
import sys
sys.path.append('..')
from aoc_utils import get_input


def part_1(calibrations: list):
    cal_val = 0
    for text_line in calibrations:
        vals = re.findall(r"\d", text_line)
        if vals:
            cal_val += int(vals[0] + vals[-1])
    return cal_val


def part_2(calibrations: list):
    cal_val = 0
    pat = r"(?=(\d)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))"
    val_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    for text_line in calibrations:
        vals = [num for group in re.findall(pat, text_line) for num in group if num]
        if vals:
            first_val = vals[0]
            last_val = vals[-1]
            if first_val in val_map:
                first_val = val_map[first_val]
            if last_val in val_map:
                last_val = val_map[last_val]
            cal_val += int(first_val + last_val)
    return cal_val


if __name__ == '__main__':
    puzzle_data = get_input(day_num=1).split('\n')
    print(part_1(puzzle_data))
    print(part_2(puzzle_data))
