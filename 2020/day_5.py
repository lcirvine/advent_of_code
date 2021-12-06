import os


with open(os.path.join('Inputs', 'day_5.txt')) as f_input:
    data = f_input.read().split('\n')


def return_range(char: str, num_range: range, divisions: int = 2):
    half_range = len(num_range) // divisions
    if char in ['F', 'L']:
        return num_range[:half_range]
    elif char in ['B', 'R']:
        return num_range[half_range:]


def part_1():
    """
    Rows - The first 7 characters will either be F or B; specify exactly one of the 128 rows (0 through 127)
        F means to take the lower half (i.e. lower numbers)
        B means to take the upper half (i.e. higher numbers)
    Columns - The last three characters will be either L or R; specify exactly one of the 8 columns (0 through 7)
        L means to take the lower half (i.e. lower numbers)
        R means to take the upper half (i.e. higher numbers)
    :return:
    """
    seats = []
    for seat in data:
        row_str = seat[:7]
        row_range = range(0, 128)
        for char in row_str:
            row_range = return_range(char, row_range)
        col_str = seat[7:]
        col_range = range(0, 8)
        for char in col_str:
            col_range = return_range(char, col_range)
        seat_id = (row_range[0] * 8) + col_range[0]
        seats.append(seat_id)
    return seats


def part_2():
    seats = part_1()
    max_seat_id = (128 * 8) + 7
    seat_id_range = range(0, max_seat_id)
    missing_seats = [s for s in seat_id_range if s not in seats]
    return [x for x in missing_seats if x + 1 not in missing_seats and x - 1 not in missing_seats]


if __name__ == '__main__':
    print(max(part_1()))
    print(part_2())
