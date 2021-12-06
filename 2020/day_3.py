import os


with open(os.path.join('Inputs', 'day_3.txt')) as f:
    data = f.read().split('\n')


def part_1(x_inc: int, y_inc: int):
    with open('day 3 trail.txt', 'w') as f:
        x_pos = 0
        y_pos = 0
        coords = []
        result_dict = {'.': 'O', '#': 'X'}
        results = []
        for r in data:
            row = [x for x in r]
            coords.append((x_pos, y_pos))
            row_len = len(row)
            x_pos %= row_len
            square = row[x_pos]
            results.append(square)
            row.insert(x_pos, result_dict[square])
            x_pos += x_inc
            y_pos += y_inc
            f.write(str(row) + '\n')
        trees_hit = len([x for x in results if x == '#'])
    print(f"number of trees hit {trees_hit}")


def part_2(x_inc: int, y_inc: int):
    x_pos = 0
    y_pos = 0
    coords = []
    result_dict = {'.': 'O', '#': 'X'}
    results = []
    for r in data[::y_inc]:
        row = [x for x in r]
        coords.append((x_pos, y_pos))
        row_len = len(row)
        x_pos %= row_len
        square = row[x_pos]
        results.append(square)
        row.insert(x_pos, result_dict[square])
        x_pos += x_inc
        y_pos += y_inc
    trees_hit = len([x for x in results if x == '#'])
    return trees_hit


if __name__ == '__main__':
    part_1(3, 1)
    pt2_answer_list = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for s in slopes:
        pt2_answer_list.append(part_2(s[0], s[1]))
    print(pt2_answer_list)
    pt2_answer = 1
    for answ in pt2_answer_list:
        pt2_answer *= answ
    print(pt2_answer)
