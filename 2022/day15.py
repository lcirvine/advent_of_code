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
    return dict(sorted(signal_map.items()))


def signal_area(signal: tuple, dist: int):
    """
    Don't do this. Your computer will freeze.
    """
    sx, sy = signal
    signal_area = []
    for distx in range(dist + 1):
        for disty in range(dist - distx + 1):
            signal_area.extend([
                (sx - distx, sy - disty),
                (sx + distx, sy - disty),
                (sx - distx, sy + disty),
                (sx + distx, sy + disty)
            ])
    return list(set(signal_area))


def signal_borders(signal: tuple, dist: int, max_val: int):
    sx, sy = signal
    # want to be outside the border
    # dist += 1
    borders = []
    for dx in range(dist + 1):
        dy = dist - dx
        borders.extend([
            (sx - dx, sy - dy),
            (sx + dx, sy - dy),
            (sx - dx, sy + dy),
            (sx + dx, sy + dy)
        ])
    borders = list(set([b for b in borders if b[0] in range(0, max_val) and b[1] in range(0, max_val)]))
    return borders


def outside_signal_area(loc: tuple, signal_map: dict = None):
    outside = []
    x, y = loc
    for sig, sigattrs in signal_map.items():
        sx, sy = sig
        dist = sigattrs['distance']
        # is this even in range of the signal?
        if (abs(x - sx) + abs(x - sy)) > dist:
            outside.append(True)
        else:
            outside.append(False)
            break
    return all(outside)


def part_1(test=True):
    """
    Triangles!!!
    """
    unavail = set()
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
                unavail.add((bx, y_val))
    # remove x values if there is already a beacon there
    for beacon in unavail.intersection(beacon_pos):
        unavail.remove(beacon)
    return len(unavail)


def part_2(test=True):
    signal_map = get_signal_map(test=test)
    if test:
        max_val = 20
    else:
        max_val = 4000000
    for sig, sigattrs in signal_map.items():
        borders = signal_borders(sig, sigattrs['distance'], max_val)
        for loc in borders:
            if outside_signal_area(loc, signal_map):
                print(loc)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
