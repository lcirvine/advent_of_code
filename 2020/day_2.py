import os
import re

with open(os.path.join('Inputs', 'day_2.txt')) as f:
    data = f.read().split('\n')


def part_1():
    matches = []
    for item in data:
        policy, pw = item.split(': ')
        num_range, letter = policy.split(' ')
        low_num, high_num = num_range.split('-')
        low_num = int(low_num)
        high_num = int(high_num)
        num_matches = len([lm for lm in pw if lm == letter])
        if num_matches in range(low_num, high_num + 1):
            matches.append(item)
    return len(matches)


def testing_part_2():
    with open(os.path.join('Tests', 'day 2 part 2.txt', 'w')) as f:
        matches = []
        for item in data[:10]:
            f.write(item + '\n')
            policy, pw = item.split(': ')
            num_range, letter = policy.split(' ')
            low_num, high_num = num_range.split('-')
            low_num = int(low_num) - 1
            high_num = int(high_num) - 1
            f.write(f"low number {low_num}, high number {high_num}, length of pw {len(pw)}\n")
            if (low_num < len(pw)) and (high_num < len(pw)):
                letter_low_num = pw[low_num]
                letter_high_num = pw[high_num]
                f.write(f"letter low number: {letter_low_num}, letter high number: {letter_high_num}\n")
                if letter_low_num == letter and letter_high_num != letter:
                    matches.append(item)
                    f.write('Match!\n')
                elif letter_low_num != letter and letter_high_num == letter:
                    matches.append(item)
                    f.write('Match!\n')
                else:
                    f.write('not a match!\n')
            f.write('\n')
        return len(matches)


def part_2():
    matches = []
    for item in data:
        policy, pw = item.split(': ')
        num_range, letter = policy.split(' ')
        low_num, high_num = num_range.split('-')
        low_num = int(low_num) - 1
        high_num = int(high_num) - 1
        if (low_num < len(pw)) and (high_num < len(pw)):
            letter_low_num = pw[low_num]
            letter_high_num = pw[high_num]
            if letter_low_num == letter and letter_high_num != letter:
                matches.append(item)
            elif letter_low_num != letter and letter_high_num == letter:
                matches.append(item)
    return len(matches)

# Adding another solution I found for reference


pat = re.compile(r'(\d+)-(\d+) (\w): (\w*)')


def parse_line(line):
    low, high, char, pw = re.match(pat, line).groups()
    return int(low), int(high), char, pw


def part_1_alt():
    count = 0
    for item in data:
        low, high, char, pw = parse_line(item)
        if pw.count(char) in range(low, high + 1):
            count += 1
    return count


def part_2_alt():
    count = 0
    for item in data:
        low, high, char, pw = parse_line(item)
        if (pw[low - 1] == char) != (pw[high - 1] == char):
            count += 1
    return count


if __name__ == '__main__':
    print(part_1())
    print(part_2())
    print(part_1_alt())
    print(part_2_alt())
