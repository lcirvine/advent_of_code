from aoc_inputs import get_input

instructions = get_input().split('\n')


def part_1():
    check_cycles = [20, 60, 100, 140, 180, 220]
    cycle = 0
    x = 1
    signal_strengths = []
    for instr in instructions:
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
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
