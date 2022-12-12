from aoc_inputs import get_input
import re
import math


def return_monkey_map():
    monkeys = get_input(day_num=11).split('\n\n')
    monkey_map = {}
    for monkey in monkeys:
        # monkey_attrs = [i.strip() for i in monkey.split('\n')]
        num = int(re.search(r"Monkey\s(\d*):", monkey).group(1))
        start_items = [int(i) for i in re.search(r"Starting items:\s([\d\,\s]*)\n", monkey).group(1).split(',')]
        op, op_num = re.search(r"Operation:\snew\s=\sold\s([\w\s\+\*]*)\n", monkey).group(1).split()
        test = int(re.search(r"Test:\sdivisible\sby\s(\d*)\n", monkey).group(1))
        cond_true = int(re.search(r"If\strue:\sthrow\sto\smonkey\s(\d*)\n", monkey).group(1))
        cond_false = int(re.search(r"If\sfalse:\sthrow\sto\smonkey\s(\d*)", monkey).group(1))
        monkey_map[num] = {
            'inspected_items': 0,
            'items': start_items,
            'op': op,
            'op_num': op_num,
            'test': test,
            'cond_true': cond_true,
            'cond_false': cond_false
        }
    return monkey_map


def part_1():
    monkey_map = return_monkey_map()
    for rnd in range(0, 20):
        for monkey_num, attributes in monkey_map.items():
            for item in attributes['items']:
                # inspect
                if attributes['op'] == '+':
                    if attributes['op_num'] == 'old':
                        item += item
                    else:
                        item += int(attributes['op_num'])
                elif attributes['op'] == '*':
                    if attributes['op_num'] == 'old':
                        item *= item
                    else:
                        item *= int(attributes['op_num'])
                attributes['inspected_items'] += 1
                # reduce worry
                item = math.floor(item / 3)
                # test
                if item % attributes['test'] == 0:
                    new_monkey = attributes['cond_true']
                else:
                    new_monkey = attributes['cond_false']
                # give item to new monkey
                monkey_map[new_monkey]['items'].append(item)
            # monkey should have thrown all items they held originally
            attributes['items'] = []
    inspected_items = [mattr['inspected_items'] for mattr in monkey_map.values()]
    inspected_items.sort()
    m1, m2 = inspected_items[-2:]
    return m1 * m2


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
