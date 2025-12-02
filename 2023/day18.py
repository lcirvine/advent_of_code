import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 18
data = get_input(day_num, test=True)


digmap = {}
x = 0
y = 0
for i in data.splitlines():
    direction, num, hex = i.split()
    num = int(num)
    hex = hex.strip('(').strip(')')
    if direction == 'R':
        for ix in range(x, num + 1):
            digmap[(ix, y)] = '#'
    elif direction == 'L':
        for ix in range(x - num, x + 1):
            digmap[(ix, y)] = '#'
    elif direction == 'D':
        for iy in range(y, num + 1):
            digmap[(x, iy)] = '#'
    elif direction == 'U':
        for iy in range(y - num, y + 1):
            digmap[(x, iy)] = '#'


def part_1():
    return None


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
