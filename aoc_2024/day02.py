from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = date.today().day
data = get_input(day_num)

reports = []
for row in data.split('\n'):
    reports.append([int(x) for x in row.split(' ')])

def safety_check(report: list) -> int:
    assessment = 0
    diff = [report[i + 1] - report[i] for i in range(0, len(report) - 1)]
    if all(x > 0 for x in diff): 
        if min(diff) >= 1 and max(diff) <= 3:
            assessment = 1
    elif all(x < 0 for x in diff):
        if min(diff) >= -3 and max(diff) <= -1:
            assessment = 1
    return assessment


def part_1():
    return sum([safety_check(report) for report in reports])


def part_2():
    total = 0
    for report in reports: 
        report_combo = [report]
        report_combo.extend([report[:i] + report[i + 1: ] for i in range(len(report))])
        total += max(list(map(safety_check, report_combo)))
    return total


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
