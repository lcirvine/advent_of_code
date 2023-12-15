import numpy as np
from collections import deque
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 14
data = get_input(day_num, test=True)


def part_1():
    total_load = 0
    arr = np.array([list(row) for row in data.splitlines()])
    num_rows, num_cols = arr.shape
    for col in range(num_cols):
        rocks_str = ''.join(arr[:, col])
        rocks = []
        for segment in rocks_str.split('#'):
            rocks.extend(['#'] + sorted(segment))
        total_load += sum([i for i, char in enumerate(rocks) if char == 'O'])
        arr[:, col] = rocks[::-1][:num_rows]
    return total_load


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
