import re
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 19
data = get_input(day_num)
workflow_list, ratings_list = [x.splitlines() for x in data.split('\n\n')]

workflows = {}
for workflow in workflow_list:
    k, tests = workflow.split('{')
    test_list = []
    for test in tests.strip('}').split(','):
        if ':' in test:
            t, res = test.split(':')
            test_list.append((t, res))
        else:
            # there will always be one test result that evaluates to True
            test_list.append(('True', test))
    workflows[k] = test_list


def evaluate_part(wf_key: str = 'in', **kwargs):
    x = kwargs.get('x')
    m = kwargs.get('m')
    a = kwargs.get('a')
    s = kwargs.get('s')
    for test in workflows[wf_key]:
        if eval(test[0]):
            test_result = test[1]
            break
    # there will always be one test result that evaluates to True
    if test_result == 'A':
        return sum((x, m, a, s))
    elif test_result == 'R':
        return 0
    else:
        return evaluate_part(test_result, **kwargs)


def part_1():
    total = 0
    for part in ratings_list:
        ratings = eval(f"dict({part.strip('{').strip('}')})")
        part_val = evaluate_part(**ratings)
        total += part_val
    return total


def part_2():
    xmas_values = {}
    pat_accepted = r"([xmas][<>]\d*):A"
    pat_rejected = r"([xmas][<>]\d*):R"
    accepted = re.findall(pat_accepted, data)
    rejected = re.findall(pat_rejected, data)
    for rating in ('x', 'm', 'a', 's'):
        min_val_accepted = min([int(r.split(f"{rating}>")[1]) for r in accepted if r.startswith(f"{rating}>")] + [4000])
        min_val_rejected = max([int(r.split(f"{rating}>")[1]) for r in rejected if r.startswith(f"{rating}<")] + [1])
        min_val = max(min_val_rejected, min_val_accepted)
        print(f"{rating} - min value {min_val}")

if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
