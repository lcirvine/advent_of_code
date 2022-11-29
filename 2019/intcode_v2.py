class Intcode:
    def __init__(self, data_file, idx, input_instruction):
        with open(data_file) as f:
            data = f.read()
        self.data = [int(x) for x in data.split(',')]
        self.idx = idx
        self.input_instruction = input_instruction

    def parameters(self):
        instruction = str(self.data[self.idx])
        instruction = '0' * (5 - len(instruction)) + str(instruction)
    
        opcode = int(instruction[3:5])
    
        param1_value = int(instruction[2])
        if param1_value == 0:
            param1_value = self.data[self.idx + 1]
        elif param1_value == 1:
            param1_value = self.idx + 1
    
        param2_value = int(instruction[1])
        if param2_value == 0:
            param2_value = self.data[self.idx + 2]
        elif param2_value == 1:
            param2_value = self.idx + 2
    
        param3_value = int(instruction[0])
        if param3_value == 0:
            param3_value = self.data[self.idx + 3]
        elif param3_value == 1:
            param3_value = self.idx + 3
    
        return opcode, param1_value, param2_value, param3_value

    def run_intcode(self):
        while self.idx < len(self.data):
            opcode, param1, param2, param3 = self.parameters()
            if opcode == 1:
                self.data[param3] = self.data[param1] + self.data[param2]
                self.idx += 4
            if opcode == 2:
                self.data[param3] = self.data[param1] * self.data[param2]
                self.idx += 4
            if opcode == 3:
                self.data[param1] = self.input_instruction
                self.idx += 2
            if opcode == 4 or opcode == 99:
                if self.data[param1] != 0 and self.data[self.idx + 2] == 99:
                    print(f'Diagnostic test succeeded, final output {self.data[param1]}')
                    break
                elif self.data[param1] != 0 and self.data[self.idx + 2] != 99:
                    print(f'Diagnostic test failed, final output {self.data[param1]}')
                    break
                self.idx += 2
            if opcode == 5:
                if self.data[param1] != 0:
                    self.idx = self.data[param2]
                else:
                    self.idx += 3
            if opcode == 6:
                if self.data[param1] == 0:
                    self.idx = self.data[param2]
                else:
                    self.idx += 3
            if opcode == 7:
                if self.data[param1] < self.data[param2]:
                    self.data[param3] = 1
                else:
                    self.data[param3] = 0
                self.idx += 4
            if opcode == 8:
                if self.data[param1] == self.data[param2]:
                    self.data[param3] = 1
                else:
                    self.data[param3] = 0
                self.idx += 4
        return self.data[param1]


if __name__ == '__main__':
    ic = Intcode('day5_input.txt', 0, 5)
    print(ic.run_intcode())
