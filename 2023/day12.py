import re
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 12
data = get_input(day_num, test=True)


def part_1():
    spring_cond_map = {'.': 'operational', '#': 'damaged', '?': 'unknown'}
    for row in data.splitlines():
        springs, group_nums = row.split()
        springs = springs.strip('.')
        group_nums = [int(x) for x in group_nums.split(',')]

        g_wrk = len([s for s in re.findall(r"(\.*)", springs) if s != ''])
        n_dam = len([s for s in re.findall(r"(\#)", springs) if s != ''])
        n_unk = len([s for s in re.findall(r"(\?)", springs) if s != ''])
        g_unk = len([s for s in re.findall(r"(\?*)", springs) if s != ''])

        # the unknowns have to be either damaged (#) or functional (.)
        # groups of damaged springs (#) have to be separated by functional springs (.)
        # number of groups of '#' is given as the len(group_nums), minus 1 because we want number of '.' between groups
        # number of unknowns - remaining damaged - number of groups of functional + 1 to get number of ways

        # ways = n_unk - (sum(group_nums) - n_dam) - (len(group_nums) - g_wrk - 1) + 1

        dam_remaining = sum(group_nums) - n_dam
        group_wrk_remaining = len(group_nums) - g_wrk - 1

        ways = n_unk - dam_remaining - group_wrk_remaining
        print(ways)


def test(row: str):
    springs, group_nums = row.split()
    springs = springs.strip('.')
    group_nums = [int(x) for x in group_nums.split(',')]

    g_wrk = len([s for s in re.findall(r"(\.*)", springs) if s != ''])
    n_dam = len([s for s in re.findall(r"(\#)", springs) if s != ''])
    n_unk = len([s for s in re.findall(r"(\?)", springs) if s != ''])

    # the unknowns have to be either damaged (#) or functional (.)
    # groups of damaged springs (#) have to be separated by functional springs (.)
    # the number of groups of '#' is given as the len(group_nums), minus 1 because we want number of '.' between groups
    # number of unknowns - remaining damaged - number of groups of functional
    ways = n_unk - (sum(group_nums) - n_dam) - (len(group_nums) - g_wrk - 1) + 1
    return ways


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
