from aoc_inputs import get_input
import string

data = get_input(day_num=12, test=True).split('\n')
char_height = dict(zip(string.ascii_lowercase, range(0, 26)))
char_height['S'] = 0
char_height['E'] = 25
height_map = {}
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        height_map[(x, y)] = char_height[data[y][x]]


def part_1():
    pass


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
