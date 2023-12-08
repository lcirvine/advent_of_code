from typing import Union
import math
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 8
data = get_input(day_num)
instructions, all_nodes = data.split('\n\n')
node_map = {}
for node in all_nodes.split('\n'):
    loc, opts = node.split(' = ')
    opts = tuple([x.strip() for x in opts.strip('()').split(',')])
    node_map[loc] = opts


def next_node(current_node: str, step: int):
    instr_num = step % len(instructions)
    instr = instructions[instr_num]
    instr_map = {'L': 0, 'R': 1}
    next_node_num = instr_map[instr]
    return node_map[current_node][next_node_num]


def part_1(node: str = 'AAA', destination: Union[str, list] = 'ZZZ'):
    if isinstance(destination, str):
        destination = [destination]
    steps = 0
    while node not in destination:
        node = next_node(node, steps)
        steps += 1
    return steps


def part_2():
    a_nodes = [n for n in node_map if n.endswith('A')]
    z_nodes = [n for n in node_map if n.endswith('Z')]
    a_node_steps = {}
    for node in a_nodes:
        a_node_steps[node] = part_1(node, z_nodes)
    return math.lcm(*a_node_steps.values())


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
