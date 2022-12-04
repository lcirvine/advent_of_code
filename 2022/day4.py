from aoc_inputs import get_input

elf_pairs = get_input().split('\n')


def part_1():
    num_overlap = 0
    for ep in elf_pairs:
        e1, e2 = ep.split(',')
        e1r = [int(sect) for sect in e1.split('-')]
        e2r = [int(sect) for sect in e2.split('-')]
        e1set = set([i for i in range(e1r[0], e1r[1] + 1)])
        e2set = set([i for i in range(e2r[0], e2r[1] + 1)])
        u = set.intersection(e1set, e2set)
        # how many fully overlap?
        if len(u) == len(e1set) or len(u) == len(e2set):
            num_overlap += 1
    return num_overlap


def part_2():
    num_overlap = 0
    for ep in elf_pairs:
        e1, e2 = ep.split(',')
        e1r = [int(sect) for sect in e1.split('-')]
        e2r = [int(sect) for sect in e2.split('-')]
        e1set = set([i for i in range(e1r[0], e1r[1] + 1)])
        e2set = set([i for i in range(e2r[0], e2r[1] + 1)])
        u = set.intersection(e1set, e2set)
        # how many overlap at all?
        if len(u) > 0:
            num_overlap += 1
    return num_overlap


if __name__ == '__main__':
    print(part_1())
    print(part_2())
