from instructions import instructions, decodeInstruction, executeInstruction
from utilities import readStartingAddress
from registers import registers, Registers

Labels = {}
stackPointer = {}
dataMemory = {}

currentInstruction = instructions("N/A", -1, -2, -1, -1, -1, -1, -1, -1, -1, False)
startingAddress = readStartingAddress('input.txt')
programCounter = int(startingAddress)

with open('input.txt', 'r') as instructionFile:
    next(instructionFile)
    for instructionLine in instructionFile:
        decodeInstruction(instructionLine, currentInstruction, Labels, programCounter)
        #print(f"Instruction: {currentInstruction.name}")
        #print(f"RD: {currentInstruction.rd}")
        #print(f"RS1: {currentInstruction.rs1}")
        #print(f"RS2: {currentInstruction.rs2}")
        #print(f"IMM: {currentInstruction.immediate}")
        executeInstruction(currentInstruction, Labels, stackPointer, dataMemory, programCounter)
        programCounter += 4

    
    # Assuming you've already defined the Registers dictionary as shown in your code snippet

# ...

for i in range(32):
    if str(i) in Registers:
        print(f"{i}: {Registers[str(i)].name}, {Registers[str(i)].value}")
    else:
        print(f"{i}: Register not defined")
