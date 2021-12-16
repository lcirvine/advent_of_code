import os

with open(os.path.join('inputs', 'day16_key.txt')) as f:
    hexkey = {}
    binkey = {}
    for i in f.read().split('\n'):
        h, b = i.split(' = ')
        hexkey[h] = b
        binkey[b] = h
    # hexkey = {i.split(' = ')[0]: i.split(' = ')[1] for i in f.read().split('\n')}


def read_input(file: str = 'day16.txt'):
    with open(os.path.join('inputs', file)) as f:
        data = f.read()
    return data


def convert_to_binary(hexstr: str):
    return ''.join([hexkey[char] for char in hexstr])


def parse_binary(binstr: str, sum_v=0, val=0):
    sum_v += int(binkey['0' + binstr[:3]])
    t = int(binkey['0' + binstr[3:6]])

    if t == 4:  # literal value
        # remaining_packet_num = max([(remaining_packet_num - 1), 0])
        binstr = binstr[6:]
        first_bits = [p for p in binstr[::5]]
        # including the first packet that starts with 0
        first_zero = first_bits.index('0') + 1
        literal_val = ''
        for packet in [binstr[x: x + 5] for x in range(0, 5 * first_zero, 5)]:
            literal_val += packet[1:5]
        val += int(literal_val, 2)
        # what's remaining at the end of this literal string?
        binstr = binstr[5 * first_zero:]
        # remaining_packet_len = max([(remaining_packet_num - (5 * first_zero) + 6), 0])
    else:  # operator
        # remaining_packet_num = max([(remaining_packet_num - 1), 0])
        len_id = int(binstr[6:7])
        binstr = binstr[7:]
        if len_id == 0:
            sub_len = int(binstr[:15], 2)
            binstr = binstr[15:]
            # remaining_packet_len += sub_len
        elif len_id == 1:
            sub_num = int(binstr[: 11], 2)
            binstr = binstr[11:]
            # remaining_packet_num += sub_num
    if len(binstr) > 8:
        return parse_binary(binstr, sum_v, val)
    return sum_v


def part_2():
    pass


if __name__ == '__main__':
    hexcode = read_input()
    binstr = convert_to_binary(hexcode)
    print(parse_binary(binstr))
