from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 4
data = get_input(day_num)

word_search = {}
x_pos = []
a_pos = []
for y, row in enumerate(data.split('\n')):
    for x, char in enumerate(row):
        word_search[(x, y)] = char
        if char.upper() == 'X':
            x_pos.append((x, y))
        elif char.upper() == 'A':
            a_pos.append((x, y))


def get_neighbor_xmas_text(pos):
    neighbor_text = []
    x, y = pos
    neighbor_text.append(''.join([word_search.get((x + i, y), '') for i in range(4)]))   # right
    neighbor_text.append(''.join([word_search.get((x - i, y), '') for i in range(4)]))   # left
    neighbor_text.append(''.join([word_search.get((x, y - i), '') for i in range(4)]))   # up
    neighbor_text.append(''.join([word_search.get((x, y + i), '') for i in range(4)]))   # down
    neighbor_text.append(''.join([word_search.get((x + i, y - i), '') for i in range(4)]))   # diagonal up right
    neighbor_text.append(''.join([word_search.get((x - i, y - i), '') for i in range(4)]))   # diagonal up left
    neighbor_text.append(''.join([word_search.get((x + i, y + i), '') for i in range(4)]))   # diagonal down right
    neighbor_text.append(''.join([word_search.get((x - i, y + i), '') for i in range(4)]))   # diagonal down left
    return neighbor_text


def get_neighbor_mas_text(pos):
    neighbor_text = []
    x, y = pos
    up_right = word_search.get((x + 1, y - 1), '')
    down_right = word_search.get((x + 1, y + 1), '')
    up_left = word_search.get((x - 1, y - 1), '')
    down_left = word_search.get((x - 1, y + 1), '')
    neighbor_text.append(''.join([up_right, word_search.get(pos), down_left]))   # diagonal up right
    neighbor_text.append(''.join([up_left, word_search.get(pos), down_right]))   # diagonal up left
    neighbor_text.append(''.join([down_right, word_search.get(pos), up_left]))   # diagonal down right
    neighbor_text.append(''.join([down_left, word_search.get(pos), up_right]))   # diagonal down left
    return neighbor_text


def part_1():
    total = 0
    for pos in x_pos:
        for text in get_neighbor_xmas_text(pos):
            if text == 'XMAS':
                total += 1
    return total


def part_2():
    total = 0 
    for pos in a_pos:
        neighbor_text = get_neighbor_mas_text(pos)
        if neighbor_text.count('MAS') == 2:
            total += 1
    return total


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
