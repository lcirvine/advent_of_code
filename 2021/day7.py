import os
from collections import Counter


def read_input(file: str = 'day7.txt'):
    with open(os.path.join('inputs', file)) as f:
        data = [int(x) for x in f.read().split(',')]
    return data


def part_1():
    crab_pos = read_input(file='day7.txt')
    fuel_consumed = {}
    for i in range(min(crab_pos), max(crab_pos) + 1):
        fuel = 0
        for crab in crab_pos:
            fuel += abs(i - crab)
        fuel_consumed[i] = fuel
    return min(fuel_consumed.values())


def part_2_weighted_average():
    """
    I thought the crabs would move to the weighted average position which was so close but ultimately wrong.
    It will work with the example data though.
    Using my input the weighted average rounds to 486 which would have a fuel consumption of 89791190.
    The actual answer was a position of 467 with a fuel consumption of 89791146.
    :return:
    """
    crab_pos = read_input(file='day7.txt')
    ct = Counter(crab_pos)
    wt = 0
    for i, w in ct.items():
        wt += i * w
    wa = round(wt / len(crab_pos))
    fuel_consumed = 0
    for crab in crab_pos:
        for i in range(abs(crab - wa) + 1):
            fuel_consumed += i
    return fuel_consumed


def part_2():
    crab_pos = read_input(file='day7.txt')
    fuel_consumed = {}
    for i in range(min(crab_pos), max(crab_pos) + 1):
        fuel = 0
        for crab in crab_pos:
            # Thanks Gauss!
            diff = abs(i - crab)
            fuel += (diff * (diff + 1))/2
        fuel_consumed[i] = fuel
    return int(min(fuel_consumed.values()))


if __name__ == '__main__':
    print(part_1())
    print(part_2_weighted_average())
    print(part_2())
