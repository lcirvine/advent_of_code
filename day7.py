import os


def read_input(file: str):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    return data


def part_1():
    pass


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
