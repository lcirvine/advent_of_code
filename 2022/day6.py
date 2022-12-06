from aoc_inputs import get_input

data = get_input()


def part_1_and_2(char_len: int):
    for x in range(char_len, len(data) + 1):
        char_set = set(data[x-char_len: x])
        if len(char_set) == char_len:
            return x


if __name__ == '__main__':
    print(part_1_and_2(char_len=4))
    print(part_1_and_2(char_len=14))
