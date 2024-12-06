from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = date.today().day
data = get_input(day_num)

guard_map = {}
for y, row in enumerate(data.split('\n')):
    for x, char in enumerate(row):
        guard_map[(x, y)] = char
        if char == '^':
            guard_pos = (x, y)


def turn_right(current_direction): 
    directions = [
        (0, -1),   # up 
        (1, 0),    # right
        (0, 1),    # down
        (-1, 0)    # left
    ]
    ix_current = directions.index(current_direction)
    ix_next = (ix_current + 1) % 4
    return directions[ix_next]


def part_1():
    direction = (0, -1)  # up
    visited = set()
    while guard_pos in guard_map:
        visited.add(guard_pos)
        x, y = guard_pos
        nx = x + direction[0]
        ny = y + direction[1]
        if guard_map.get((nx, ny)) == '#':
            direction = turn_right(direction)
        else:
            guard_pos = (nx, ny)
    return len(visited)


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
