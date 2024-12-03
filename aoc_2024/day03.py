from datetime import date
import re
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = date.today().day
data = get_input(day_num)

mul_pat = r"mul\((\d{1,3},\d{1,3})\)"
dont_pat = r"don\'t\(\)"
do_pat = r"do\(\)"

def part_1(data: str) -> int:
    mul_instructions = re.findall(mul_pat, data)
    total = 0
    for instr in mul_instructions:
        x, y = instr.split(',')
        total += int(x) * int(y)
    return total


def part_2(data: str) -> int:
    dont_starts = [m.start() for m in re.finditer(dont_pat, data)]
    do_ends = [m.end() for m in re.finditer(do_pat, data)]
    for start in dont_starts:
        end = sorted([de for de in do_ends if de > start])[0]
        data = data[:start] + "X" * (end - start) + data[end:]
    return part_1(data)


if __name__ == '__main__':
    a1 = part_1(data)
    a2 = part_2(data)
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
