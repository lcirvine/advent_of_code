import os

with open(os.path.join('Inputs', 'day_9.txt')) as f:
    data = f.read().split('\n')
    data = [int(x) for x in data]


def part_1(preamble_len: int = 25):
    for i_num in data:
        preamble = [x for x in data[i_num: i_num + preamble_len]]
        next_num = data[i_num + preamble_len]
        add_nums = [n for n in preamble if (next_num - n) in preamble]
        if len(add_nums) == 0:
            return next_num


def add_range(running_total: int, i_num: int, target_num: int, num_range: list):
    if i_num <= len(data):
        num_range.append(data[i_num])
    else:
        return False
    running_total += data[i_num]
    if running_total == target_num and len(num_range) > 1:
        return num_range
    elif running_total < target_num:
        i_num += 1
        return add_range(running_total, i_num, target_num, num_range)
    elif running_total > target_num:
        return False


def part_2():
    invalid_num = part_1()
    for i in range(len(data)):
        result = add_range(running_total=0, i_num=i, target_num=invalid_num, num_range=[])
        if result:
            return min(result) + max(result)


def add_range_test(test_data: list, running_total: int, i_num: int, target_num: int, num_range: list):
    if i_num <= len(test_data):
        num_range.append(test_data[i_num])
        print(f"Num range = {num_range}")
    running_total += test_data[i_num]
    print(f"Running total = {running_total}")
    if running_total == target_num and len(num_range) > 1:
        print(f"\nTotal in this range equals target number!\n{num_range}")
        return num_range
    elif running_total < target_num:
        print('Adding another number to range')
        i_num += 1
        return add_range_test(test_data, running_total, i_num, target_num, num_range)
    elif running_total > target_num:
        print('Running total is larger than target number')


def part_2_test():
    invalid_num = 127
    test_data = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    for i in range(len(test_data)):
        print(f"\nStarting with {test_data[i]}")
        result = add_range_test(test_data=test_data, running_total=0, i_num=i, target_num=invalid_num, num_range=[])
        if result:
            return min(result) + max(result)


if __name__ == '__main__':
    print(part_1())
    # print(part_2_test())
    print(part_2())
