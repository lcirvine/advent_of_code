import os
import matplotlib.pyplot as plt


def get_input():
    with open(os.path.join(os.getcwd(), 'day3_input.txt')) as f:
        day3_data = f.readlines()
    wire1 = [x for x in day3_data[0].split(',')]
    wire2 = [x for x in day3_data[1].split(',')]
    return wire1, wire2


dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def wire_path(wire):
    x = 0
    y = 0
    length = 0
    # part 1
    # ans = set()
    ans = {}
    for w in wire:
        direction = w[0]
        value = int(w[1:])
        assert direction in ['L', 'R', 'U', 'D']
        for _ in range(value):
            x += dx[direction]
            y += dy[direction]
            # part 1
            # ans.add((x, y))
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


def wire_charts(wire):
    x_data = [0]
    y_data = [0]
    x_value = 0
    y_value = 0
    for w in wire:
        direction = w[0]
        value = int(w[1:])
        if direction == 'U':
            y_value += value
            x_data.append(x_value)
            y_data.append(y_value)
        elif direction == 'D':
            y_value -= value
            x_data.append(x_value)
            y_data.append(y_value)
        elif direction == 'L':
            x_value -= value
            x_data.append(x_value)
            y_data.append(y_value)
        elif direction == 'R':
            x_value += value
            x_data.append(x_value)
            y_data.append(y_value)
        else:
            print('Something is wrong...')
            break
    return x_data, y_data


if __name__ == '__main__':
    w1, w2 = get_input()
    w1a = wire_path(w1)
    w2a = wire_path(w2)
    # part 1
    # both = w1a & w2a
    both = set(w1a.keys()) & set(w2a.keys())
    part_1_ans = min([abs(x) + abs(y) for (x, y) in both])
    part_2_ans = min([w1a[p] + w2a[p] for p in both])
    print(part_1_ans, part_2_ans)
    w1x, w1y = wire_charts(w1)
    w2x, w2y = wire_charts(w2)
    fig = plt.figure(figsize=(12, 8), dpi=80)
    ax = plt.axes()
    plt.plot(w1x, w1y, color='green', linestyle='solid')
    plt.plot(w2x, w2y, color='blue', linestyle='dashed')
    fig.savefig('day3_crossed_wires.png')
    plt.show()
