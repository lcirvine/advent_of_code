"""
The input is given as AAA)BBB where BBB orbits AAA.
This problem becomes a lot easier if you flip the dictionary
so that the key is the orbiting object and the value is the object it orbits.
"""

# x = VVV)KKK
# x[x.find(')' + 1:] = KKK
# x[0:x.find(')'] = VVV
# creates a dictionary of KKK: VVV
orbits = {x[x.find(')') + 1:]: x[0:x.find(')')] for x in open('day6_input.txt').read().split('\n')}


def part_one():
    """For each orbing object, find what objects it orbits."""
    orbit_count = 0
    for orbiting_object in orbits.keys():
        while orbiting_object in orbits:
            orbit_count += 1
            orbiting_object = orbits[orbiting_object]
    return orbit_count


def part_two():
    you_orbit = 'YOU'
    san_orbit = 'SAN'
    you_orbits = []
    san_orbits = []
    while you_orbit in orbits:
        you_orbits.append(orbits[you_orbit])
        you_orbit = orbits[you_orbit]
    while san_orbit in orbits:
        san_orbits.append(orbits[san_orbit])
        san_orbit = orbits[san_orbit]
    transfer_count = min([you_orbits.index(orbit) + san_orbits.index(orbit) for orbit in set(you_orbits) & set(san_orbits)])
    return transfer_count


if __name__ == '__main__':
    print(f'part one answer {part_one()}')
    print(f'part two answer {part_two()}')
