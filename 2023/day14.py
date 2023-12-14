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
        rocks = deque(arr[:, col])
        ix_round = deque([ix for ix, char in enumerate(rocks) if char == 'O'])
        ix_square = deque([ix for ix, char in enumerate(rocks) if char == '#'])
        # putting in a 'blocker' in the first position
        ix_square = deque([0])
        for rr in ix_round:
            insert_pos = [i for i in ix_square if i <= rr][-1]
            # replacing the round rock with an empty space
            rocks.remove('.')
            rocks.insert(insert_pos, 'O')
        total_load += sum([ix for ix, char in enumerate(rocks) if char == 'O'])
        arr[:, col] = rocks
    return total_load


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
