import os

with open(os.path.join('Inputs', 'day_10.txt')) as f:
    adapters = list(map(int, f.read().split('\n')))

# adding 0 for the charging outlet
adapters.append(0)
# adding +3 to last adapter for device
adapters.append(max(adapters) + 3)
adapters.sort()


def part_1():
    diffs = [adapters[x + 1] - adapters[x] for x in range(len(adapters)-1)]
    ones = [x for x in diffs if x == 1]
    threes = [x for x in diffs if x == 3]
    return len(ones) * len(threes)


def part_2():
    dp = [1]
    for i in range(1, len(adapters)):
        ans = 0
        for j in range(i):
            if adapters[j] + 3 >= adapters[i]:
                ans += dp[j]
        dp.append(ans)
    return dp[-1]


if __name__ == '__main__':
    print(part_1())
    print(part_2())
