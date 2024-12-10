from datetime import date
import sys
import math
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 7
data = get_input(day_num, test=True)


def part_1():
    total = 0
    for row in data.split('\n'):
        result = int(row.split(':')[0])
        nums = [int(n) for n in row.split(':')[1].strip().split(' ')]
        p = math.prod(nums)
        s = sum(nums)
        if p >= result:
            if p == result:
                total += result
            elif s == result:
                total += result
            
    return total


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
