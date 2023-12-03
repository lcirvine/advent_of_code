import re
import sys
sys.path.append('..')
from aoc_utils import get_input

data = get_input(day_num=3, test=True)
special_chars = [x for x in set(data) if not x.isnumeric() and x not in ('\n', '.')]
special_char_coords = []
char_map = {}
for y, row in enumerate(data.split('\n'), 0):
    for x, char in enumerate(row, 0):
        char_map[(x, y)] = char
        if char in special_chars:
            special_char_coords.append((x, y))


def part_1():
    result = []
    for y, row in enumerate(data.split('\n'), 0):
        for m in [mo for mo in re.finditer(r"(\d*)", row) if mo.group()]:
            neighbors = [(ix, iy) for ix in range(m.start() - 1, m.end() + 2) for iy in range(y - 1, y + 2) if (ix, iy) in special_char_coords]
            if neighbors:
                result.append(int(m.group()))
    return sum(result)


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
