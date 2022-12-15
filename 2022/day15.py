from aoc_inputs import get_input
import re


def get_signal_map(test=False):
    sensor_data = get_input(day_num=15, test=test).split('\n')
    signal_map = {}
    for sensor in sensor_data:
        sx, bx = [int(x) for x in re.findall(r"x=([\-\d]*)", sensor)]
        sy, by = [int(y) for y in re.findall(r"y=([\-\d]*)", sensor)]
        dist = abs(sx - bx) + abs(sy - by)
        signal_map[(sx, sy)] = {'beacon': (bx, by), 'distance': dist}
    return signal_map


def signal_area(signal: tuple, beacon: tuple, dist: int):
    """
    Don't do this. Your computer will freeze.
    """
    sx, bx = signal
    sy, by = beacon
    signal_area = []
    for distx in range(dist + 1):
        for disty in range(dist - distx + 1):
            sa_locs = [
                (sx - distx, sy - disty),
                (sx + distx, sy - disty),
                (sx - distx, sy + disty),
                (sx + distx, sy + disty)
            ]
            signal_area.extend(list(filter(lambda n: n != (bx, by), sa_locs)))
    return list(set(signal_area))


def part_1(test=False):
    """
    Triangles!!!
    """
    unavail = []
    if test:
        y_val = 10
    else:
        y_val = 2000000
    signal_map = get_signal_map(test=test)
    beacon_pos = set([b['beacon'] for s, b in signal_map.items()])
    for sig, sigattrs in signal_map.items():
        # if the signal area would cross the y_val
        if y_val in range(sig[1] - sigattrs['distance'], sig[1] + sigattrs['distance'] + 1):
            sx, sy = sig
            dist = sigattrs['distance']
            triangle_base = dist - abs(sy - y_val)
            for bx in range(sx - triangle_base, sx + triangle_base + 1):
                unavail.append((bx, y_val))
    # remove duplicates
    unavail = set(unavail)
    # remove x values if there is already a beacon there
    for beacon in unavail.intersection(beacon_pos):
        unavail.remove(beacon)
    return len(unavail)


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
