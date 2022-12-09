from aoc_inputs import get_input

moves = get_input().split('\n')


class Rope:
    def __init__(self, rope_len: int):
        self.rope = [(0, 0) for knot in range(rope_len)]
        self.tail_positions = [self.rope[-1]]
        self.moves = get_input().split('\n')

    def move_head(self):
        for move in self.moves:
            hx, hy = self.rope[0]
            direction, num = move.split()
            for x in range(int(num)):
                if direction == 'U':
                    hy += 1
                if direction == 'D':
                    hy -= 1
                if direction == 'L':
                    hx -= 1
                if direction == 'R':
                    hx += 1
                self.rope[0] = (hx, hy)
                self.move_tail()
                self.track_tail()

    def move_tail(self):
        for knot_num in range(1, len(self.rope)):
            curr_x, curr_y = self.rope[knot_num]
            prev_x, prev_y = self.rope[knot_num - 1]
            delta_x = abs(prev_x - curr_x)
            delta_y = abs(prev_y - curr_y)
            # horizontal move
            if delta_x > 1 and delta_y == 0:
                if prev_x > curr_x:
                    curr_x += 1
                elif prev_x < curr_x:
                    curr_x -= 1
            # vertical move
            elif delta_x == 0 and delta_y > 1:
                if prev_y > curr_y:
                    curr_y += 1
                elif prev_y < curr_y:
                    curr_y -= 1
            # diagonal
            elif (delta_x == 1 and delta_y > 1) or (delta_x > 1 and delta_y == 1):
                if prev_x > curr_x:
                    curr_x += 1
                elif prev_x < curr_x:
                    curr_x -= 1
                if prev_y > curr_y:
                    curr_y += 1
                elif prev_y < curr_y:
                    curr_y -= 1
            elif delta_x > 1 and delta_y > 1:
                if prev_x > curr_x:
                    curr_x += delta_x - 1
                elif prev_x < curr_x:
                    curr_x -= delta_x - 1
                if prev_y > curr_y:
                    curr_y += delta_y - 1
                elif prev_y < curr_y:
                    curr_y -= delta_y - 1
            self.rope[knot_num] = (curr_x, curr_y)

    def track_tail(self):
        self.tail_positions.append(self.rope[-1])

    def return_tail_positions(self):
        return len(set(self.tail_positions))

    def main(self):
        self.move_head()
        return self.return_tail_positions()


if __name__ == '__main__':
    rope = Rope(rope_len=2)
    print(rope.main())
    rope2 = Rope(rope_len=10)
    print(rope2.main())
