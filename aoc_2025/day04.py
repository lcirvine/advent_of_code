import argparse
from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer


def create_char_map(puzzle_input: str) -> dict[tuple[int, int], str]:
    char_map = {}
    for y, row in enumerate(puzzle_input.split('\n'), 0):
        for x, char in enumerate(row, 0):
            char_map[(x, y)] = char
    return char_map


def neighbor_coord(pos: tuple[int, int], include_diagonals: bool = True) -> list[tuple[int, int]]:
    x, y = pos
    if include_diagonals:
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
    else:
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def get_neighbors(char_map: dict[tuple[int, int], str], pos: tuple[int, int]) -> list[str]:
    return [char_map[p] for p in neighbor_coord(pos) if p in char_map]


def part_1(puzzle_input):
    accessable_rolls = set()
    char_map = create_char_map(puzzle_input)
    for pos in char_map:
        if char_map[pos] == '@':
            neighbors = get_neighbors(char_map, pos)
            num_neighbor_rolls = len([n for n in neighbors if n == '@'])
            if num_neighbor_rolls < 4:
                accessable_rolls.add(pos)
    return len(accessable_rolls)


def part_2(puzzle_input):
    accessable_rolls = set()
    removable_rolls = True
    char_map = create_char_map(puzzle_input)
    while removable_rolls:
        removable_rolls = False
        for pos in char_map:
            if char_map[pos] == '@':
                neighbors = get_neighbors(char_map, pos)
                num_neighbor_rolls = len([n for n in neighbors if n == '@'])
                if num_neighbor_rolls < 4:
                    accessable_rolls.add(pos)
                    char_map[pos] = 'x'
                    removable_rolls = True
    return len(accessable_rolls)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code solution')
    parser.add_argument('-t', '--test', action='store_true', help='Use test input')
    parser.add_argument('-d', '--day_num', type=int, help='Day number for Advent of Code')
    parser.add_argument('-s', '--submit', action='store_true', help='Submit the answer to Advent of Code')
    args = parser.parse_args()
    if not args.day_num:
        args.day_num = date.today().day

    puzzle_input = get_input(day_num=args.day_num, test=args.test)

    a1 = part_1(puzzle_input)
    a2 = part_2(puzzle_input)
    submit_answer(answer_1=a1, answer_2=a2, day_num=args.day_num, submit=args.submit)