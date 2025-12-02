import sys
sys.path.append('..')
import re
from aoc_utils import get_input, submit_answer

day_num = 1
data = get_input(day_num).split('\n')

turn_mapping = {
    'L': -1,
    'R': 1
}

def get_direction(turn: str):
    return re.search(r'[A-Z]', turn).group()

def get_clicks(turn: str):
    return int(re.search(r'\d+', turn).group())

def new_position(turn: str, current_pos: int):
    direction = get_direction(turn)
    clicks = get_clicks(turn)
    return current_pos + (clicks * turn_mapping[direction])


def part_1():
    pos = 50
    num_zeros = 0

    for turn in data:
        pos = new_position(turn, pos)
        pos %= 100
        if pos == 0:
            num_zeros += 1

    return num_zeros


def part_2():
    pos = 50
    num_zeros = 0
    zero_clicks = 0

    for turn in data:
        direction = get_direction(turn)
        clicks = get_clicks(turn)
        # if turning left, reverse position
        if direction == 'L':
            pos = (100 - pos) % 100
        pos += clicks
        zero_clicks += pos // 100
        pos %= 100
        # part 1
        if pos == 0:
            num_zeros += 1
        # reverse back after finding new position
        if direction == 'L':
            pos = (100 - pos) % 100
    
    return zero_clicks


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
