import re
import numpy as np
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer


data = get_input(day_num=6).split('\n')


def part_1():
    times = [int(t) for t in re.findall(r"(\d*)", data[0]) if t]
    distance_records = [int(d) for d in re.findall(r"(\d*)", data[1]) if d]
    wins_races = []
    for race in range(len(times)):
        t = times[race]
        dr = distance_records[race]
        wins_races.append(len([s for s in range(1, t) if ((t - s) * s) > dr]))
    return np.prod(wins_races)


def part_2():
    t = int(''.join([t for t in re.findall(r"(\d)", data[0]) if t]))
    dr = int(''.join([d for d in re.findall(r"(\d)", data[1]) if d]))
    """
    d = (t - s) * s
    d = t*s - s**2
    d' = t - 2s
    d'' = -2
    speed to get max distance = t/2
    """
    ways_to_win = 0
    for s in range(1, t):
        d = (t - s) * s
        if d > dr:
            ways_to_win += 1
    return ways_to_win


if __name__ == '__main__':
    a1 = part_1()
    print(a1)
    # submit_answer(part=1, answer=a1, day_num=6)
    a2 = part_2()
    print(a2)
    # submit_answer(part=2, answer=a2, day_num=6)
