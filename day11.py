import os


def read_input(file: str):
    energy = {}
    with open(os.path.join('inputs', file)) as f:
        for x, row in enumerate(f.read().split('\n')):
            for y, e in enumerate(row):
                energy[(x, y)] = int(e)
    return energy


class Octopuses:
    def __init__(self, file):
        self.energy = read_input(file)
        self.flash_count = 0
        self.already_flashed = []
        self.total_octopuses = len(self.energy)

    def increase_energy(self):
        self.energy = {k: v + 1 for k, v in self.energy.items()}

    def neighbors(self, octo: tuple):
        x, y = octo
        return filter(lambda n: n in self.energy, [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)])

    def return_new_flashers(self):
        return [k for k, v in self.energy.items() if v > 9 and k not in self.already_flashed]

    def check_flashes(self):
        for f in self.return_new_flashers():
            self.flash_count += 1
            self.energy[f] = 0
            self.already_flashed.append(f)
            for n in self.neighbors(f):
                self.energy[n] += 1
            return self.check_flashes()

    def reset(self):
        for op in self.already_flashed:
            self.energy[op] = 0
            self.already_flashed = []


def part_1():
    octo = Octopuses('day11.txt')
    for step in range(100):
        # 1 increase energy by 1 for all octopuses
        octo.increase_energy()
        # 2 any octopus with energy greater than 9 flashes
        octo.check_flashes()
        # 3 any octopus that flashed has its energy reset to 0
        octo.reset()
    return octo.flash_count


def part_2():
    octo = Octopuses('day11.txt')
    step = 0
    while len(octo.already_flashed) < octo.total_octopuses:
        # 3 any octopus that flashed has its energy reset to 0
        octo.reset()
        # 1 increase energy by 1 for all octopuses
        octo.increase_energy()
        # 2 any octopus with energy greater than 9 flashes
        octo.check_flashes()
        step += 1
    return step


if __name__ == '__main__':
    print(part_1())
    print(part_2())
