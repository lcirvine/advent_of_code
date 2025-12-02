import argparse
from datetime import date
import sys
sys.path.append('..')
import re
from aoc_utils import get_input, submit_answer


def get_direction(turn: str):
    return re.search(r'[A-Z]', turn).group()

def get_clicks(turn: str):
    return int(re.search(r'\d+', turn).group())

def new_position(turn: str, current_pos: int):
    direction = get_direction(turn)
    clicks = get_clicks(turn)
    turn_mapping = {
        'L': -1,
        'R': 1
    }
    return current_pos + (clicks * turn_mapping[direction])


def part_1(puzzle_input):
    pos = 50
    num_zeros = 0

    for turn in puzzle_input:
        pos = new_position(turn, pos)
        pos %= 100
        if pos == 0:
            num_zeros += 1

    return num_zeros


def part_2(puzzle_input):
    pos = 50
    num_zeros = 0
    zero_clicks = 0

    for turn in puzzle_input:
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
    parser = argparse.ArgumentParser(description='Advent of Code solution')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    parser.add_argument('-d', '--day_num', type=int, help='Day number for Advent of Code')
    parser.add_argument('-p', '--sep', type=str, default='\n', help='Input separator')
    parser.add_argument('-s', '--submit', action='store_true', help='Submit the answer to Advent of Code')
    args = parser.parse_args()
    if not args.day_num:
        args.day_num = date.today().day

    puzzle_input = get_input(args.day_num, test=args.test).split(args.sep)

    a1 = part_1(puzzle_input)
    a2 = part_2(puzzle_input)
    submit_answer(answer_1=a1, answer_2=a2, day_num=args.day_num, submit=args.submit)