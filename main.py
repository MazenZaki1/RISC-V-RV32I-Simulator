from instructions import instructions, decodeInstruction, executeInstruction
from utilities import readStartingAddress
from registers import registers, Registers

Labels = {}
stackPointer = {}
dataMemory = {}

currentInstruction = instructions("N/A", -1, -1, -1, -1, -1, -1, -1, -1, -1, False)
startingAddress = readStartingAddress('input.txt')
programCounter = int(startingAddress)

with open('input.txt', 'r') as instructionFile:
    for instructionLine in instructionFile:
        decodeInstruction(instructionLine)
        executeInstruction(currentInstruction, Labels, stackPointer, dataMemory, programCounter)
        programCounter += 4
    
    for reg_name, reg_obj in Registers.items():
        print(f"Register {reg_name}:")
        print(f"Name: {reg_obj.name}")
        print(f"Value: {reg_obj.value}")
        print()