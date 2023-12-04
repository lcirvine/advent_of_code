import re
import sys
sys.path.append('..')
from aoc_utils import get_input

data = get_input(day_num=3)
special_chars = [x for x in set(data) if not x.isnumeric() and x not in ('\n', '.')]
special_char_coords = []
gear_coords = []
char_map = {}
# creating a dictionary with keys as (x, y) and values as char in location
for y, row in enumerate(data.split('\n'), 0):
    for x, char in enumerate(row, 0):
        char_map[(x, y)] = char
        # saving special characters and gears (pt 2) in separate list
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
        # look at the rows above, on, and below the row with the gear
        for row_num in [y for y in range(gy - 1, gy + 2) if y in range(0, len(rows))]:
            # find what numbers are in that row
            for mo in [m for m in re.finditer(r"(\d*)", rows[row_num]) if m.group()]:
                # find if the x coord is in range of number
                mo_x_span = range(mo.start(), mo.end())
                if (gx - 1 in mo_x_span) or (gx in mo_x_span) or (gx + 1 in mo_x_span):
                    neighbors.append(int(mo.group()))
        if len(neighbors) == 2:
            result += (neighbors[0] * neighbors[1])
    return result


if __name__ == '__main__':
    print(part_1())
    print(part_2())
