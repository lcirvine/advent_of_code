import os
from collections import defaultdict


def read_input(file: str):
    caves = defaultdict(list)
    with open(os.path.join('inputs', file)) as f:
        for i in f.read().split('\n'):
            c1, c2 = i.split('-')
            if c2 != 'start':
                caves[c1].append(c2)
            if c1 != 'start':
                caves[c2].append(c1)
    return caves


def part_1():
    caves = read_input('day12_test.txt')
    all_paths = []



def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
