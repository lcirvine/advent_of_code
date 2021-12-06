import os

with open(os.path.join('Inputs', 'day_11.txt')) as f:
    seats = f.read().split('\n')


def adj_seats(seat: tuple):
    adjacent = []
    x = seat[0]
    y = seat[1]



def part_1():
    seat_d = {}
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            seat_d[(i, j)] = seats[i][j]


def part_2():
    pass


if __name__ == '__main__':
    print(part_1())
    # print(part_2())
