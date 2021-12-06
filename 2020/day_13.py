import os

with open(os.path.join('Inputs', 'day_13.txt')) as f:
    data = f.read().split('\n')

depart = int(data[0])
busses = [int(x) for x in data[1].split(',') if x != 'x']
bus_sched = []
for b in data[1].split(','):
    if b != 'x':
        bus_sched.append(int(b))
    else:
        bus_sched.append(b)


def part_1():
    bus_time = {}
    min_bus_time = depart + max(busses) + 1
    for b in busses:
        bus_time[b] = [x for x in range(0, min_bus_time, b) if x >= depart]
    for t in bus_time.values():
        if min(t) < min_bus_time:
            min_bus_time = min(t)
    for k, v in bus_time.items():
        if min(v) == min_bus_time:
            return k * (min(v) - depart)


def crt(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total


def part_2():
    pairs = []
    for i, n in enumerate(data[1].split(',')):
        if n == 'x':
            continue
        n = int(n)
        pairs.append((n - i, n))
    return crt(pairs)


if __name__ == '__main__':
    print(part_1())
    print(part_2())

