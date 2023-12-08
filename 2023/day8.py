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


def part_1():
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        node = next_node(node, steps)
        steps += 1
    return steps


def part_2():
    nodes = [n for n in node_map if n.endswith('A')]
    steps = 0
    all_z = False
    while not all_z:
        nodes = list(map(next_node, nodes, [steps for n in nodes]))
        steps += 1
        all_z = all([n.endswith('Z') for n in nodes])
    return steps


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num, submit=True)
