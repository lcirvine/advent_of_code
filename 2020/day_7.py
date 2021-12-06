import os
import re
import collections

with open(os.path.join('Inputs', 'day_7.txt')) as f:
    rules = f.read().split('\n')

contained_in = collections.defaultdict(set)
contains = collections.defaultdict(list)
bag_pat = re.compile(r'^(\d)*\s([a-z\s]*)\sbag')
for rule in rules:
    bag, content_str = rule.split(' bags contain ')
    content_str = [c.replace('.', '').strip() for c in content_str.split(',')]
    for c in content_str:
        if c == 'no other bags':
            pass
        else:
            num, bag_inside = re.search(bag_pat, c).groups()
            contains[bag].append((int(num), bag_inside))
            contained_in[bag_inside].add(bag)


holdsgold = set()


def check(color):
    for c in contained_in[color]:
        holdsgold.add(c)
        check(c)


def part_1():
    check('shiny gold')
    print(len(holdsgold))


def cost(color):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct * cost(inner)
    return total


def part_2():
    print(cost('shiny gold'))


if __name__ == '__main__':
    part_1()
    part_2()
