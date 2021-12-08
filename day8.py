import os

display = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],          # 6
    1: ['c', 'f'],                              # 2
    2: ['a', 'c', 'd', 'e', 'g'],               # 5
    3: ['a', 'c', 'd', 'f', 'g'],               # 5
    4: ['b', 'c', 'd', 'f'],                    # 4
    5: ['a', 'b', 'd', 'f', 'g'],               # 5
    6: ['a', 'b', 'd', 'e', 'f', 'g'],          # 6
    7: ['a', 'c', 'f'],                         # 3
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],     # 7
    9: ['a', 'b', 'c', 'd', 'f', 'g']           # 6
}


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
