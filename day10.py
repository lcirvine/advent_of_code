import os
from math import ceil

open_chars = '([{<'
close_chars = ')]}>'
char_dict = dict(zip(open_chars, close_chars))


def read_input(file: str):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    return data


def part_1():
    lines = read_input('day10.txt')
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def incorrect_char(ln: str):
        line_open = []
        for char in ln:
            if char in open_chars:
                line_open.append(char)
            elif char in close_chars:
                if char == char_dict[line_open[-1]]:
                    line_open.pop()
                else:
                    return points[char]
        # score 0 points if there are no incorrect characters (incomplete line)
        return 0

    return sum(map(incorrect_char, lines))


def part_2():
    lines = read_input('day10.txt')
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def incomplete_line(ln: str):
        line_open = []
        for char in ln:
            if char in open_chars:
                line_open.append(char)
            elif char in close_chars:
                if char == char_dict[line_open[-1]]:
                    line_open.pop()
                else:
                    return False
        return line_open

    def score(remaining_open: list):
        score = 0
        missing = [char_dict[x] for x in remaining_open[::-1]]
        for char in missing:
            score = (score * 5) + points[char]
        return score

    remaining_chars = list(map(incomplete_line, filter(incomplete_line, lines)))
    scores = list(map(score, remaining_chars))
    scores.sort()
    # subtract 1 since list will start at index 0
    mid_score_index = ceil(len(scores) / 2) - 1
    return scores[mid_score_index]


if __name__ == '__main__':
    print(part_1())
    print(part_2())
