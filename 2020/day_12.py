import os
import re

with open(os.path.join('Inputs', 'day_12.txt')) as f:
    data = f.read().split('\n')

test_data = ['F10', 'N3', 'F7', 'R90', 'F11']

instr_pat = re.compile(r'^([A-Z]*)(\d*)$')


def part_1():
    pos = (0, 0)
    facing = 'E'
    directions = 'NESWNESW'
    for instruction in data:
        instr, num = re.match(instr_pat, instruction).groups()
        num = int(num)
        x = pos[0]
        y = pos[1]
        if (instr == 'N') or (instr == 'F' and facing == 'N'):
            y += num
        elif (instr == 'S') or (instr == 'F' and facing == 'S'):
            y -= num
        elif (instr == 'E') or (instr == 'F' and facing == 'E'):
            x += num
        elif (instr == 'W') or (instr == 'F' and facing == 'W'):
            x -= num
        elif instr == 'L':
            facing = directions[::-1][directions[::-1].find(facing) + (num // 90)]
        elif instr == 'R':
            facing = directions[directions.find(facing) + (num // 90)]
        pos = (x, y)
    return abs(pos[0]) + abs(pos[1])


def part_2():
    wp = (10, 1)
    pos = (0, 0)
    for instruction in data:
        instr, num = re.match(instr_pat, instruction).groups()
        num = int(num)
        wpx = wp[0]
        wpy = wp[1]
        sx = pos[0]
        sy = pos[1]
        if instr == 'N':
            wpy += num
        elif instr == 'S':
            wpy -= num
        elif instr == 'E':
            wpx += num
        elif instr == 'W':
            wpx -= num
        elif instr in ['L', 'R']:
            turns = num // 90
            if (instr == 'L' and turns == 1) or (instr == 'R' and turns == 3):
                nwpx = wpy * -1
                nwpy = wpx
            elif turns == 2:
                nwpx = wpx * -1
                nwpy = wpy * -1
            elif (instr == 'L' and turns == 3) or (instr == 'R' and turns == 1):
                nwpx = wpy
                nwpy = wpx * -1
            wpx = nwpx
            wpy = nwpy
        elif instr == 'F':
            sx = sx + (wpx * num)
            sy = sy + (wpy * num)
        wp = (wpx, wpy)
        pos = (sx, sy)
    return abs(pos[0]) + abs(pos[1])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
