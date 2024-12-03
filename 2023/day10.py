import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 10
data = get_input(day_num, test=True)
pipe_map = {}
for row_num, row in enumerate(data.split('\n')):
    for col_num, char in enumerate(row):
        pipe_map[(col_num, row_num)] = char
        if char == 'S':
            start_pos = (col_num, row_num)

# up = (0, -1), down = (0, 1), right = (1, 0), left = (-1, 0)
pipe_directions = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)],
    'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]
}


def travel_in_pipes(loc, pipes_visited: list):
    pipes_visited.append(loc)
    char = pipe_map[loc]
    # replacing the character with a number for the step, that way I don't revisit this place
    pipe_map[loc] = len(pipes_visited) - 1
    new_loc = None
    for deltas in pipe_directions[char]:
        new_loc_option = (loc[0] + deltas[0], loc[1] + deltas[1])
        if (new_loc_option in pipe_map) and (new_loc_option not in pipes_visited) and pipe_map[new_loc_option] != '.':
            new_loc = new_loc_option
    # if I get back to start position, return the list of pipes visited
    if new_loc:
        return travel_in_pipes(new_loc, pipes_visited)
    else:
        return pipes_visited


def part_1():
    pipe_path = travel_in_pipes(start_pos, pipes_visited=[])
    return int(len(pipe_path) / 2)


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
