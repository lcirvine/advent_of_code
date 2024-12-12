from datetime import date
from collections import deque
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 9
data = get_input(day_num, test=True)
# removing the last number of spaces if there is an even number of characters
if len(data) % 2 == 0:
    data = data[:-1]

files = deque([data[x] for x in range(0, len(data), 2)])
files = deque([str(i) * int(num) for i, num in enumerate(files)])
spaces = deque([data[x] for x in range(1, len(data), 2)])

whole_string = ''
for i in range(len(spaces)):
    whole_string += files[i] 
    whole_string += '.' * int(spaces[i])

if len(files) > len(spaces):
    whole_string += files[-1]

space_count = whole_string.count('.')
right_string = whole_string[:(space_count + 1) * -1: -1].replace('.', '')
right_deque = deque(right_string)
left_string = whole_string[: len(whole_string) - space_count]

for i in range(left_string.count('.')):
    left_string = left_string.replace('.', right_deque.popleft(), 1)


def part_1():
    checksum = 0
    for i, char in enumerate(left_string):
        checksum += (i * int(char))
    return checksum


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
