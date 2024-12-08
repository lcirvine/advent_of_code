from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = date.today().day
data = get_input(day_num)

word_search = {}
x_pos = []
for y, row in enumerate(data.split('\n')):
    for x, char in enumerate(row):
        word_search[(x, y)] = char
        if char.upper() == 'X':
            x_pos.append((x, y))

def part_1():
    return None


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
