"""
PART ONE
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

puzzle_input = 206938-679128

PART TWO
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""


def increasing_digits(num):
    num_list = [int(x) for x in str(num)]
    count_incr = 0
    for d in range(len(num_list) - 1):
        if num_list[d] <= num_list[d + 1]:
            count_incr += 1
    if count_incr == 5:
        return True
    else:
        return False


def duplicated_digits_one(num):
    num_list = [int(x) for x in str(num)]
    count_dupe = 0
    for d in range(len(num_list) - 1):
        if num_list[d] == num_list[d + 1]:
            count_dupe += 1
    if count_dupe >= 1:
        return True
    else:
        return False


def duplicated_digits_two(num):
    num_list = [int(x) for x in str(num)]
    count_dupe = 0
    for d in range(len(num_list) - 1):
        if d == 0:
            if num_list[d] == num_list[d + 1] and num_list[d] != num_list[d + 2]:
                count_dupe += 1
        elif d == 4:
            if num_list[d] == num_list[d + 1] and num_list[d] != num_list[d - 1]:
                count_dupe += 1
        else:
            if num_list[d] == num_list[d + 1] and num_list[d] != num_list[d + 2] and num_list[d] != num_list[d - 1]:
                count_dupe += 1
    if count_dupe >= 1:
        return True
    else:
        return False


def main(range_low, range_high):
    result = 0
    for num in range(range_low, range_high):
        if increasing_digits(num) and duplicated_digits_two(num):
            result += 1
    return result


if __name__ == '__main__':
    ans = main(206938, 679128)
    print(ans)
    # test_data = [112233, 123444, 111122, 111112, 112345]
    # for test in test_data:
    #     print(test, duplicated_digits_two(test))
