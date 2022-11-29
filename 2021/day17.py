
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


def step_x(v_x, x=0, x_min=155, x_max=215):
    # x position increases by x velocity
    x += v_x
    # y position increases by y velocity
    if v_x > 0:
        v_x -= 1
    else:
        v_x += 1
    if x in range(x_min, x_max + 1):
        return v_x
    elif x > x_max:
        return 0
    else:
        return step_x(v_x=v_x, x=x)


def step_y(v_y, y=0, y_min=-72, y_max=-132, height=0):
    # y position increases by y velocity
    y += v_y
    # gravity - y velocity decreases by 1
    v_y -= 1
    if v_y == 0:
        height = y
    if y in range(y_min, y_max - 1, -1):
        return height
    elif y < y_max:
        return 0
    else:
        return step_y(v_y=v_y, y=y, height=height)


# what is the highest y position that will still reach the target?
# highest position is where y velocity == 0
print(max(map(step_y, [vy for vy in range(100, 250)])))
# max height is where y velocity = 131


def step(v_x, v_y, x=0, y=0, x_min=155, x_max=215, y_min=-72, y_max=-132):
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
    if x in range(x_min, x_max + 1) and y in range(y_min, y_max - 1, -1):
        return True
    elif x > x_max or y < y_max:
        return False
    else:
        return step(v_x=v_x, v_y=v_y, x=x, y=y)


valid_velocities = []
x, y = (0, 0)
x_max = 215
x_min = 155
y_min = -72
y_max = -132
# x_max = 20
# x_min = 30
# y_min = -5
# y_max = -10
x_range = range(x_min, x_max + 1)
y_range = range(y_min, y_max - 1)
# max valid x velocity is 214
valid_x = []
for i, v_x in enumerate(map(step_x, [vx for vx in range(1, 250)])):
    if v_x > 0:
        valid_x.append(i)
valid_y = []
for i, v_y in enumerate(map(step_y, [vy for vy in range(-100, 150)])):
    if v_x > 0:
        valid_x.append(i)
for v_x in range(1, 230):
    for v_y in range(-150, 150):
        if step(v_x, v_y, x=0, y=0, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max):
            valid_velocities.append((v_x, v_y))

print(len(set(valid_velocities)))
# print(set(valid_velocities))
