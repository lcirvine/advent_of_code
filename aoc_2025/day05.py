import argparse
from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer


def part_1(puzzle_input):
    ingredient_ranges, ingredient_ids = puzzle_input
    fresh_ingredients = []
    for ir in ingredient_ranges.split('\n'):
        start, end = map(int, ir.split('-'))
        fresh_ingredients.append(range(start, end + 1))
    ingredient_ids = list(map(int, ingredient_ids.split('\n')))
    result = set()
    for id in ingredient_ids:
        for r in fresh_ingredients:
            if id in r:
                result.add(id)
    return len(result)


def part_2(puzzle_input):
    ingredient_ranges, _ = puzzle_input
    fresh_ingredients = set()
    for ir in ingredient_ranges.split('\n'):
        start, end = map(int, ir.split('-'))
        fresh_ingredients.update(range(start, end + 1))
    return len(fresh_ingredients)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code solution')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    parser.add_argument('-d', '--day_num', type=int, help='Day number for Advent of Code')
    parser.add_argument('-p', '--sep', type=str, default='\n\n', help='Input separator')
    parser.add_argument('-s', '--submit', action='store_true', help='Submit the answer to Advent of Code')
    args = parser.parse_args()
    if not args.day_num:
        args.day_num = date.today().day

    puzzle_input = get_input(day_num=args.day_num, test=args.test).split(args.sep)

    a1 = part_1(puzzle_input)
    a2 = part_2(puzzle_input)
    submit_answer(answer_1=a1, answer_2=a2, day_num=args.day_num, submit=args.submit)