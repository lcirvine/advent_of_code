from collections import defaultdict
import re
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 15
data = get_input(day_num)


def hash_val(s: str) -> int:
    val = 0
    for char in s:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def part_1():
    value = 0
    for step in data.split(','):
        value += hash_val(step)
    return value


def focusing_power(boxes: dict):
    total = 0
    for box_number, lenses in boxes.items():
        lens_counter = 1
        for lens in lenses:
            lens_power = (box_number + 1) * lens_counter * lens[1]
            lens_counter += 1
            total += lens_power
    return total


def part_2():
    boxes = defaultdict(list)
    pat_label = r"^([a-zA-Z]*)[\-|=]"
    pat_op = r"([\-=])"
    pat_focal_len = r"=(\d*)"
    for step in data.split(','):
        label = re.findall(pat_label, step)[0]
        val = hash_val(label)
        op = re.findall(pat_op, step)[0]
        if op == '-':
            # remove [label] from box it's in, move other lenses forward (?)
            in_box = [lb for lb in boxes[val] if lb[0] == label]
            if in_box:
                boxes[val].remove(in_box[0])
        elif op == '=':
            # put focal length into box with [label] in it
            # if there's not already a lens, add to the box immediately behind any lenses already in the box (?)
            focal_len = int(re.findall(pat_focal_len, step)[0])
            # if there's already a lens in the box with that label, replace the old lens with the new lens
            slot_num = [boxes[val].index(lb) for lb in boxes[val] if lb[0] == label]
            if slot_num:
                boxes[val][slot_num[0]][1] = focal_len
            else:
                boxes[val].append([label, focal_len])
    return focusing_power(boxes)


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
