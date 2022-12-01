from pathlib import Path

day_num = 1
input_file = Path.cwd() / '2022' / 'inputs' / f"day{day_num}.txt"

with open(input_file) as f:
    elves = f.read().split('\n\n')
    elf_cals = []
    for elf in elves:
        elf_cals.append(sum([int(item) for item in elf.split('\n')]))


def part_1():
    return max(elf_cals)


def part_2():
    elf_cals.sort(reverse=True)
    return sum(elf_cals[:3])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
