from aoc_inputs import get_input

lava_cubes = get_input(day_num=18).split('\n')

cube_coord = []
for cube in lava_cubes:
    cx, cy, cz = cube.split(',')
    cx = int(cx)
    cy = int(cy)
    cz = int(cz)
    cube_coord.append((cx, cy, cz))


def differences(cube1, cube2):
    return abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2])


def part_1():
    surface = 0
    for cube1 in cube_coord:
        surface += 6
        for cube2 in cube_coord:
            if differences(cube1, cube2) == 1:
                surface -= 1
    return surface


def air_pockets_inside():
    """First attempt at part 2.
    This didn't work because small droplets inside the big bubble still take away from the surface area."""
    surface = part_1()
    air_pockets = []
    # I could slice this in any direction but y seemed to make sense
    for sy in range(min([c[1] for c in cube_coord]), max([c[1] for c in cube_coord]) + 1):
        plane = [(c[0], c[2]) for c in cube_coord if c[1] == sy]
        # air pockets will be in the middle of other points in the plane
        for sx in range(min([s[0] for s in plane]), max([s[0] for s in plane]) + 1):
            for sz in range(min([s[1] for s in plane]), max([s[1] for s in plane]) + 1):
                neighbors = list(filter(lambda n: n in plane, [(sx-1, sz), (sx+1, sz), (sx, sz-1), (sx, sz+1)]))
                if len(neighbors) == 4 and (sx, sz) not in plane:
                    air_pockets.append((sx, sy, sz))
    return surface - (len(air_pockets) * 6)


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
