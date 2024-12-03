import numpy as np
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 21
data = get_input(day_num, test=True)
garden = {}
for row_num, row in enumerate(data.splitlines()):
    for col_num, char in enumerate(row):
        if char == 'S':
            garden[(row_num, col_num)] = 0
        else:
            garden[(row_num, col_num)] = char

garden_arr = np.array([list(row) for row in data.splitlines()])
start_arr = np.where(garden_arr == 'S')
garden_arr[start_arr[0][0]][start_arr[1][0]] = 0


def find_neighbors(loc):
    x, y = loc
    # [n for n in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if n in garden and garden[n] != '#']
    return list(filter(lambda n: n in garden and garden[n] != '#', [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))


def part_1(target_steps: int = 16):
    for step in range(0, target_steps + 1):
        for loc in [x for x in garden if garden[x] == step]:
            neighbors = find_neighbors(loc)
            for neighbor in neighbors:
                garden[neighbor] = step + 1
                garden_arr[neighbor[0]][neighbor[1]] = step + 1
    locs_at_steps = [loc for loc in garden if garden[loc] == target_steps]
    return len(locs_at_steps)


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
