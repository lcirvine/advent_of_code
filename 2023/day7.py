from string import ascii_uppercase
import re
from collections import Counter
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 7
data = get_input(day_num)


def part_1():
    card_vals = dict(zip('AKQJT98765432', ascii_uppercase))
    winnings = 0
    poker_round = []
    all_players_hands = data.split('\n')
    for hand in all_players_hands:
        cards, bid = hand.split(' ')
        bid = int(bid.strip())
        card_count = Counter(cards)
        unique_card_count = len(card_count)
        max_value_of_card = max(card_count.values())
        card_sort = ''.join([card_vals[c] for c in cards])
        poker_round.append((cards, bid, unique_card_count, max_value_of_card, card_sort))
    # sorting by least important attribute to most important attribute
    poker_round = sorted(poker_round, key=lambda x: x[4])                   # sort by card_sort, ascending
    poker_round = sorted(poker_round, key=lambda x: x[3], reverse=True)     # sort by max value of card, descending
    poker_round = sorted(poker_round, key=lambda x: x[2])                   # sort by number of unique cards, ascending
    # now that the poker round is sorted properly, I can multiply rank by bid and add that to the winnings
    rnk = len(all_players_hands)
    for hand in poker_round:
        winnings += (rnk * hand[1])
        rnk -= 1
    return winnings


def part_2():
    # J is now joker, not jack
    # jokers are the least valuable card
    card_vals = dict(zip('AKQT98765432J', ascii_uppercase))
    winnings = 0
    poker_round = []
    all_players_hands = data.split('\n')
    for hand in all_players_hands:
        cards, bid = hand.split(' ')
        bid = int(bid.strip())
        card_count = Counter(cards)
        unique_card_count = len(card_count)
        # remove jokers from max value count, those will be used as other cards and added to max value count later
        # in case cards = 'JJJJJ', + [0] adds zero to the list to ensure it is not an empty sequence
        max_value_of_card = max([val for card, val in card_count.items() if card != 'J'] + [0])
        card_sort = ''.join([card_vals[c] for c in cards])
        # jokers are wild
        if 'J' in cards:
            unique_card_count -= 1
        # have to have at least one unique card
        unique_card_count = max(unique_card_count, 1)
        for J in re.findall('J', cards):
            max_value_of_card += 1
        poker_round.append((cards, bid, unique_card_count, max_value_of_card, card_sort))
    # sorting by least important attribute to most important attribute
    poker_round = sorted(poker_round, key=lambda x: x[4])                   # sort by card_sort, ascending
    poker_round = sorted(poker_round, key=lambda x: x[3], reverse=True)     # sort by max value of card, descending
    poker_round = sorted(poker_round, key=lambda x: x[2])                   # sort by number of unique cards, ascending
    # now that the poker round is sorted properly, I can multiply rank by bid and add that to the winnings
    rnk = len(all_players_hands)
    for hand in poker_round:
        winnings += (rnk * hand[1])
        rnk -= 1
    return winnings


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, submit=True)
