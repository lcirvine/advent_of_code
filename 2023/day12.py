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
        # removing '.' from ends
        springs = springs.strip('.')
        group_nums = [int(x) for x in group_nums.split(',')]

        # s_wrk = [mo for mo in re.finditer(r"(\.*)", springs) if mo.group()]
        # s_dam = [mo for mo in re.finditer(r"(#*)", springs) if mo.group()]
        # s_unk = [mo for mo in re.finditer(r"(\?*)", springs) if mo.group()]

        n_wrk = len([s for s in re.findall(r"(\.*)", springs) if s != ''])
        n_dam = len([s for s in re.findall(r"(\#*)", springs) if s != ''])
        n_unk = len([s for s in re.findall(r"(\?*)", springs) if s != ''])

        ways = n_unk - (sum(group_nums) - n_dam) - (len(group_nums) - n_wrk) + 1

        total_dam = sum(group_nums)
        missing_dam = total_dam - len(s_dam)


def test(row: str):
    springs, group_nums = row.split()
    # removing '.' from ends
    springs = springs.strip('.')
    group_nums = [int(x) for x in group_nums.split(',')]

    g_wrk = len([s for s in re.findall(r"(\.*)", springs) if s != ''])
    n_dam = len([s for s in re.findall(r"(\#)", springs) if s != ''])
    n_unk = len([s for s in re.findall(r"(\?)", springs) if s != ''])

    return n_unk - (sum(group_nums) - n_dam) - (len(group_nums) - g_wrk) + 1



def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
