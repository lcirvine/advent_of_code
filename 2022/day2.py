from aoc_inputs import get_input

data = get_input()
rps = data.split('\n')


def part_1():
    # A / X = rock = 1
    # B / Y = paper = 2
    # C / Z = scissors = 3
    # ----------------
    # lose = 0
    # draw = 3
    # win = 6
    shape_pts_map = {'X': 1, 'Y': 2, 'Z': 3}
    round_pts_map = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3}
    }
    total_points = 0
    for game in rps:
        opp, you = game.split()
        round_pts = round_pts_map[opp][you]
        shape_pts = shape_pts_map[you]
        total_points += sum((round_pts, shape_pts))
    return total_points


def part_2():
    # A = rock = 1
    # B = paper = 2
    # C = scissors = 3
    # ----------------
    # X = lose = 0
    # Y = draw = 3
    # Z = win = 6
    round_pts_map = {'X': 0, 'Y': 3, 'Z': 6}
    shape_pts_map = {
        'X': {'A': 3, 'B': 1, 'C': 2},  # lose
        'Y': {'A': 1, 'B': 2, 'C': 3},  # draw
        'Z': {'A': 2, 'B': 3, 'C': 1},  # win
    }
    total_points = 0
    for game in rps:
        opp, outcome = game.split()
        round_pts = round_pts_map[outcome]
        shape_pts = shape_pts_map[outcome][opp]
        total_points += sum((round_pts, shape_pts))
    return total_points


if __name__ == '__main__':
    print(part_1())
    print(part_2())
