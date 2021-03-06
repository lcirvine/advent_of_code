import os
from collections import Counter

"""Needed help with part 2. I did set the problem up correctly and I was on the right track."""


def read_input(file: str):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    template = [x for x in data.pop(0)]
    data.remove('')
    rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in data}
    return template, rules


def part_1():
    template, rules = read_input('day14.txt')
    for step in range(10):
        insert_chars = [rules[template[x] + template[x + 1]] for x in range(len(template) - 1)]
        pos = [x for x in range(1, len(template) + len(insert_chars), 2)]
        insert_temp = dict(zip(pos, insert_chars))
        for pos, char in insert_temp.items():
            template.insert(pos, char)
    ct = Counter(template)
    return max(ct.values()) - min(ct.values())


def part_2():
    template, rules = read_input('day14.txt')
    chars = Counter(template)
    pairs = Counter([template[x] + template[x + 1] for x in range(len(template) - 1)])
    for _ in range(40):
        for (a, b), c in pairs.copy().items():
            x = rules[a + b]
            pairs[a + b] -= c
            pairs[a + x] += c
            pairs[x + b] += c
            chars[x] += c
    return max(chars.values()) - min(chars.values())


if __name__ == '__main__':
    print(part_1())
    print(part_2())
