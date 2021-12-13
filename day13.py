import os
import re
# import pandas as pd


def read_input(file: str):
    dots = []
    pat_dot = r"(\d*),(\d*)"
    folding_instructions = []
    pat_fold = r"fold along\s([xy])=(\d*)"
    with open(os.path.join('inputs', file)) as f:
        txt_data = f.read()
    for dot in re.findall(pat_dot, txt_data):
        x = int(dot[0])
        y = int(dot[1])
        dots.append((x, y))
    dots.sort()
    for instruction in re.findall(pat_fold, txt_data):
        ax = instruction[0]
        num = int(instruction[1])
        folding_instructions.append((ax, num))
    return dots, folding_instructions


def part_1(num_instructions: int = None):
    dots, folding_instructions = read_input('day13.txt')
    folding_instructions = folding_instructions[:num_instructions]
    for fi in folding_instructions:
        ax = fi[0]
        fold_line = fi[1]
        # within each instruction I'm going to loop over each dot
        # creating a new variable to store the new values
        new_dots = []
        for dot in dots:
            x = dot[0]
            y = dot[1]
            if ax == 'y' and y > fold_line:
                new_y = fold_line - (y - fold_line)
                new_x = x
            elif ax == 'x' and x > fold_line:
                new_x = fold_line - (x - fold_line)
                new_y = y
            else:
                # no change, for points in the part that does not get folded over
                new_x = x
                new_y = y
            new_dots.append((new_x, new_y))
        # setting the list of dots to the new values
        dots = new_dots
    new_dots = list(set(dots))
    new_dots.sort()
    return new_dots


def part_2():
    dots = part_1()
    max_x = max([d[0] for d in dots])
    max_y = max([d[1] for d in dots])
    dot_plot = [[' ' for x in range(max_x + 1)] for y in range(max_y + 1)]
    # df_dots = pd.DataFrame(dot_plot)
    for dot in dots:
        x = dot[0]
        y = dot[1]
        dot_plot[y][x] = '$'
        # df_dots.loc[x, y] = '$'
    for row in dot_plot:
        print(' '.join(row))


if __name__ == '__main__':
    print(len(part_1(num_instructions=1)))
    part_2()
