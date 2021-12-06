import os

with open(os.path.join('Inputs', 'day_6.txt')) as f:
    groups = f.read().split('\n\n')


def part_1():
    total = 0
    for group in groups:
        total += len([x for x in list(set(group)) if x != '\n'])
    return total


def part_2():
    total = 0
    for group in groups:
        common_chars = [x for x in list(set(group)) if x != '\n']
        for person in group.split('\n'):
            common_chars = [x for x in common_chars if x in person]
        total += len(common_chars)
    return total


if __name__ == '__main__':
    print(part_1())
    print(part_2())
