from aoc_inputs import get_input

movements = get_input(day_num=17, test=True)
shapes = {
    'minus': [(2, 0), (3, 0), (4, 0), (5, 0)],
    'plus': [(2, 1), (3, 0), (3, 1), (3, 2), (4, 1)],
    'el': [(2, 2), (3, 2), (4, 0), (4, 1), (4, 2)],
    'line': [(2, 0), (2, 1), (2, 2), (2, 3)],
    'square': [(2, 0), (2, 1), (3, 0), (3, 1)]
}


def x_movement():
    move_int = {'<': -1, '>': 1}
    for m in movements:
        yield move_int[m]


def gen_rock(y_max: int):
    shapes = [
        [(2, y_max), (3, y_max), (4, y_max), (5, y_max)],
        [(2, y_max - 1), (3, y_max), (3, y_max - 1), (3, y_max - 2), (4, y_max - 1)],
        [(2, y_max - 2), (3, y_max - 2), (4, y_max), (4, y_max - 1), (4, y_max - 2)],
        [(2, y_max), (2, y_max - 1), (2, y_max - 2), (2, y_max - 3)],
        [(2, y_max), (2, y_max - 1), (3, y_max), (3, y_max - 1)]
    ]
    for shape in shapes:
        yield shape


def part_1():
    pass


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
