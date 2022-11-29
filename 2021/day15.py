import os


def read_input(file: str):
    cave = {}
    with open(os.path.join('inputs', file)) as f:
        for x, row in enumerate(f.read().split('\n')):
            for y, risk in enumerate(row):
                cave[(x, y)] = int(risk)
    return cave





def part_1():
    cave = read_input('day15_test.txt')
    start = [c for c in cave][0]
    destination = [c for c in cave][-1]
    unvisited = {}

    def neighbors(coord):
        x, y = coord
        # return filter(lambda n: n in cave, [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)])
        return filter(lambda n: n in cave, [(x, y + 1), (x + 1, y)])

    all_risks = []


    def cave_risk(loc, path: list = [], risk=0):
        if loc == destination:
            all_risks.append(risk)
        else:
            risk += cave[loc]
            path.append(loc)
            for n in neighbors(loc):
                return cave_risk(n, path, risk)

    cave_risk(loc=start, risk=(0 - cave[start]))

    return min(all_risks)



def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
