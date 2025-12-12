import argparse
from datetime import date
from collections import defaultdict
import re
import math
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer


def part_1(puzzle_input):
    homework = defaultdict(list)
    for row in puzzle_input:
        for i, num in enumerate(list(map(int, re.findall(r'\d+', row)))):
            homework[i].append(num)
    operations = re.findall(r'[\*\+]', puzzle_input[-1])

    result = 0
    for i, nums in homework.items():
        op = operations[i]
        if op == '*':
            result += math.prod(nums)
        elif op == '+':
            result += sum(nums)

    return result


def part_2(puzzle_input):
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code solution')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    parser.add_argument('-d', '--day_num', type=int, help='Day number for Advent of Code')
    parser.add_argument('-p', '--sep', type=str, default='\n', help='Input separator')
    parser.add_argument('-s', '--submit', action='store_true', help='Submit the answer to Advent of Code')
    args = parser.parse_args()
    if not args.day_num:
        args.day_num = date.today().day

    puzzle_input = get_input(day_num=args.day_num, test=args.test).split(args.sep)

    a1 = part_1(puzzle_input)
    a2 = part_2(puzzle_input)
    submit_answer(answer_1=a1, answer_2=a2, day_num=args.day_num, submit=args.submit)