import os
import pandas as pd


def read_input(file: str):
    data_returned = []
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    for row in data:
        data_returned.append([int(x) for x in row])
    return data_returned


def part_1():
    data = read_input('day9.txt')
    df = pd.DataFrame(data)
    num_rows, num_cols = df.shape
    risk_level = 0
    for col in df.columns:
        for row, row_data in df.iterrows():
            cell_val = df.loc[row, col]
            comp_cells = []
            if row != 0:
                left_cell = df.loc[row - 1, col]
                comp_cells.append(left_cell)
            if row != (num_rows - 1):
                right_cell = df.loc[row + 1, col]
                comp_cells.append(right_cell)
            if col != 0:
                up_cell = df.loc[row, col - 1]
                comp_cells.append(up_cell)
            if col != (num_cols - 1):
                down_cell = df.loc[row, col + 1]
                comp_cells.append(down_cell)
            if min(comp_cells) > cell_val:
                risk_level += (cell_val + 1)
    return risk_level


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
