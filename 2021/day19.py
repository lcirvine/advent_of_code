import re
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 19
data = get_input(day_num, test=True)
workflow_list, ratings = [x.splitlines() for x in data.split('\n\n')]

workflows = {}
for workflow in workflow_list:
    # k = re.findall(r"(\w*){", workflow)[0]
    k, tests = workflow.split('{')
    for test in tests.strip('}').split(','):
        if ':' in test:
            t, res = test.split(':')
            workflows[t] = res


def evaluate_part(**kwargs):
    x = kwargs.get('x')
    m = kwargs.get('m')
    a = kwargs.get('a')
    s = kwargs.get('s')



def part_1():
    for rating in ratings:
        eval(f"dict({rating.strip('{').strip('}')})")


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
