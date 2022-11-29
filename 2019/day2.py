import os


def get_input():
    with open(os.path.join(os.getcwd(), 'day2_input.txt')) as f:
        day2_data = f.read()
    data = [int(x) for x in day2_data.split(',')]
    return data


def part_one(noun, verb):
    intcode = get_input()
    # before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    intcode[1] = noun
    intcode[2] = verb
    instruction_pointer = 0
    for x in range(len(intcode)):
        opcode = intcode[0 + instruction_pointer]
        noun = intcode[1 + instruction_pointer]
        verb = intcode[2 + instruction_pointer]
        position = intcode[3 + instruction_pointer]
        if opcode == 1:
            intcode[position] = intcode[noun] + intcode[verb]
        elif opcode == 2:
            intcode[position] = intcode[noun] * intcode[verb]
        elif opcode == 99:
            return intcode[0]
        else:
            print('Something is wrong...')
            print(intcode)
            break
        instruction_pointer += 4


def part_two(expected_result):
    for x in range(100):
        for y in range(100):
            if part_one(x, y) == expected_result:
                return 100 * x + y


if __name__ == '__main__':
    print(part_one(12, 2))
    print(part_two(19690720))
