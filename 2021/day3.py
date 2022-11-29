import os
from collections import defaultdict
import numpy as np

with open(os.path.join('inputs', 'day3.txt')) as f:
    data = f.read().split('\n')

with open(os.path.join('inputs', 'day3_test.txt')) as f:
    test_data = f.read().split('\n')


def part_1_attempt_1(input_data: list):
    bit_pos = defaultdict(list)
    for x in input_data:
        for y in range(len(x)):
            bit_pos[y].append(x[y])
    gamma = []
    epsilon = []
    for k, v in bit_pos.items():
        one_count = v.count('1')
        zero_count = v.count('0')
        if one_count > zero_count:
            gamma.append('1')
            epsilon.append('0')
        elif zero_count > one_count:
            gamma.append('0')
            epsilon.append('1')
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part_1_attempt_2(input_data: list):
    gamma = []
    epsilon = []
    ll = []
    for x in input_data:
        ll.append([x[y] for y in range(len(x))])
    ll_trans = np.array(ll).T.tolist()
    for bit_pos in ll_trans:
        if bit_pos.count('1') > bit_pos.count('0'):
            gamma.append('1')
            epsilon.append('0')
        elif bit_pos.count('0') > bit_pos.count('1'):
            gamma.append('0')
            epsilon.append('1')
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part_2(input_data: list):

    def rating(oxy_co2: str, possible_matches=None, match_str: str = '', bit_pos: int = 0):
        if possible_matches is None:
            possible_matches = input_data
        col = [x[bit_pos] for x in possible_matches]
        diff = col.count('1') - col.count('0')
        if oxy_co2 == 'oxy':
            if diff >= 0:  # 1's >= 0's
                match_str += '1'
            else:
                match_str += '0'
        elif oxy_co2 == 'co2':
            if diff >= 0:
                match_str += '0'
            else:
                match_str += '1'
        possible_matches = [m for m in possible_matches if m.startswith(match_str)]
        if len(possible_matches) == 1:
            return int(possible_matches[0], 2)
        else:
            bit_pos += 1
            return rating(oxy_co2=oxy_co2, possible_matches=possible_matches, match_str=match_str, bit_pos=bit_pos)

    oxy_rating = rating(oxy_co2='oxy')
    co2_rating = rating(oxy_co2='co2')
    return oxy_rating * co2_rating


if __name__ == '__main__':
    print(part_1_attempt_1(data))
    print(part_1_attempt_2(data))
    print(part_2(data))
