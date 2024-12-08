from datetime import date
import sys
sys.path.append('..')
from aoc_utils import get_input, submit_answer

day_num = 6

class GuardMap:
    def __init__(self, test=False):
        data = get_input(6, test=test)
        self.guard_map = {}
        for y, row in enumerate(data.split('\n')):
            for x, char in enumerate(row):
                self.guard_map[(x, y)] = char
                if char == '^':
                    self.guard_pos = (x, y)
        self.direction = (0, -1)  # up
        self.visited = set()
        self.obstructions = []

    def turn_right(self):
        directions = [
            (0, -1),   # up 
            (1, 0),    # right
            (0, 1),    # down
            (-1, 0)    # left
        ]
        ix_current = directions.index(self.direction)
        ix_next = (ix_current + 1) % 4
        return directions[ix_next]
    
    def next_position(self):
        x, y = self.guard_pos
        nx = x + self.direction[0]
        ny = y + self.direction[1]
        return nx, ny

    def travelled_right(self):
        x, y = self.guard_pos
        right_dirction = self.turn_right()
        rx = x + right_dirction[0]
        ry = y + right_dirction[1]
        while (rx, ry) in self.visited:
            nrx = rx + right_dirction[0]
            nry = ry + right_dirction[1]
            if self.guard_map.get((nrx, nry)) == '#':
                next_pos = self.next_position()
                self.obstructions.append(next_pos)
            rx = nrx
            ry = nry

    def travel_map(self):
        while self.guard_pos in self.guard_map:
            self.visited.add(self.guard_pos)
            next_pos = self.next_position()
            self.travelled_right()
            if self.guard_map.get(next_pos) == '#':
                self.direction = self.turn_right()
                next_pos = self.next_position()
            self.guard_pos = next_pos

    def return_visited(self):
        return self.visited
    
    def return_obstructions(self):
        return self.obstructions



if __name__ == '__main__':
    gm = GuardMap(test=True)
    gm.travel_map()
    visited = gm.return_visited()
    obstructions = gm.return_obstructions()
    a1 = len(visited)
    a2 = len(obstructions)
    submit_answer(answer_1=a1, answer_2=a2, day_num=day_num)
