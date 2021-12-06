import os
import pyperclip

with open(os.path.join('Inputs', 'day_1.txt')) as f:
    data = [int(num) for num in f.read().split('\n')]


def part_1():
    results = []
    for x in data:
        for y in data:
            if x + y == 2020:
                results.append(x * y)
    answer = list(set(results))[0]
    print(answer)
    pyperclip.copy(answer)


def part_1_alt():
    results = [x * y for x in data for y in data if x + y == 2020]
    answer = list(set(results))[0]
    print(answer)


def part_2():
    for x in data:
        for y in data:
            for z in data:
                if x + y + z == 2020:
                    result = x * y * z
                    print(result)
                    pyperclip.copy(result)


def part_2_alt():
    results = [x * y * z for x in data for y in data for z in data if x + y + z == 2020]
    answer = list(set(results))[0]
    print(answer)


if __name__ == '__main__':
    part_1()
    part_1_alt()
    part_2()
    part_2_alt()
