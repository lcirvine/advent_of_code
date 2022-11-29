import os
import pyperclip

with open(os.path.join('inputs', 'day1.txt')) as f:
    depths = [int(d) for d in f.read().split('\n')]

test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part_1(depth_list: list):
    num_increasing = 0
    for i in range(1, len(depth_list)):
        depth_diff = depth_list[i] - depth_list[i-1]
        if depth_diff > 0:
            num_increasing += 1
    return num_increasing


def part_2(depth_list: list):
    sliding_depths = []
    for i in range(0, len(depth_list) - 2):
        sliding_depths.append(sum([depth_list[d] for d in range(i, i + 3)]))
    return part_1(sliding_depths)


if __name__ == '__main__':
    print(part_1(depths))
    print(part_2(depths))
