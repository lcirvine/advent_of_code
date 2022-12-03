from aoc_inputs import get_input
import string

sacks = get_input().split('\n')
chars = list(string.ascii_lowercase + string.ascii_uppercase)
char_val = {char: val for val, char in enumerate(chars, start=1)}


def part_1():
    total_val = 0
    for sack in sacks:
        midpoint = int(len(sack) / 2)
        dupe_char = [char for char in sack[:midpoint] if char in sack[midpoint:]][0]
        total_val += char_val[dupe_char]
    return total_val


def part_2():
    total_val = 0
    for i in range(0, len(sacks), 3):
        group = sacks[i: i + 3]
        dupe_char = [char for char in group[0] if char in group[1] and char in group[2]][0]
        total_val += char_val[dupe_char]
    return total_val


if __name__ == '__main__':
    print(part_1())
    print(part_2())
