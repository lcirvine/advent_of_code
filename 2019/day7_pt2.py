# Part 1
from intcode_v3 import IntCode, InputInterrupt, OutputInterrupt
from itertools import permutations
from collections import deque


def run_sequence(sequence, prgm):
    amp = 0
    for phase in sequence:
        computer = IntCode(open('day7_input.txt').readline())
        computer.input_queue = deque([phase, amp])
        while (not computer.done):
            try:
                computer.run()
            except(OutputInterrupt):
                pass

        amp = computer.output_queue.popleft()

    return amp


# computer = IntCode(open('in\\7.in').readline())

sequences = permutations(range(5))
prgm = open('day7_input.txt').readline()
max_sequence = max(sequences, key=lambda x: run_sequence(x, prgm))

print(max_sequence)
print(run_sequence(max_sequence, prgm))


# Part 2

def run_sequence(sequence, prgm):
    computers = list()
    for phase in sequence:
        computers.append(IntCode(prgm))
        computers[-1].input_queue.append(phase)

    i = -1
    computers[0].input_queue.append(0)
    while (True):
        i = (i + 1) % 5
        while (not computers[i].done):
            try:
                computers[i].run()
            except(OutputInterrupt):
                computers[(i + 1) % 5].input_queue.append(computers[i].output_queue[-1])
                continue
            except(InputInterrupt):
                break

        if (all(map(lambda x: x.done, computers))):
            break

    return computers[0].input_queue[-1]


prgm = open('day7_input.txt').readline()

sequences = permutations(range(5, 10))

max_sequence = max(sequences, key=lambda x: run_sequence(x, prgm))

print(max_sequence)
print(run_sequence(max_sequence, prgm))
