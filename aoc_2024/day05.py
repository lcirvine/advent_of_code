from datetime import date
from collections import defaultdict
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer


day_num = 5
data = get_input(day_num)
rules_text, pages_text = data.split('\n\n')

rules = defaultdict(list)
for r in rules_text.split('\n'):
    k, v = r.split('|')
    rules[int(k)].append(int(v))

# print_instructions = [[int(x) for x in instruction.split(',')] for instruction in pages_text.split('\n')]
print_instructions = []
for instruction in pages_text.split('\n'):
    print_instructions.append([int(x) for x in instruction.split(',')])

def passes_test(page_list):
    for i, p in enumerate(page_list):
        pages_before = page_list[:i]
        page_rules = rules[p]
        if any([x for x in pages_before if x in page_rules]):
            return False
    return True

def get_mid_page(page_list):
    ix_mid = len(page_list) // 2
    return page_list[ix_mid]


def part_1():
    total = 0
    for page_list in print_instructions: 
        if passes_test(page_list):
            total += get_mid_page(page_list)
    return total


def part_2():
    total = 0
    for page_list in print_instructions: 
        if not passes_test(page_list):
            for i, p in enumerate(page_list):
                    pages_before = page_list[:i]
                    page_rules = rules[p]
                    for _ in [x for x in pages_before if x in page_rules]:
                            page_list.remove(p)
                            ix = min([page_list.index(i) for i in rules[p] if i in page_list])
                            page_list.insert(ix, p)
            total += get_mid_page(page_list)
    return total


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
