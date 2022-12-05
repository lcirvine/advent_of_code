from aoc_inputs import get_input
import re

stacks_text, moves = get_input().split('\n\n')
moves = moves.split('\n')
move_pat = r"move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)$"


def parse_stacks():
    stacks_v = stacks_text.split('\n')
    # reversing so that the rows go from bottom to top rather than top to bottom
    stacks_v.reverse()
    # columns are aligned vertically so all the characters for each stack must be in the same position
    # finding the positions with alphanumeric characters in the first row i.e. not in (' ', '[', ']')
    char_pos = [stacks_v[0].index(char) for char in stacks_v[0] if char.isalnum()]
    stacks = {}
    for pos in char_pos:
        stack_text = ''
        for row in stacks_v:
            stack_text += row[pos]
        stack_num = [int(char) for char in stack_text if char.isnumeric()][0]
        stacks[stack_num] = [char for char in stack_text if char.isalpha()]
    return stacks


def part_1():
    stacks = parse_stacks()
    for move in moves:
        num, from_stack, to_stack = re.match(move_pat, move).groups()
        num = int(num)
        from_stack = int(from_stack)
        to_stack = int(to_stack)
        # moving one crate at a time
        for i in range(num):
            stacks[to_stack].append(stacks[from_stack].pop())
    top_of_stacks = ''
    for stack in stacks:
        top_of_stacks += stacks[stack][-1]
    return top_of_stacks


def part_2():
    stacks = parse_stacks()
    for move in moves:
        num, from_stack, to_stack = re.match(move_pat, move).groups()
        num = int(num)
        from_stack = int(from_stack)
        to_stack = int(to_stack)
        # moving multiple crates at once
        to_be_moved = stacks[from_stack][num * -1:]
        stacks[to_stack].extend(to_be_moved)
        stacks[from_stack] = stacks[from_stack][:num * -1]
    top_of_stacks = ''
    for stack in stacks:
        top_of_stacks += stacks[stack][-1]
    return top_of_stacks


if __name__ == '__main__':
    print(part_1())
    print(part_2())
