import os

display = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],          # 6
    1: ['c', 'f'],                              # 2
    2: ['a', 'c', 'd', 'e', 'g'],               # 5
    3: ['a', 'c', 'd', 'f', 'g'],               # 5
    4: ['b', 'c', 'd', 'f'],                    # 4
    5: ['a', 'b', 'd', 'f', 'g'],               # 5
    6: ['a', 'b', 'd', 'e', 'f', 'g'],          # 6
    7: ['a', 'c', 'f'],                         # 3
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],     # 7
    9: ['a', 'b', 'c', 'd', 'f', 'g']           # 6
}


def read_input(file: str = 'day8.txt'):
    with open(os.path.join('inputs', file)) as f:
        data = f.read().split('\n')
    entries = {}
    for i, line in enumerate(data):
        signal_pat = line.split(' | ')[0].split(' ')
        output = line.split(' | ')[1].split(' ')
        entries[i] = {'signal_pat': signal_pat, 'output': output}
    return entries


def part_1():
    """How many times do digits 1, 4, 7, or 8 appear"""
    entries = read_input('day8.txt')
    # I'm flipping this dictionary so that it is len(display): display
    display_len = {len(v): k for k, v in display.items() if k in [1, 4, 7, 8]}
    display_counts = {v: 0 for v in display_len.values()}
    for i, entry in entries.items():
        for out in entry['output']:
            if len(out) in display_len.keys():
                display_counts[display_len[len(out)]] += 1
    return sum(display_counts.values())


def part_2():
    entries = read_input('day8.txt')
    # I'm flipping this dictionary so that it is len(display): display
    display_len = {len(v): k for k, v in display.items() if k in [1, 4, 7, 8]}
    output_vals = {}
    for entry_num, entry in entries.items():
        entry_disp = {}
        # 1, 4, 7, 8- signals with unique lengths
        for sig in entry['signal_pat']:
            if len(sig) in display_len.keys():
                entry_disp[display_len[len(sig)]] = sig
        # how many times does each letter appear in each signal?
        num_appearances = {}
        for letter in 'abcdefg':
            num_appearances[letter] = len([sig for sig in entry['signal_pat'] if letter in sig])
        # f value - f is in 9 displays (display 2 is the only one that does not contain f)
        f = [x for x in num_appearances if num_appearances[x] == 9][0]
        # e value - e is in only 4 displays
        e = [x for x in num_appearances if num_appearances[x] == 4][0]
        # b value - b is in only 6 displays
        b = [x for x in num_appearances if num_appearances[x] == 6][0]
        # 2 - display 2 is the only one that does not contain f
        for sig in entry['signal_pat']:
            if f not in sig:
                entry_disp[2] = sig
        # c value - the other letter in display 1 that is not f
        c = [x for x in entry_disp[1] if x != f][0]
        # a value - display 7 has values a, c and f and display 1 only has c and f
        a = [x for x in entry_disp[7] if x not in entry_disp[1]][0]
        # d value - display 4 has b, c, d and f. b, c and f have been found so the remaining one is d
        d = [x for x in entry_disp[4] if x not in (b, c, f)][0]
        # g value - g is the last unknown, it should be the only letter in display 8 that is unknown
        g = [x for x in entry_disp[8] if x not in (a, b, c, d, e, f)][0]
        # fill in the remaining displays now that I have all the letters (I already have 1, 4, 7, 8 and 2)
        for sig in entry['signal_pat']:
            if all(x in sig for x in [a, b, c, e, f, g]) and all(x in [a, b, c, e, f, g] for x in sig):
                entry_disp[0] = sig
            elif all(x in sig for x in [a, b, d, e, f, g]) and all(x in [a, b, d, e, f, g] for x in sig):
                entry_disp[6] = sig
            elif all(x in sig for x in [a, b, c, d, f, g]) and all(x in [a, b, c, d, f, g] for x in sig):
                entry_disp[9] = sig
            elif all(x in sig for x in [a, c, d, f, g]) and all(x in [a, c, d, f, g] for x in sig):
                entry_disp[3] = sig
            elif all(x in sig for x in [a, b, d, f, g]) and all(x in [a, b, d, f, g] for x in sig):
                entry_disp[5] = sig
        assert len(entry_disp.keys()) == 10, f"\nMissing keys in {entry_num}\n{entry}\n{len(entry_disp)}\n{entry_disp}"
        str_val = ''
        for out in entry['output']:
            for val, code in entry_disp.items():
                if all(x in out for x in code) and all(x in code for x in out):
                    str_val += str(val)
        assert len(str_val) == 4, f"\nEntry\n{entry}\nEntry Disp\n{entry_disp}\nOutput so far\n{output_vals}\nLatest output\n{out}"
        output_vals[entry_num] = int(str_val)
    return sum(output_vals.values())


if __name__ == '__main__':
    print(part_1())
    print(part_2())
