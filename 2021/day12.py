import os
from collections import defaultdict

"""
Had to get significant help with both parts of this puzzle. 
"""


def read_input(file: str):
    caves = defaultdict(list)
    with open(os.path.join('inputs', file)) as f:
        for i in f.read().split('\n'):
            c1, c2 = i.split('-')
            caves[c1].append(c2)
            caves[c2].append(c1)
    return caves


caves = read_input('day12.txt')


def cave_count(part, seen=[], cave='start'):
    if cave == 'end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1
    return sum(cave_count(part, seen+[cave], n) for n in caves[cave])


if __name__ == '__main__':
    print(cave_count(part=1))
    print(cave_count(part=2))
