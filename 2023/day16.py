from collections import Counter
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 16
data = get_input(day_num, test=True)

cave_map = {}
for row_num, row in enumerate(data.splitlines()):
    for col_num, char in enumerate(row):
        cave_map[(col_num, row_num)] = {'char': char, 'visited': 0}


def get_next_pos(current_pos, prev_pos):
    cave_map[current_pos]['visited'] += 1
    new_positions = []
    current_char = cave_map[current_pos]['char']
    delta_x, delta_y = (current_pos[0] - prev_pos[0], current_pos[1] - prev_pos[1])
    # right: delta_x == 1
    # left: delta_x == -1
    # remember top will have lower y value than bottom!
    # up: delta_y == -1
    # down: delta_y == 1
    if current_char == '\\':
        # hit a mirror and change x and y directions
        new_positions.append((current_pos[0] + delta_y, current_pos[1] + delta_x))
    elif current_char == '/':
        # hit a mirror and change x and y directions in inverse
        new_positions.append((current_pos[0] + delta_y * -1, current_pos[1] + delta_x * -1))
    elif current_char == '-' and delta_y:
        # moving vertically and hit a horizontal splitter
        new_positions.append((current_pos[0] + 1, current_pos[1]))
        new_positions.append((current_pos[0] - 1, current_pos[1]))
    elif current_char == '|' and delta_x:
        # moving horizontally and hit a vertical splitter
        new_positions.append((current_pos[0], current_pos[1] + 1))
        new_positions.append((current_pos[0], current_pos[1] - 1))
    else:
        # continue in same direction
        new_positions.append((current_pos[0] + delta_x, current_pos[1] + delta_y))
    # remove new_positions not on map
    for new_position in [np for np in new_positions if np in cave_map]:
        return get_next_pos(new_position, current_pos)


def part_1():
    get_next_pos(current_pos=(0, 0), prev_pos=(-1, 0))
    places_visited = [loc for loc, vals in cave_map.items() if vals['visited'] > 0]
    return len(places_visited)


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
