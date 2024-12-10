from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 10
data = get_input(day_num, test=True)

trail_map = {}
trail_heads = []
for y, row in enumerate(data.split('\n')):
    for x, height in enumerate(row):
        trail_map[(x, y)] = int(height)
        if int(height) == 0:
            trail_heads.append((x, y))


def get_neighbors(loc: tuple, current_height: int):
    x, y = loc
    neighbors = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]
    neighbors = [n for n in neighbors if n in trail_map and trail_map[n] == current_height + 1]
    return neighbors


def climb(loc: tuple, score: int = 0):
    current_height = trail_map[loc]
    if current_height == 9:
        score += 1
    neighbors = get_neighbors(loc, current_height)
    for n in neighbors:
        return climb(n, score)
    return score


def part_1():
    total_score = 0
    for th in trail_heads:
        total_score += climb(th)
    return total_score


def part_2():
    return None


if __name__ == '__main__':
    a1 = part_1()
    a2 = part_2()
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
