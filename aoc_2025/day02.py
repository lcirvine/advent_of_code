from datetime import date
import sys
import argparse
sys.path.append('..')
from aoc_utils import get_input, submit_answer


def part_1(puzzle_input):
    sum_invalid = 0
    for rng in puzzle_input:
        start = int(rng.split('-')[0])
        end = int(rng.split('-')[1])
        for product_id in range(start, end + 1):
            str_id = str(product_id)
            half_len = int(len(str_id) / 2)
            if str_id[:half_len] == str_id[half_len:]:
                sum_invalid += product_id
    return sum_invalid


def part_2(puzzle_input):
    # don't double count IDs like 222222
    invalid_prod_ids = set()
    for rng in puzzle_input:
        start = int(rng.split('-')[0])
        end = int(rng.split('-')[1])
        for product_id in range(start, end + 1):
            str_id = str(product_id)
            for i in range(1, len(str_id)):
                if len(str_id) % i == 0:
                    num = str_id[:i]
                    if str_id == num * (len(str_id) // i):
                        invalid_prod_ids.add(product_id)
    return sum(invalid_prod_ids)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code solution')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    parser.add_argument('-d', '--day_num', type=int, help='Day number for Advent of Code')
    parser.add_argument('-p', '--sep', type=str, default=',', help='Input separator')
    parser.add_argument('-s', '--submit', action='store_true', help='Submit the answer to Advent of Code')
    args = parser.parse_args()
    if not args.day_num:
        args.day_num = date.today().day

    puzzle_input = get_input(day_num=args.day_num, test=args.test).split(args.sep)

    a1 = part_1(puzzle_input)
    a2 = part_2(puzzle_input)
    submit_answer(answer_1=a1, answer_2=a2, day_num=args.day_num, submit=args.submit)