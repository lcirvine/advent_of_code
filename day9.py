import os
from math import prod


def read_input(file: str):
    height = {}
    with open(os.path.join('inputs', file)) as f:
        for x, row in enumerate(f.read().split('\n')):
            for y, val in enumerate(row):
                height[(x, y)] = int(val)
    return height


height = read_input('day9.txt')


def neighbours(x, y):
    return filter(lambda n: n in height,
                  [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)])  # remove points outside grid


def is_low(p):
    return all(height[p] < height[n] for n in neighbours(*p))


low_points = list(filter(is_low, height))


def part_1():
    return sum(height[p] + 1 for p in low_points)


def part_2():

    def count_basin(p):
        if height[p] == 9:
            return 0  # stop counting at ridge
        del height[p]  # prevent further visits
        return 1 + sum(map(count_basin, neighbours(*p)))

    basins = [count_basin(p) for p in low_points]
    return prod(sorted(basins)[-3:])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
