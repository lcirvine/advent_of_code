import argparse
from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = date.today().day
data = get_input(day_num)


def part_1(puzzle_input):
    total_joltage = 0
    for bank in puzzle_input:
        num_1 = max(bank[:len(bank) - 1])
        num_2 = max(bank[bank.index(num_1) + 1:])
        total_joltage += int(num_1 + num_2)
    return total_joltage


def part_2(puzzle_input):
    total_joltage = 0

    for bank in puzzle_input:
        joltage = ''
        while len(joltage) < 12:
            # make sure you have enough numbers left in the bank to complete a 12-digit joltage
            end_index = len(bank) - (11 - len(joltage))
            next_num = max(bank[:end_index])
            joltage += next_num
            # remove used numbers and all preceding numbers from bank
            bank = bank[bank.index(next_num) + 1:]

        total_joltage += int(joltage)

    return total_joltage


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