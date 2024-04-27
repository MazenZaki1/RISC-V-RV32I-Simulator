from instructions import instructions, decodeInstruction, executeInstruction
from utilities import readStartingAddress, outputRegisters
from registers import registers, Registers

Labels = {}
stackPointer = {}

currentInstruction = instructions("N/A", -1, -2, -1, -1, -1, -1, -1, -1, -1, False)
startingAddress = input ("Enter Starting Address: ")
programCounter = int(startingAddress)

with open('input.txt', 'r') as instructionFile:
    for instructionLine in instructionFile:
        decodeInstruction(instructionLine, currentInstruction, Labels, programCounter)
        print(f"Instruction: {currentInstruction.name}")
        print(f"RD: {currentInstruction.rd}")
        print(f"RS1: {currentInstruction.rs1}")
        print(f"RS2: {currentInstruction.rs2}")
        print(f"IMM: {currentInstruction.immediate}")
        print(f"isLabel: {currentInstruction.isLabel}")
        print(Labels)
        executeInstruction(currentInstruction, Labels, stackPointer, programCounter)
        programCounter += 4

outputRegisters(programCounter)