import os
import re

with open(os.path.join('Inputs', 'day_4.txt')) as f:
    pp = f.read().split('\n\n')

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_keys = ['cid']


def part_1():
    valid_count = 0
    for p in pp:
        if all(item in p for item in required_keys):
            valid_count += 1
    return valid_count


def part_2():

    def byr_check(passport: str, year_low: int = 1920, year_high: int = 2002):
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        byr_pat = re.compile(r'byr:\s?(\d{4})\b')
        try:
            byr = int(byr_pat.search(passport).group(1))
            if byr in range(year_low, year_high + 1):
                return byr
            else:
                return False
        except (ValueError, AttributeError):
            return False
    
    def iyr_check(passport, year_low: int = 2010, year_high: int = 2020):
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        iyr_pat = re.compile(r'iyr:\s?(\d{4})\b')
        try:
            iyr = int(iyr_pat.search(passport).group(1))
            if iyr in range(year_low, year_high + 1):
                return iyr
            else:
                return False
        except (ValueError, AttributeError):
            return False

    def eyr_check(passport, year_low: int = 2020, year_high: int = 2030):
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        eyr_pat = re.compile(r'eyr:\s?(\d{4})\b')
        try:
            eyr = int(eyr_pat.search(passport).group(1))
            if eyr in range(year_low, year_high + 1):
                return eyr
            else:
                return False
        except (ValueError, AttributeError):
            return False

    def hgt_check(passport):
        """hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76."""
        hgt_dict = {'cm': (150, 193), 'in': (59, 76)}
        hgt_pat = re.compile(r'hgt:\s?(\d*)(in|cm)\b')
        try:
            hgt, units = hgt_pat.search(passport).groups()
            hgt = int(hgt)
            if hgt in range(hgt_dict[units][0], hgt_dict[units][1] + 1):
                return hgt
        except (ValueError, AttributeError):
            return False

    def hcl_check(passport):
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        hcl_pat = re.compile(r'hcl:\s?(#[a-f0-9]{6})\b')
        try:
            hcl = hcl_pat.search(passport).group(1)
            if hcl:
                return hcl
        except (ValueError, AttributeError):
            return False

    def ecl_check(passport):
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        ecl_pat = re.compile(r'ecl:\s?([a-z]{3})\b')
        try:
            ecl = ecl_pat.search(passport).group(1)
            if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return ecl
        except (ValueError, AttributeError):
            return False

    def pid_check(passport):
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        pid_pat = re.compile(r'pid:\s?(\d{9})\b')
        try:
            pid = int(pid_pat.search(passport).group(1))
            if pid:
                return pid
        except (ValueError, AttributeError):
            return False

    valid_count = 0
    checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    with open(os.path.join('Tests', 'day 4 part 2.txt', 'w')) as f:
        for p in pp:
            f.write(p + '\n')
            p_results = [byr_check(p),
                         iyr_check(p),
                         eyr_check(p),
                         hgt_check(p),
                         hcl_check(p),
                         ecl_check(p),
                         pid_check(p)]
            f.write(str(dict(zip(checks, p_results))) + '\n')
            if all(p_results):
                valid_count += 1
                f.write('valid' + '\n\n')
            else:
                f.write('invalid' + '\n\n')
    return valid_count


if __name__ == '__main__':
    print(part_1())
    print(part_2())
