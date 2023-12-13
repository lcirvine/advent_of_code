import numpy as np
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 13
data = get_input(day_num)


def part_1():
    result = 0
    for pattern in data.split('\n\n'):
        patarr = np.array([list(row) for row in pattern.splitlines()])
        rows, cols = patarr.shape
        for r in range(rows - 1):
            # if this row is the same as the next row
            if np.array_equal(patarr[r], patarr[r + 1]):
                # what is above and below the reflection point
                reflected_up = patarr[0: r + 1]
                reflected_down = patarr[r + 1:]
                # mirrored, flip up side so that row 0 will be the first row after reflection point for both
                reflected_up = np.flip(reflected_up, axis=0)
                # which side has the fewest rows
                min_rows = min(reflected_up.shape[0], reflected_down.shape[0])
                # make sure they have the same number of rows
                reflected_up = reflected_up[:min_rows]
                reflected_down = reflected_down[:min_rows]
                # if both sides are equal, that is the row
                if np.array_equal(reflected_up, reflected_down):
                    # plus 1 because numpy arrays will start at 0 and puzzle numbering starts at 1
                    result += (100 * (r + 1))
        for c in range(cols - 1):
            # if this column is the same as the next column
            if np.array_equal(patarr[:, c], patarr[:, c + 1]):
                # what is to the left and right of the reflection point
                reflected_left = patarr[:, 0: c + 1]
                reflected_right = patarr[:, c + 1:]
                # mirrored, flip left side so that column 0 will be first column after reflection point for both
                reflected_left = np.flip(reflected_left, axis=1)
                # which side has the fewest columns
                min_cols = min(reflected_left.shape[1], reflected_right.shape[1])
                # make sure they have the same number of columns
                reflected_left = reflected_left[:, :min_cols]
                reflected_right = reflected_right[:, :min_cols]
                # if both sides of the array are equal, that is the column
                if np.array_equal(reflected_left, reflected_right):
                    # plus 1 because np array starts at 0 and puzzle numbering starts at 1
                    result += c + 1
    return result


def part_2():
    # there can be only one difference and it may be in the reflected row or column
    result = 0
    for pattern in data.split('\n\n'):
        patarr = np.array([list(row) for row in pattern.splitlines()])
        rows, cols = patarr.shape
        for r in range(rows - 1):
            diffs = 0
            diffs_with_next_row = patarr[r].size - np.sum(patarr[r] == patarr[r + 1])
            diffs += diffs_with_next_row
            if diffs <= 1:
                reflected_up = patarr[0: r + 1]
                reflected_down = patarr[r + 1:]
                reflected_up = np.flip(reflected_up, axis=0)
                min_rows = min(reflected_up.shape[0], reflected_down.shape[0])
                reflected_up = reflected_up[:min_rows]
                reflected_down = reflected_down[:min_rows]
                diffs_in_mirrored_arrays = reflected_up.size - np.sum(reflected_up == reflected_down)
                # don't want to double count the diffs from the reflected row twice
                diffs += (diffs_in_mirrored_arrays - diffs_with_next_row)
                if diffs == 1:
                    result += (100 * (r + 1))
        for c in range(cols - 1):
            diffs = 0
            diffs_with_next_col = patarr[:, c].size - np.sum(patarr[:, c] == patarr[:, c + 1])
            diffs += diffs_with_next_col
            if diffs <= 1:
                reflected_left = patarr[:, 0: c + 1]
                reflected_right = patarr[:, c + 1:]
                reflected_left = np.flip(reflected_left, axis=1)
                min_cols = min(reflected_left.shape[1], reflected_right.shape[1])
                reflected_left = reflected_left[:, :min_cols]
                reflected_right = reflected_right[:, :min_cols]
                diffs_in_mirrored_arrays = reflected_left.size - np.sum(reflected_left == reflected_right)
                diffs += (diffs_in_mirrored_arrays - diffs_with_next_col)
                if diffs == 1:
                    result += c + 1
    return result


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
