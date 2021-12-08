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
display_reverse = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
for k, v in display.items():
    for letter in v:
        display_reverse[letter].append(k)


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
    entries = read_input('day8_test.txt')
    # I'm flipping this dictionary so that it is len(display): display
    display_len = {len(v): k for k, v in display.items() if k in [1, 4, 7, 8]}
    output_vals = {}
    for entry_num, entry in entries.items():
        entry_disp = {}
        # 1, 4, 7, 8- signals with unique lengths
        for sig in entry['signal_pat']:
            if len(sig) in display_len.keys():
                entry_disp[display_len[len(sig)]] = sig
        # 2 - display 1 contains c and f. display 2 is the only one that does not contain f
        # f value - display 2 is the only one that does not contain f
        # c value - the other letter in display 1 that is not f
        for letter in entry_disp[1]:
            for sig in entry['signal_pat']:
                if letter not in sig:
                    entry_disp[2] = sig
                    f = letter
                    c = [l for l in entry_disp[1] if l != f][0]
        # a value - display 7 has values a, c and f and display 1 only has c and f
        a = [l for l in entry_disp[7] if l not in entry_disp[1]][0]
        # b and d values - display 4 has b, c, d and f. c and f have been found so the remaining 2 are b and d
        # b shows up in 6 displays, d shows up in 7 displays
        for l in [x for x in entry_disp[4] if x not in (c, f)]:
            signals_with_letter = [x for x in entry['signal_pat'] if l in x]
            if len(signals_with_letter) == 6:
                b = l
            elif len(signals_with_letter) == 7:
                d = l
        # g value - displays 3 and 4 have 5 letters and the only unknown is g
        for sig in [s for s in entry['signal_pat'] if len(s) == 5]:
            unknown_letters = [l for l in sig if l not in (a, b, c, d, f)]
            if len(unknown_letters) == 1:
                g = unknown_letters[0]
        # e value - the last unknown letter is e. Display 8 has all the letters so the unknown must be e
        e = [l for l in entry_disp[8] if l not in (a, b, c, d, f, g)][0]
        # fill in the remaining displays now that I have all the letters. Start with the longest first.
        for sig in entry['signal_pat']:
            if len(sig) == len(display[0]) and len([z for z in sig if z in (a, b, c, e, f, g)]) == len(display[0]):
                entry_disp[0] = sig
            # elif len(sig) == len(display[6]) and len([z for z in sig if z in (a, b, d, e, f, g)]) == len(display[6]):
            #     entry_disp[6] = sig
            elif len(sig) == len(display[9]) and len([z for z in sig if z in (a, b, c, d, f, g)]) == len(display[9]):
                entry_disp[9] = sig
            elif len(sig) == len(display[2]) and len([z for z in sig if z in (a, c, d, e, g)]) == len(display[2]):
                entry_disp[2] = sig
            elif len(sig) == len(display[3]) and len([z for z in sig if z in (a, c, d, f, g)]) == len(display[3]):
                entry_disp[3] = sig
            # elif len(sig) == len(display[5]) and len([z for z in sig if z in (a, b, d, f, g)]) == len(display[5]):
            #     entry_disp[5] = sig
            elif len(sig) == len(display[6]):
                entry_disp[6] = sig
            elif len(sig) == len(display[5]):
                entry_disp[5] = sig
        assert len(entry_disp.keys()) == 10, f"\nMissing keys in {entry_num}\n{entry}\n{len(entry_disp)}\n{entry_disp}"
        str_val = ''
        for out in entry['output']:
            for val, code in entry_disp.items():
                if len(out) == len(code) and len([j for j in code if j in out]) == len(out):
                    str_val += str(val)
        output_vals[entry_num] = int(str_val)
    print(output_vals)
    return sum(output_vals.values())


if __name__ == '__main__':
    print(part_1())
    print(part_2())
