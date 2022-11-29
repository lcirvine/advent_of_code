import os

# line segment format
# x1,y1 -> x2,y2


def read_input(file: str = 'day5.txt'):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    lines = {}
    for i, line in enumerate(data):
        c1, c2 = line.split(' -> ')
        x1, y1 = c1.split(',')
        x2, y2 = c2.split(',')
        lines[i] = [(int(x1), int(y1)), (int(x2), int(y2))]
    return lines


def part_1():
    # horizontal and vertical lines only
    lines = read_input()
    intersections = {}
    for i, line in lines.items():
        x1, y1 = line[0]
        x2, y2 = line[1]
        # horizontal
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                try:
                    intersections[(x1, y)] += 1
                except KeyError:
                    intersections[(x1, y)] = 1
        # vertical
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                try:
                    intersections[(x, y1)] += 1
                except KeyError:
                    intersections[(x, y1)] = 1
    return len([i for i in intersections.values() if i > 1])


def part_2():
    # horizontal, vertical and 45 degree angle diagonal lines
    lines = read_input(file='day5.txt')
    intersections = {}
    for i, line in lines.items():
        x1, y1 = line[0]
        x2, y2 = line[1]
        # horizontal
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                try:
                    intersections[(x1, y)] += 1
                except KeyError:
                    intersections[(x1, y)] = 1
        # vertical
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                try:
                    intersections[(x, y1)] += 1
                except KeyError:
                    intersections[(x, y1)] = 1
        # diagonal
        elif abs(x2 - x1) == abs(y2 - y1):
            if x2 > x1:
                xs = [x for x in range(x1, x2 + 1)]
            else:
                xs = [x for x in range(x1, x2 - 1, -1)]
            if y2 > y1:
                ys = [y for y in range(y1, y2 + 1)]
            else:
                ys = [y for y in range(y1, y2 - 1, -1)]
            for xy in list(zip(xs, ys)):
                try:
                    intersections[(xy[0], xy[1])] += 1
                except KeyError:
                    intersections[(xy[0], xy[1])] = 1
    return len([i for i in intersections.values() if i > 1])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
