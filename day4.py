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
    nums, boards = read_input('day4.txt')
    for num in nums:
        # marking the boards by setting number called to nan
        for n, board in boards.items():
            board.replace(num, np.nan, inplace=True)
            # checking the boards for a winner
            for col in board.columns:
                if board[col].isna().all():
                    return int(board.sum().sum() * num)
            for i, row in board.iterrows():
                if row.isna().all():
                    return int(board.sum().sum() * num)


def part_2():
    nums, boards = read_input('day4.txt')
    possible_boards = list(boards.keys())
    for num in nums:
        for n, board in boards.items():
            # marking the boards by setting number called to nan
            board.replace(num, np.nan, inplace=True)
            # checking the boards for a winner
            for col in board.columns:
                if board[col].isna().all() and n in possible_boards:
                    possible_boards.remove(n)
            for i, row in board.iterrows():
                if row.isna().all() and n in possible_boards:
                    possible_boards.remove(n)
            # checking to see how many boards are left
            if len(possible_boards) == 0:
                return int(board.sum().sum() * num)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
