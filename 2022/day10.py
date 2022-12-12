from aoc_inputs import get_input
from pathlib import Path

instruction_list = get_input(day_num=10).split('\n')


def part_1():
    check_cycles = [20, 60, 100, 140, 180, 220]
    cycle = 0
    x = 1
    signal_strengths = []
    for instr in instruction_list:
        if instr.startswith('addx '):
            num = int(instr.split('addx ')[1])
            for cy in range(2):
                cycle += 1
                if cycle in check_cycles:
                    signal_strengths.append(x * cycle)
                    # print(f"cycle {cycle} - {x * cycle}")
            x += num
        elif instr == 'noop':
            cycle += 1
            if cycle in check_cycles:
                signal_strengths.append(x * cycle)
                # print(f"cycle {cycle} - {x * cycle}")
    return sum(signal_strengths)


def part_2():
    cycle_add_to_x = {x: 0 for x in range(1, 242)}
    current_cycle = 0
    for instr in instruction_list:
        if instr.startswith('addx '):
            current_cycle += 2
            cycle_add_to_x[current_cycle] += int(instr.split('addx ')[1])
        elif instr == 'noop':
            current_cycle += 1
    crt = []
    row = []
    x = 1
    for cycle in range(1, 242):
        pos = (cycle - 1) % 40
        if pos == 0:
            crt.append(row)
            row = []
        if pos in range(x-1, x + 2):
            row.append('#')
        else:
            row.append('.')
        x += cycle_add_to_x[cycle]
    with open(Path.cwd() / 'inputs' / 'day10_visual.txt', 'w') as f:
        for r in crt:
            for pixel in r:
                f.write(pixel + ' ')
            f.write('\n')
    for r in crt:
        print(' '.join(r))


if __name__ == '__main__':
    print(part_1())
    part_2()
