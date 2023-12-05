import re
import numpy as np
import sys
sys.path.append('..')
from aoc_utils import get_input

"""
seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location

map syntax
(destination range start) (source range start) (range length)
"""


def parse_map(row_text):
    return_map = {}
    for row in row_text.split('\n')[1:]:
        dest_start, src_start, range_len = [int(x) for x in re.findall(r"(\d*)", row) if x]
        return_map[(src_start, src_start + range_len)] = dest_start
    return return_map


data = get_input().split('\n\n')
almanac = {}
for item in data:
    item_name = item.split(':')[0].replace(' ', '_').replace('-', '_')
    if item_name == 'seeds':
        seeds = [int(x) for x in re.findall(r"(\d*)", item) if x]
        almanac[item_name] = seeds
        # for pt 2
        seed_ranges = []
        for s in range(0, len(seeds), 2):
            seed_ranges.append((seeds[s], seeds[s] + seeds[s + 1]))
        almanac['seed_range'] = seed_ranges
    else:
        almanac[item_name] = parse_map(item)

steps = (
    'seeds',
    'seed_to_soil_map',
    'soil_to_fertilizer_map',
    'fertilizer_to_water_map',
    'water_to_light_map',
    'light_to_temperature_map',
    'temperature_to_humidity_map',
    'humidity_to_location_map'
)


def fetch_destination(value: int, step_id: int):
    almanac_key = steps[step_id]
    src_key = [x for x in almanac[almanac_key] if value in range(x[0], x[1] + 1)]
    if src_key:
        diff = value - src_key[0][0]
        new_value = almanac[almanac_key][src_key[0]] + diff
    else:
        new_value = value
    if almanac_key == 'humidity_to_location_map':
        return new_value
    else:
        return fetch_destination(value=new_value, step_id=step_id+1)


def part_1():
    locations = []
    for seed in almanac['seeds']:
        seed_loc = fetch_destination(seed, 1)
        locations.append(seed_loc)
    return min(locations)


def part_2():
    min_loc = np.inf
    for sr in almanac['seed_range']:
        for seed in range(sr[0], sr[1] + 1):
            seed_loc = fetch_destination(seed, 1)
            if seed_loc < min_loc:
                min_loc = seed_loc
    return min_loc


if __name__ == '__main__':
    print(part_1())
    print(part_2())
