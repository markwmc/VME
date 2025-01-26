class VM:
    def __init__(self):
        self.memory = [0] * 256
        self.registers = [0] * 4
        self.pc = 0
        self.stack = []
        
    def run(self, program):
        self.memory[:len(program)] = program

        while self.pc < len(self.memory):
            instruction = self.memory[self.pc]
            self.pc += 1
            self.execute(instruction)

    def execute(self, instruction):
        opcode = instruction & 0xF0
        operand = instruction & 0x0F

        if opcode == 0x10:
            reg_idx = operand
            value = self.memory[self.pc]
            self.registers[reg_idx] = value
            self.pc += 1
        
        elif opcode == 0x20:
            reg_idx1 = operand >> 2
            reg_idx2 = operand & 0x03
            self.registers[reg_idx1] += self.registers[reg_idx2]

        elif opcode == 0x30:
            reg_idx = operand
            self.stack.append(self.registers[reg_idx])
        
        elif opcode == 0x40:
            reg_idx = operand
            if self.stack:
                self.registers[reg_idx] = self.stack.pop()
        
        else:
            print(f"Unknown opcode {hex(opcode)}")