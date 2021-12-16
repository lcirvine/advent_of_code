import os

with open(os.path.join('inputs', 'day16_key.txt')) as f:
    hexkey = {}
    binkey = {}
    for i in f.read().split('\n'):
        h, b = i.split(' = ')
        hexkey[h] = b
        binkey[b] = h
    # hexkey = {i.split(' = ')[0]: i.split(' = ')[1] for i in f.read().split('\n')}



def read_input(file: str):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    return data


def convert_to_binary(hexstr: str):
    return ''.join([hexkey[char] for char in hexstr])


def parse_binary(binstr: str, sum_v=0, literal_val_total=0, remaining_packet_num=0, remaining_packet_len=0):

    sum_v += int(binkey['0' + binstr[:3]])
    t = int(binkey['0' + binstr[3:6]])

    if t == 4:  # literal value
        packet_bits = binstr[6:]
        first_bits = [p for p in packet_bits[::5]]
        # including the first packet that starts with 0
        first_zero = first_bits.index('0') + 1
        literal_val = ''
        for packet in [packet_bits[x: x + 5] for x in range(0, 5 * first_zero, 5)]:
            literal_val += packet[1:5]
        literal_val_total += int(literal_val, 2)
    else:  # operator
        len_id = int(binstr[6:7])
        binstr = binstr[7:]
        if len_id == 0:
            sub_len = int(binstr[:15], 2)
            binstr = binstr[15:]
            remaining_packet_len = sub_len
        elif len_id == 1:
            sub_num = int(binstr[: 11], 2)
            binstr = binstr[11:]
            remaining_packet_num = sub_num
    return sum_v


def part_2():
    pass


if __name__ == '__main__':
    binstr = convert_to_binary('D2FE28')
    print(parse_binary(binstr))
