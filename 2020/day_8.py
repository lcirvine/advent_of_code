import os
import re

with open(os.path.join('Inputs', 'day_8.txt')) as f:
    instr = f.read().split('\n')

instr_pat = re.compile(r'^(\w{3})\s([+|-]\d*)$')


def parse_instructions(instuction):
    return re.match(instr_pat, instuction).groups()


def part_1():
    accumulator = 0
    steps_taken = []
    i = 0
    carry_on = True
    while carry_on:
        if i in steps_taken:
            carry_on = False
        else:
            steps_taken.append(i)
        arg, num = parse_instructions(instr[i])
        if arg == 'acc' and carry_on:
            accumulator += int(num)
            i += 1
        elif arg == 'jmp' and carry_on:
            i += int(num)
        elif arg == 'nop' and carry_on:
            i += 1
    return accumulator


def part_2():
    nj_dict = {x: instr[x] for x in range(len(instr)) if instr[x].startswith('nop') or instr[x].startswith('jmp')}
    for k, v in nj_dict.items():
        accumulator = 0
        steps_taken = []
        i = 0
        carry_on = True
        while carry_on:
            if i == len(instr):
                print(f"Answer? - {instr[i]}")
                # return accumulator
            if i in steps_taken:
                print(f"Repeating with {v} - {k}")
                carry_on = False
            steps_taken.append(i)
            arg, num = parse_instructions(instr[i])
            if arg == 'acc':
                accumulator += int(num)
                i += 1
            elif (arg == 'jmp') or (arg == 'nop' and i == k):
                i += int(num)
            elif (arg == 'nop') or (arg == 'jmp' and i == k):
                i += 1


def part_2_test():
    with open(os.path.join('Inputs', 'day_8_test.txt')) as f:
        instr_test = f.read().split('\n')
    nj_dict = {x: instr_test[x] for x in range(len(instr_test)) if instr_test[x].startswith('nop') or instr_test[x].startswith('jmp')}
    for k, v in nj_dict.items():
        print(f"Trying {v} at {k}")
        accumulator = 0
        steps_taken = []
        i = 0
        carry_on = True
        while carry_on:
            print(f"{instr_test[i]} - {i}")
            if i == len(instr_test):
                print(f"Answer? - {instr_test[i]}")
                # return accumulator
            if i in steps_taken:
                print(f"Repeating with {v} - {k}")
                carry_on = False
            steps_taken.append(i)
            arg, num = parse_instructions(instr_test[i])
            if arg == 'acc':
                accumulator += int(num)
                i += 1
            elif (arg == 'jmp') or (arg == 'nop' and i == k):
                i += int(num)
            elif (arg == 'nop') or (arg == 'jmp' and i == k):
                i += 1
            print(i)


if __name__ == '__main__':
    # print(part_1())
    print(part_2_test())
