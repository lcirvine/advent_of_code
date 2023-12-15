import numpy as np
from collections import deque
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 14
data = get_input(day_num)


def move_rocks(current_rocks: list, max_num: int, reverse: bool = False) -> list:
    rocks = []
    rocks_str = ''.join(current_rocks)
    if reverse:
        rocks_str = rocks_str[::-1]
    for segment in rocks_str.split('#'):
        rocks.extend(sorted(segment, reverse=True))
        rocks.append('#')
    rocks = rocks[:max_num]
    if reverse:
        rocks = rocks[::-1]
    return rocks


def calculate_load(arr: np.ndarray):
    total_load = 0
    num_rows, num_cols = arr.shape
    for col in range(num_cols):
        total_load += sum([i + 1 for i, char in enumerate(arr[:, col][::-1]) if char == 'O'])
    return total_load


def part_1():
    arr = np.array([list(row) for row in data.splitlines()])
    num_rows, num_cols = arr.shape
    # tilt North
    for col in range(num_cols):
        new_rocks = move_rocks(arr[:, col], max_num=num_rows)
        arr[:, col] = new_rocks
    return calculate_load(arr)


def spin_cycle(arr: np.ndarray):
    num_rows, num_cols = arr.shape
    # tilt North
    for col in range(num_cols):
        new_rocks = move_rocks(arr[:, col], max_num=num_rows)
        arr[:, col] = new_rocks
    # tilt West
    for row in range(num_rows):
        new_rocks = move_rocks(arr[row], max_num=num_cols)
        arr[row] = new_rocks
    # tilt South
    for col in range(num_cols):
        new_rocks = move_rocks(arr[:, col], max_num=num_rows, reverse=True)
        arr[:, col] = new_rocks
    # tilt East
    for row in range(num_rows):
        new_rocks = move_rocks(arr[row], max_num=num_cols, reverse=True)
        arr[row] = new_rocks
    return arr


def part_2(num_cycles: int):
    arr = np.array([list(row) for row in data.splitlines()])
    for cycle in range(num_cycles):
        arr = spin_cycle(arr)
    return calculate_load(arr)


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2(1000)
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
