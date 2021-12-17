
target_test = {
    'x_min': 20,
    'x_max': 30,
    'y_min': -5,
    'y_max': -10
}
# initial velocity of (6, 9) reaches a max y position of 45
# velocity decreases by 1 each time so 9 after 9 steps y velocity will be 0
# on the way down y position decreases exponentially (?) because the y velocity continues to decrease by 1
# y range is 5
target = {
    'x_min': 155,
    'x_max': 215,
    'y_min': -72,
    'y_max': -132
}


def step(pos: tuple, velocity: tuple):
    x, y = pos
    v_x, v_y = velocity
    # x position increases by x velocity
    x += v_x
    # y position increases by y velocity
    y += v_y
    # drag - x velocity moves toward 0 by 1
    if v_x > 0:
        v_x -= 1
    else:
        v_x += 1
    # gravity - y velocity decreases by 1
    v_y -= 1
    return (x, y), (v_x, v_y)


def validity_check(pos: tuple, velocity: tuple, **kwargs):
    x, y = pos
    v_x, v_y = velocity
    x_min = kwargs.get('x_min')
    x_max = kwargs.get('x_max')
    y_min = kwargs.get('y_min')
    y_max = kwargs.get('y_max')
    x_range = abs(x_max - x_min)
    y_range = abs(y_max - y_min)
    if x > x_max or y < y_max:
        return False
    else:
        return True

def max_height(y, v_y):
    y += v_y
    v_y -= 1
    if v_y > 0:
        return max_height(y, v_y)
    return y

def part_1(**kwargs):
    # what is the highest y position that will still reach the target?
    # should be able to just work out the y values that will still land in the target
    # highest position is where y velocity == 0
    # y velocity decreases by 1 every step due to gravity, as it speeds up it may overshoot the target
    x, y = (0, 0)
    x_min = kwargs.get('x_min')
    x_max = kwargs.get('x_max')
    y_min = kwargs.get('y_min')
    y_max = kwargs.get('y_max')
    x_range = range(x_min, x_max + 1)
    y_range = range(y_min, y_max - 1)
    valid = True
    while valid:




def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    print(part_2())
