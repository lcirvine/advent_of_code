from typing import Union
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 10
data = get_input(day_num)
pipe_map = {}
for row_num, row in enumerate(data.split('\n')):
    for col_num, char in enumerate(row):
        pipe_map[(col_num, row_num)] = char
        if char == 'S':
            start_pos = (col_num, row_num)


pipe_directions = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)]
}


def viable_neighbors(loc):
    possible_neighbors = []
    x, y = loc
    dir_chars = {
        'up': ('|', 'F', '7'),
        'down': ('|', 'L', 'J'),
        'right': ('-', '7', 'J'),
        'left': ('-', 'F', 'L')
    }
    neighbor_map = {
        'up': (x, y + 1),
        'down': (x, y - 1),
        'right': (x + 1, y),
        'left': (x - 1, y)
    }
    for direction, loc in neighbor_map.items():
        if loc in pipe_map and pipe_map[neighbor_map[direction]] in dir_chars[direction]:
            possible_neighbors.append(loc)
    return possible_neighbors


def travel_in_pipes(loc, pipes_visited: list):
    pipes_visited.append(loc)
    char = pipe_map[loc]
    # replacing the character with a number for the step, that way I don't revisit this place
    pipe_map[loc] = len(pipes_visited) - 1
    new_loc = None
    for deltas in pipe_directions[char]:
        new_loc_option = (loc[0] + deltas[0], loc[1] + deltas[1])
        if (new_loc_option in pipe_map) and (new_loc_option not in pipes_visited):
            new_loc = new_loc_option
    # if I get back to start position, return the list of pipes visited
    if not new_loc:
        return pipes_visited
    else:
        return travel_in_pipes(new_loc, pipes_visited)


def part_1():
    start_neighbors = viable_neighbors(start_pos)
    pipe_map[start_pos] = 0
    pipe_path = travel_in_pipes(start_neighbors[0], pipes_visited=[(start_pos)])
    return int(len(pipe_path) / 2)


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
