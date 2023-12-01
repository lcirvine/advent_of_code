from aoc_inputs import get_input
import json

pairs = {}
for i, pair in enumerate(get_input(day_num=13, test=True).split('\n\n'), start=1):
    l, r = pair.split('\n')
    pairs[i] = {'left': json.loads(l), 'right': json.loads(r)}


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1
    elif isinstance(left, int) and isinstance(right, list):
        return compare(left=[left], right=right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left=left, right=[right])
    elif isinstance(left, list) and isinstance(right, list):
        return compare(left=left[0], right=right[0])


def char_comparison():
    """This works for part 1 of the example but not for the real input"""
    ix_sum = 0
    pair_num = 0
    for pair in get_input(day_num=13, test=True).split('\n\n'):
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
    for i, pair in pairs.items():
        left = pair['left']
        right = pair['right']
        for j in range(min(len(left), len(right))):
            val = compare(left[j], right[j])
            if val == 1 or (j == len(left) and len(left) < len(right)):
                total += (val * i)
                break
            elif val == -1:
                break


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
