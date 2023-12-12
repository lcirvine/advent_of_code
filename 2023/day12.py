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

        # there are num_s characters in the springs
        num_s = len(springs)
        # there are num_s_dam functional springs
        num_s_fct = sum(group_nums)

        s_opp = [mo for mo in re.finditer(r"(\.*)", row) if mo.group()]
        s_dam = [mo for mo in re.finditer(r"(#*)", row) if mo.group()]
        s_dam = [mo for mo in re.finditer(r"(\?*)", row) if mo.group()]


        # there are num_s_fct_group groups of functional springs
        num_s_fct_group = len(s_fct)
        # there are
        num_s_dam = len(s_dam)






def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
