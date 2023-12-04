import re
import sys
sys.path.append('..')
from aoc_utils import get_input

data = get_input(day_num=3)
special_chars = [x for x in set(data) if not x.isnumeric() and x not in ('\n', '.')]
special_char_coords = []
gear_coords = []
char_map = {}
for y, row in enumerate(data.split('\n'), 0):
    for x, char in enumerate(row, 0):
        char_map[(x, y)] = char
        if char in special_chars:
            special_char_coords.append((x, y))
        if char == '*':
            gear_coords.append((x, y))


def part_1():
    result = 0
    for y, row in enumerate(data.split('\n'), 0):
        for m in [mo for mo in re.finditer(r"(\d*)", row) if mo.group()]:
            neighbors = [(ix, iy) for ix in range(m.start() - 1, m.end() + 1) for iy in range(y - 1, y + 2) if (ix, iy) in special_char_coords]
            if neighbors:
                result += int(m.group())
    return result


def part_2():
    result = 0
    rows = data.split('\n')
    for gear_coord in gear_coords:
        gx = gear_coord[0]
        gy = gear_coord[1]
        neighbors = []
        for row_num in (gy - 1, gy + 1):
            if row_num in range(0, len(rows) + 1):
                for nm in [mo.group() for mo in re.finditer(r"(\d*)", rows[row_num]) if mo.group() and ((gx - 1 in mo.span()) or (gx + 1 in mo.span()))]:
                    neighbors.append(nm)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
