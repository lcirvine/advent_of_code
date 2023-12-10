import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 9
data = get_input(day_num).split('\n')
readings = []
for row in data:
    readings.append([int(x) for x in row.split(' ')])


def find_next_num(nums: list, last_diffs=None):
    if not last_diffs:
        last_diffs = []
    diffs = [nums[x + 1] - nums[x] for x in range(len(nums) - 1)]
    last_diffs.append(diffs[-1])
    if all([d == 0 for d in diffs]):
        return sum(last_diffs)
    else:
        return find_next_num(nums=diffs, last_diffs=last_diffs)


def find_prev_num(nums: list, first_diffs=None):
    if not first_diffs:
        first_diffs = []
    diffs = [nums[x + 1] - nums[x] for x in range(len(nums) - 1)]
    first_diffs.append(diffs[0])
    if all([d == 0 for d in diffs]):
        return sum(first_diffs[::2]) - sum(first_diffs[1::2])
    else:
        return find_prev_num(nums=diffs, first_diffs=first_diffs)


def part_1():
    next_nums = []
    for r in readings:
        next_nums.append(r[-1] - find_next_num(r))
    return sum(next_nums)


def part_2():
    prev_nums = []
    for r in readings:
        prev_nums.append(r[0] - find_prev_num(r))
    return sum(prev_nums)


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
