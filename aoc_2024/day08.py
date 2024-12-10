from collections import defaultdict
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 8
data = get_input(day_num)

antenna_locations = defaultdict(list)
antenna_map = {}
for y, row in enumerate(data.split('\n')):
    for x, char in enumerate(row):
        antenna_map[(x, y)] = char
        if char != '.':
            antenna_locations[char].append((x, y))


def part_1():
    node_locations = set()
    for a in antenna_locations:
        for loc in antenna_locations[a]:
            x1, y1 = loc
            for loc2 in antenna_locations[a]:
                if loc == loc2:
                    continue
                x2, y2 = loc2
                x_diff = x1 - x2
                y_diff = y1 - y2
                x_node = x2 - x_diff
                y_node = y2 - y_diff
                if (x_node, y_node) in antenna_map:
                    node_locations.add((x_node, y_node))
    return len(node_locations)


def part_2():
    node_locations = set()
    for a in antenna_locations:
        for loc in antenna_locations[a]:
            x1, y1 = loc
            for loc2 in antenna_locations[a]:
                if loc == loc2:
                    node_locations.add(loc)
                    continue
                x2, y2 = loc2
                x_diff = x1 - x2
                y_diff = y1 - y2
                x_node = x2 - x_diff
                y_node = y2 - y_diff
                while (x_node, y_node) in antenna_map:
                    node_locations.add((x_node, y_node))
                    x_node -= x_diff
                    y_node -= y_diff
    return len(node_locations)


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
