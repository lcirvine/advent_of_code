import os
import re

with open(os.path.join('inputs', 'day2.txt')) as f:
    course = f.read().split('\n')


with open(os.path.join('inputs', 'day2_test.txt')) as f:
    test_course = f.read().split('\n')

pat_num = r"(\d*)$"
# could also just do r"(\d)" but wanted to capture all digits in case of larger numbers
# including $ so that I get only one match for number at end of string


def part_1(course_input: list, x_pos: int = 0, y_pos: int = 0):
    for i in course_input:
        num = int(re.findall(pat_num, i)[0])
        if 'forward' in i:
            x_pos += num
        elif 'down' in i:
            y_pos += num
        elif 'up' in i:
            y_pos -= num
    return x_pos * y_pos


def part_2(course_input: list, x_pos: int = 0, y_pos: int = 0, aim: int = 0):
    for i in course_input:
        num = int(re.findall(pat_num, i)[0])
        if 'down' in i:
            aim += num
        elif 'up' in i:
            aim -= num
        elif 'forward' in i:
            x_pos += num
            if aim > 0:
                y_pos += (aim * num)
            elif aim < 0:
                y_pos -= (aim * num)
    return x_pos * y_pos


if __name__ == '__main__':
    print(part_1(course))
    print(part_2(course))
