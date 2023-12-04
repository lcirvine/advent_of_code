import re
import sys
sys.path.append('..')
from aoc_utils import get_input

data = get_input(day_num=4, test=True)
card_info = {}
for card in data.split('\n'):
    card_str, all_nums = card.split(':')
    id = [int(c) for c in re.findall(r"Card\s*(\d*)", card_str) if c][0]
    win_nums = set([int(n) for n in re.findall(r"(\d*)", all_nums.split('|')[0]) if n])
    my_nums = set([int(n) for n in re.findall(r"(\d*)", all_nums.split('|')[1]) if n])
    card_info[id] = {'win_nums': win_nums, 'my_nums': my_nums, 'num_cards': 1, 'num_winners': len(win_nums.intersection(my_nums))}


def check_winners(card_id):
    return card_info[card_id]['win_nums'].intersection(card_info[card_id]['my_nums'])


def part_1():
    points = 0
    for card_id in card_info:
        num_winners = card_info[card_id]['num_winners']
        if num_winners > 0:
            points += 2 ** (num_winners - 1)
    return points


def increment_winners(card_id):
    num_winners = card_info[card_id]['num_winners']
    for card_won in range(card_id + 1, num_winners + 2):
        card_info[card_won]['num_cards'] += 1
        increment_winners(card_won)


def part_2():
    for card_id in card_info:
        increment_winners(card_id)
    return sum([x['num_cards'] for x in card_info.values()])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
