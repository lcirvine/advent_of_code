import os
import pandas as pd
import numpy as np


def read_input(file: str = 'day4.txt'):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
        nums = [int(n) for n in data.pop(0).split(',')]
        data.remove('')
    boards = {}
    board_counter = 0
    board = []
    for i in data:
        if len(i) > 0:
            board.append([int(n) for n in i.split()])
        elif len(i) == 0:
            boards[board_counter] = pd.DataFrame(board)
            board = []
            board_counter += 1
    # adding the last board to the dictionary
    boards[board_counter] = pd.DataFrame(board)
    return nums, boards


def part_1():
    nums, boards = read_input('day4_test.txt')
    for num in nums:
        for n, board in boards.items():
            board.replace(num, np.nan, inplace=True)


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
