from datetime import date
from collections import Counter
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = date.today().day
data = get_input(day_num)

l1 = []
l2 = []
for location in data.split('\n'):
    id_1, id_2 = location.split('   ')
    l1.append(int(id_1))
    l2.append(int(id_2))
l1.sort()
l2.sort()


def part_1():
    return sum([abs(x - y) for x, y in zip(l1, l2)])


def part_2():
    l2_ct = Counter(l2)
    return sum([x * l2_ct[x] for x in l1])


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
