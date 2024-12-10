from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 9
data = get_input(day_num)

files = [data[x] for x in range(0, len(data), 2)]
spaces = [data[x] for x in range(1, len(data), 2)]


def part_1():
    return None


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
