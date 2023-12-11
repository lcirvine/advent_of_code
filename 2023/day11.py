import numpy as np
from itertools import combinations
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 11
data = get_input(day_num)


def find_empty_rows_and_cols(arr: np.ndarray, axis: int, empty_char: str = '.'):
    rows, cols = arr.shape
    axis_ref = {0: rows, 1: cols}
    # finding which rows or columns do not contain '#'
    empty = []
    # rows
    if axis == 0:
        for num in range(axis_ref[axis]):
            if all([x == empty_char for x in arr[num]]):
                empty.append(num)
    # cols
    elif axis == 1:
        for num in range(axis_ref[axis]):
            if all([x == empty_char for x in arr[:, num]]):
                empty.append(num)
    return empty


def expand_universe(arr: np.ndarray):
    rows, cols = arr.shape
    # expand rows
    empty_rows = find_empty_rows_and_cols(arr, axis=0)
    for ix, r in enumerate(empty_rows, start=1):
        arr = np.insert(arr, ix + r, list('.' * cols), axis=0)
    # finding new shape
    # expand cols
    rows, cols = arr.shape
    # finding which rows do not contain '#'
    empty_cols = find_empty_rows_and_cols(arr, axis=1)
    for ix, c in enumerate(empty_cols, start=1):
        arr = np.insert(arr, ix + c, list('.' * rows), axis=1)
    return arr


def print_array(arr: np.ndarray):
    for row in arr[:]:
        print(' '.join([str(x) for x in row]))


def find_galaxies(arr: np.ndarray, galaxy_char: str = '#'):
    galaxies = []
    for row_num, row in enumerate(arr):
        for col_num, char in enumerate(row):
            if char == galaxy_char:
                galaxies.append((col_num, row_num))
    return galaxies


def part_1():
    cosmos = np.array([list(row) for row in data.splitlines()])
    cosmos = expand_universe(cosmos)
    galaxies = find_galaxies(cosmos)
    total_dist = 0
    for galaxy_combo in combinations(galaxies, 2):
        g1x, g1y = galaxy_combo[0]
        g2x, g2y = galaxy_combo[1]
        dist = abs(g2x - g1x) + abs(g2y - g1y)
        total_dist += dist
    return total_dist


def part_2():
    expansion_dist = 1000000
    cosmos = np.array([list(row) for row in data.splitlines()])
    galaxies = find_galaxies(cosmos)
    empty_rows = find_empty_rows_and_cols(cosmos, axis=0)
    empty_cols = find_empty_rows_and_cols(cosmos, axis=1)
    total_dist = 0
    for galaxy_combo in combinations(galaxies, 2):
        g1x, g1y = galaxy_combo[0]
        g2x, g2y = galaxy_combo[1]
        x_dist = abs(g2x - g1x)
        xsorted = sorted((g2x, g1x))
        xcrosses = len([x for x in empty_cols if x in range(xsorted[0], xsorted[1])])
        # already counted the original distance, so subtracting 1 from expansion distance
        x_dist += (expansion_dist - 1) * xcrosses
        y_dist = abs(g2y - g1y)
        ysorted = sorted((g2y, g1y))
        ycrosses = len([y for y in empty_rows if y in range(ysorted[0], ysorted[1])])
        # already counted the original distance, so subtracting 1 from expansion distance
        y_dist += (expansion_dist - 1) * ycrosses
        total_dist += sum((x_dist, y_dist))
    return total_dist


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
