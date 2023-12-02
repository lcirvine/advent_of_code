import re
import sys
sys.path.append('..')
from aoc_utils import get_input

games = get_input(day_num=2).split('\n')


def part_1():
    possible_game_sum = 0
    limits = {'red': 12, 'green': 13, 'blue': 14}
    for game in games:
        max_red = max([int(num) for num in re.findall(r"(\d*)\sred", game)])
        max_green = max([int(num) for num in re.findall(r"(\d*)\sgreen", game)])
        max_blue = max([int(num) for num in re.findall(r"(\d*)\sblue", game)])
        if all([max_red <= limits['red'], max_green <= limits['green'], max_blue <= limits['blue']]):
            possible_game_sum += int(re.findall(r"Game\s(\d*):", game)[0])
    return possible_game_sum


def part_2():
    cube_power_sum = 0
    for game in games:
        max_red = max([int(num) for num in re.findall(r"(\d*)\sred", game)])
        max_green = max([int(num) for num in re.findall(r"(\d*)\sgreen", game)])
        max_blue = max([int(num) for num in re.findall(r"(\d*)\sblue", game)])
        cube_power_sum += (max_red * max_green * max_blue)
    return cube_power_sum


if __name__ == '__main__':
    print(part_1())
    print(part_2())
