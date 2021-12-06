import os


def read_input(file: str = 'day6.txt') -> list:
    with open(os.path.join('inputs', file)) as f:
        data = [int(x) for x in f.read().split(',')]
    return data


def part_1(days: int):
    fish = read_input()
    for t in range(days):
        new_fish = 0
        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
                new_fish += 1
            else:
                fish[i] -= 1
        for nf in range(new_fish):
            fish.append(8)
    return len(fish)


def part_2(days: int):
    fish = read_input()
    fish_count = {x: 0 for x in range(9)}
    for f in fish:
        fish_count[f] += 1
    age_change = {
        0: 6,
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7
    }
    for t in range(days):
        new_fish = fish_count[0]
        fish_count = {age_change[k]: v for k, v in fish_count.items()}
        fish_count[6] += new_fish
        fish_count[8] = new_fish
    return sum(fish_count.values())


if __name__ == '__main__':
    print(part_1(days=80))
    print(part_2(days=256))
