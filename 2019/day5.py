import os


with open(os.path.join(os.getcwd(), 'day5_input.txt')) as f:
    day5_data = f.read()
data = [int(x) for x in day5_data.split(',')]


def parameters(intcode_data, instruction_pointer):
    instruction = str(intcode_data[instruction_pointer])
    instruction = '0' * (5 - len(instruction)) + str(instruction)

    opcode = int(instruction[3:5])

    param1_value = int(instruction[2])
    if param1_value == 0:
        param1_value = intcode_data[instruction_pointer + 1]
    elif param1_value == 1:
        param1_value = instruction_pointer + 1

    param2_value = int(instruction[1])
    if param2_value == 0:
        param2_value = intcode_data[instruction_pointer + 2]
    elif param2_value == 1:
        param2_value = instruction_pointer + 2

    param3_value = int(instruction[0])
    if param3_value == 0:
        param3_value = intcode_data[instruction_pointer + 3]
    elif param3_value == 1:
        param3_value = instruction_pointer + 3

    return opcode, param1_value, param2_value, param3_value


input_instruction = 5
idx = 0
while idx < len(data):
    opcode, param1, param2, param3 = parameters(data, idx)
    if opcode == 1:
        data[param3] = data[param1] + data[param2]
        idx += 4
    if opcode == 2:
        data[param3] = data[param1] * data[param2]
        idx += 4
    if opcode == 3:
        data[param1] = input_instruction
        idx += 2
    if opcode == 4 or opcode == 99:
        if data[param1] != 0 and data[idx + 2] == 99:
            print(f'Diagnostic test succeeded, final output {data[param1]}')
            break
        elif data[param1] != 0 and data[idx + 2] != 99:
            print(f'Diagnostic test failed, final output {data[param1]}')
            break
        idx += 2
    if opcode == 5:
        if data[param1] != 0:
            idx = data[param2]
        else:
            idx += 3
    if opcode == 6:
        if data[param1] == 0:
            idx = data[param2]
        else:
            idx += 3
    if opcode == 7:
        if data[param1] < data[param2]:
            data[param3] = 1
        else:
            data[param3] = 0
        idx += 4
    if opcode == 8:
        if data[param1] == data[param2]:
            data[param3] = 1
        else:
            data[param3] = 0
        idx += 4
