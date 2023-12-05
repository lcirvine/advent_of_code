import re
import sys
sys.path.append('..')
from aoc_utils import get_input

data = get_input(day_num=4)
card_info = {}
for card in data.split('\n'):
    card_str, all_nums = card.split(':')
    id = [int(c) for c in re.findall(r"Card\s*(\d*)", card_str) if c][0]
    win_nums = set([int(n) for n in re.findall(r"(\d*)", all_nums.split('|')[0]) if n])
    my_nums = set([int(n) for n in re.findall(r"(\d*)", all_nums.split('|')[1]) if n])
    wins = win_nums.intersection(my_nums)
    wins_cards = [x for x in range(id + 1, id + len(wins) + 1)]
    card_info[id] = {'num_cards': 1, 'num_winners': len(wins), 'wins_cards': wins_cards}


def part_1():
    points = 0
    for card_id in card_info:
        num_winners = card_info[card_id]['num_winners']
        if num_winners > 0:
            points += 2 ** (num_winners - 1)
    return points


def increment_winners(card_id):
    for card_won in card_info[card_id]['wins_cards']:
        card_info[card_won]['num_cards'] += 1
        increment_winners(card_won)


def part_2():
    total_cards = 0
    for card_id, info in card_info.items():
        increment_winners(card_id)
        total_cards += info['num_cards']
    return total_cards


if __name__ == '__main__':
    print(part_1())
    print(part_2())
