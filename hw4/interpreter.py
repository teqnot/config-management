import sys
import yaml

class VirtualMachine:
    def __init__(self, memSize):
        self.memory = [0] * memSize
        self.registers = [0] * 64
        self.pc = 0

    def execute(self, binFile):
        with open(binFile, 'rb') as f:
            code = f.read()

        while self.pc < len(code):
            instruction = code[self.pc]
            self.pc += 1

            if instruction == 0x5C: # LOAD_CONST
                B = code[self.pc]
                C = code[self.pc + 1]
                self.pc += 2
                self.registers[B] = C
                print(f"LOAD_CONST: R[{B}] = {C}, Registers: {self.registers}")
                continue
            
            elif instruction == 0x2B: # READ_MEM
                B = code[self.pc]
                C = code[self.pc + 1]
                self.pc += 2
                self.registers[B] = self.memory[self.registers[C]]
                print(f"READ_MEM: R[{B}] = M[R[{C}]] ({self.registers[C]}), Registers: {self.registers}, Memory: {self.memory}")
                continue

            elif instruction == 0x3A: # WRITE_MEM
                B = code[self.pc]
                C = code[self.pc + 1]
                self.pc += 2
                self.memory[self.registers[B]] = self.registers[C]
                print(f"WRITE_MEM: M[R[{B}]] = R[{C}] ({self.registers[C]}), Registers: {self.registers}, Memory: {self.memory}")
                continue

            elif instruction == 0xC1: # BITREVERSE
                B = code[self.pc]
                C = code[self.pc + 1]
                self.pc += 2
                value = self.registers[C]
                revValue = int('{:032b}'.format(value)[::-1], 2)
                self.registers[B] = revValue 
                print(f"BITREVERSE: R[{B}] = ~R[{C}] ({value}) => {revValue}, Registers: {self.registers}")
                continue

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[ Usage: python interpreter.py <binary_file> <result_file> ]")
        sys.exit(1)

    binFile = sys.argv[1]
    resFile = sys.argv[2]


    vm = VirtualMachine(memSize=256)
    vm.execute(binFile)

    resData = {
        "registers": vm.registers,
        "memory": vm.memory
    }

    with open(resFile, 'w') as f:
        yaml.dump(resData, f)