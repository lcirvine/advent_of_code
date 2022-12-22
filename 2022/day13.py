from aoc_inputs import get_input
import json

pairs = get_input(day_num=13, test=True).split('\n\n')


def compare(left, right):
    for i in range(min(len(left), len(right))):
        li = left[i]
        ri = right[i]
        if isinstance(li, int) and isinstance(ri, int):
            if li == ri:
                continue
            elif li < ri:
                return 1
            else:
                return 0
        elif isinstance(li, int) and isinstance(ri, list):
            return compare(left=[li], right=ri)
        elif isinstance(li, list) and isinstance(ri, int):
            return compare(left=li, right=[ri])
        elif isinstance(li, list) and isinstance(ri, list):
            return compare(left=li, right=ri)


def char_comparison():
    """This works for part 1 of the example but not for the real input"""
    ix_sum = 0
    pair_num = 0
    for pair in pairs:
        pair_num += 1
        left, right = pair.split('\n')
        for i in range(min(len(left), len(right))):
            li = left[i]
            ri = right[i]
            if li == ri:
                continue
            elif li.isnumeric() and ri.isnumeric():
                # there are some 10s in the input so have to handle 2-digit numbers
                if left[i + 1].isnumeric():
                    li = li + left[i + 1]
                if right[i + 1].isnumeric():
                    ri = ri + right[i + 1]
                if int(li) < int(ri):
                    ix_sum += pair_num
                break
            elif li == '[' and ri.isnumeric():
                right = right[:i] + '[' + right[i:]
            elif li.isnumeric() and ri == '[':
                left = left[:i] + '[' + left[i:]
            elif li == ']' and (ri.isnumeric() or ri == ','):
                ix_sum += pair_num
                break
            elif ri == ']' and (li.isnumeric() or li == ','):
                break
            elif i == (len(left) - 1) and len(left) < len(right):
                ix_sum += pair_num
    return ix_sum


def part_1():
    total = 0
    for i, pair in enumerate(pairs, start=1):
        left, right = pair.split('\n')
        left = json.loads(left)
        right = json.loads(right)
        val = compare(left, right)
        if val:
            total += val * i


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
