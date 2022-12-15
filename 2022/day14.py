from aoc_inputs import get_input
import sys

sys.setrecursionlimit(10**6)


def rock_map(test=False) -> list:
    rock_paths = get_input(day_num=14, test=test).split('\n')
    rocks = []
    for r_path in rock_paths:
        r_points = r_path.split(' -> ')
        for pt in range(len(r_points) - 1):
            xcur = int(r_points[pt].split(',')[0])
            ycur = int(r_points[pt].split(',')[1])
            xnxt = int(r_points[pt + 1].split(',')[0])
            ynxt = int(r_points[pt + 1].split(',')[1])
            for x in range(min(xcur, xnxt), max(xcur, xnxt) + 1):
                for y in range(min(ycur, ynxt), max(ycur, ynxt) + 1):
                    rocks.append((x, y))
    rocks = list(set(rocks))
    rocks.sort()
    return rocks


class Cave:
    def __init__(self, test=False):
        self.rocks = rock_map(test=test)
        self.blockage = self.rocks.copy()
        self.sand = []
        self.rymax = max([r[1] for r in self.rocks])
        self.rymin = min([r[1] for r in self.rocks])
        self.rxmin = min([r[0] for r in self.rocks])
        self.rxmax = max([r[0] for r in self.rocks])
        self.sand_start = (500, 0)

    def next_loc(self, loc: tuple):
        sx, sy = loc
        nloc = list(filter(lambda n: n not in self.blockage, [(sx, sy + 1), (sx - 1, sy + 1), (sx + 1, sy + 1)]))
        if nloc:
            return nloc[0]

    def not_in_abyss(self, loc: tuple):
        sx, sy = loc
        rocks_below = [r for r in self.rocks if r[0] == sx and r[1] > sy]
        if rocks_below and len(self.sand) < 75:
            return True
        else:
            return False

    def sand_fall(self, loc: tuple = None):
        if loc is None:
            loc = self.sand_start
        if self.not_in_abyss(loc):
            nloc = self.next_loc(loc)
            if not nloc:
                self.blockage.append(loc)
                self.sand.append(loc)
            return self.sand_fall(nloc)

    def return_sand_amount(self):
        return len(set(self.sand))

    def create_visualization(self):
        with open(r"inputs/day14_visualization.txt", 'w') as f:
            for y in range(0, self.rymax + 1):
                for x in range(self.rxmin - 1, self.rxmax + 2):
                    if x == 500 and y == 0:
                        f.write('+ ')
                    elif (x, y) in self.rocks:
                        f.write('# ')
                    elif (x, y) in self.sand:
                        f.write('O ')
                    else:
                        f.write('. ')
                f.write('\n')


def part_1():
    c = Cave()
    c.sand_fall()
    c.create_visualization()
    return c.return_sand_amount()


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
