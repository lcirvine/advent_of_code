from aoc_inputs import get_input
import string


class HeightMap:
    def __init__(self, test=False):
        self.data = get_input(day_num=12, test=test).split('\n')
        self.lettermap = self.get_lettermap()
        self.start_point = [loc for loc, letter in self.lettermap.items() if letter == 'S'][0]
        self.end_point = [loc for loc, letter in self.lettermap.items() if letter == 'E'][0]
        self.heightmap = self.get_heightmap()
        self.stepmap = self.get_stepmap()
        self.seen = set()

    def get_lettermap(self):
        lettermap = {}
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y])):
                lettermap[(x, y)] = self.data[y][x]
        return lettermap

    def get_heightmap(self):
        char_height = dict(zip(string.ascii_lowercase, range(0, 26)))
        char_height['S'] = 0
        char_height['E'] = 25
        heightmap = {}
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y])):
                heightmap[(x, y)] = char_height[self.data[y][x]]
        return heightmap

    def get_stepmap(self):
        stepmap = {}
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y])):
                stepmap[(x, y)] = '.'
        return stepmap

    def neighbors(self, loc):
        x, y = loc
        return list(filter(lambda n: n in self.lettermap, [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]))

    def neighbors_to_visit(self, loc):
        current_height = self.heightmap[loc]
        x, y = loc
        n_visit = []
        neighbors = self.neighbors(loc)
        for neighbor in neighbors:
            n_height = self.heightmap[neighbor]
            if (n_height <= (current_height + 1)) and (neighbor not in self.seen):
                n_visit.append(neighbor)
        return n_visit

    def make_step(self, loc: tuple, step_num: int):
        for n in self.neighbors_to_visit(loc):
            self.lettermap[n] = step_num
            self.stepmap[n] = step_num
            self.seen.add(n)

    def solve(self, starting_point: tuple = None):
        if starting_point is None:
            starting_point = self.start_point
        step_num = 0
        self.lettermap[starting_point] = step_num
        self.seen.add(starting_point)
        while self.lettermap[self.end_point] == 'E':
            step_num += 1
            prev_steps = [loc for loc, step in self.lettermap.items() if step == (step_num - 1)]
            # with part 2 there can be starting points with no solution to get to the end
            if len(prev_steps) == 0:
                break
            else:
                for loc in prev_steps:
                    self.make_step(loc, step_num)

    def return_steps(self):
        return self.lettermap[self.end_point]

    def find_path(self, current_loc=None, maze_path=None):
        if current_loc is None:
            current_loc = self.end_point
        if maze_path is None:
            maze_path = [current_loc]
        if current_loc == self.start_point:
            return maze_path.reverse()
        for n in self.neighbors(current_loc):
            if self.lettermap[n] == (self.lettermap[current_loc] - 1):
                maze_path.append(n)
                return self.find_path(current_loc=n, maze_path=maze_path)

    def view_path(self):
        with open('day12_path.csv', 'w') as f:
            for y in set([y[1] for y in self.lettermap]):
                for x in set([x[0] for x in self.lettermap]):
                    f.write(str(self.lettermap[(x, y)]) + ',')
                f.write('\n')


def part_1():
    hm = HeightMap()
    hm.solve()
    return hm.return_steps()


def part_2():
    hm_initial = HeightMap()
    starting_points = [loc for loc, height in hm_initial.heightmap.items() if height == 0]
    steps_per_loc = {}
    for sp in starting_points:
        hm = HeightMap()
        hm.solve(starting_point=sp)
        steps = hm.return_steps()
        # if there is no solution, steps will just be 'E'
        if steps.isnumeric():
            steps_per_loc[sp] = steps
    min_steps = min(steps_per_loc.values())
    return {loc: steps for loc, steps in steps_per_loc.items() if steps == min_steps}


if __name__ == '__main__':
    print(part_1())
    print(part_2())
