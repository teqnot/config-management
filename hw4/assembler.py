import sys
import yaml

COMMANDS = {
    "LOAD_CONST": 0x5C,
    "READ_MEM": 0x2B,
    "WRITE_MEM": 0x3A,
    "BITREVERSE": 0xC1
}

def assembleLine(line):
    tokens = line.split()
    command = tokens[0]

    if command == "LOAD_CONST":
        A = COMMANDS["LOAD_CONST"]
        B = int(tokens[1])
        C = int(tokens[2])
        return [A, B, C]

    elif command == "READ_MEM":
        A = COMMANDS["READ_MEM"]
        B = int(tokens[1])
        C = int(tokens[2])
        return [A, B, C]

    elif command == "WRITE_MEM":
        A = COMMANDS["WRITE_MEM"]
        B = int(tokens[1])
        C = int(tokens[2])
        return [A, B, C]

    elif command == "BITREVERSE":
        A = COMMANDS["BITREVERSE"]
        B = int(tokens[1])
        C = int(tokens[2])
        return [A, B, C]
    
    else:
        print(f"[ Error: Unknown command '{command}' at line '{line}' ]")
        return []
    

def assemble(filePath):
    binCode = []
    log = {}

    with open(filePath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                cmdBytes = assembleLine(line)
                binCode.extend(cmdBytes)
                log[line] = cmdBytes

    return binCode, log

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("[ Usage: python assembler.py <input_file> <output_bin_file> <output_log_file> ]")
        sys.exit(1)

    inputFile = sys.argv[1]
    outputBinFile = sys.argv[2]
    logFile = sys.argv[3]

    binCode, log = assemble(inputFile)
    
    with open(outputBinFile, 'wb') as binf:
        binf.write(bytearray(binCode))
    
    with open(logFile, 'w') as logf:
        yaml.dump(log, logf)