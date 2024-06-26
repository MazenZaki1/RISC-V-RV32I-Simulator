from registers import registers, Registers
from utilities import doesLineContainLabel, binaryToDecimal, outputRegisters
#import sys
#sys.path.append(r 'C:\Users\nourt\OneDrive\Documents\Desktop')


class instructions:
    def __init__(self, name, opcode, funct3, rd=None, rs1=None, rs2=None, funct7=None, immediate=0, type=None, label=None, isLabel=False):
        self.name = name
        self.opcode = opcode
        self.rd = rd
        self.funct3 = funct3
        self.rs1 = rs1
        self.rs2 = rs2
        self.funct7 = funct7
        self.immediate = immediate
        self.type = type
        self.label = label
        self.isLabel = isLabel

Instructions = { #This is the dictionary that contains each insturction
    "LUI": instructions("LUI", 0b0110111, None, type="U"),
    "AUIPC": instructions("AUIPC", 0b0010111, None, type="U"),
    "JAL": instructions("JAL", 0b1101111, None, type="J"),
    "JALR": instructions("JALR", 0b1100111, 0b000, type="I"),
    "BEQ": instructions("BEQ", 0b1100011, 0b000, type="B"),
    "BNE": instructions("BNE", 0b1100011, 0b001, type="B"),
    "BLT": instructions("BLT", 0b1100011, 0b100, type="B"),
    "BGE": instructions("BGE", 0b1100011, 0b101, type="B"),
    "BLTU": instructions("BLTU", 0b1100011, 0b110, type="B"),
    "BGEU": instructions("BGEU", 0b1100011, 0b111, type="B"),
    "LB": instructions("LB", 0b0000011, 0b000, type="I"),
    "LH": instructions("LH", 0b0000011, 0b001, type="I"),
    "LW": instructions("LW", 0b0000011, 0b010, type="I"),
    "LBU": instructions("LBU", 0b0000011, 0b100, type="I"),
    "LHU": instructions("LHU", 0b0000011, 0b101, type="I"),
    "SB": instructions("SB", 0b0100011, 0b000, type="S"),
    "SH": instructions("SH", 0b0100011, 0b001, type="S"),
    "SW": instructions("SW", 0b0100011, 0b010, type="S"),
    "ADDI": instructions("ADDI", 0b0010011, 0b000, type="I"),
    "SLTI": instructions("SLTI", 0b0010011, 0b010, type="I"),
    "SLTIU": instructions("SLTIU", 0b0010011, 0b011, type="I"),
    "XORI": instructions("XORI", 0b0010011, 0b100, type="I"),
    "ORI": instructions("ORI", 0b0010011, 0b110, type="I"),
    "ANDI": instructions("ANDI", 0b0010011, 0b111, type="I"),
    "SLLI": instructions("SLLI", 0b0010011, 0b001, 0b0000000, type="R"),
    "SRLI": instructions("SRLI", 0b0010011, 0b101, 0b0000000, type="R"),
    "SRAI": instructions("SRAI", 0b0010011, 0b101, 0b0100000, type="R"),
    "ADD": instructions("ADD", 0b0110011, 0b000, 0b0000000, type="R"),
    "SUB": instructions("SUB", 0b0110011, 0b000, 0b0100000, type="R"), 
    "SLL": instructions("SLL", 0b0110011, 0b001, 0b0000000, type="R"),
    "SLT": instructions("SLT", 0b0110011, 0b010, 0b0000000, type="R"),
    "SLTU": instructions("SLTU", 0b0110011, 0b011, 0b0000000, type="R"),
    "XOR": instructions("XOR", 0b0110011, 0b100, 0b0000000, type="R"),
    "SRL": instructions("SRL", 0b0110011, 0b101, 0b0000000, type="R"),
    "SRA": instructions("SRA", 0b0110011, 0b101, 0b0100000, type="R"),
    "OR": instructions("OR", 0b0110011, 0b110, 0b0000000, type="R"),
    "AND": instructions("AND", 0b0110011, 0b111, 0b0000000, type="R"),
    "FENCE": instructions("FENCE", 0b0001111, 0b000, type="I"),
    "ECALL": instructions("ECALL", 0b1110011, 0b000, type="I"),
    "EBREAK": instructions("EBREAK", 0b1110011, 0b000, type="I")
}

def resetCurrentInstruction(currentInstruction):
    currentInstruction = instructions("N/A", -1, -1, -1, -1, -1, -1, -1, -1, -1, False)

def decodeInstruction(instruction_line, currentInstruction, labelsDictionary, instructionAddress):
    
    resetCurrentInstruction(currentInstruction)
    print(f"The instruction line is: {instruction_line}")
    if (instruction_line == "\n" or instruction_line == "" or instruction_line == " "):
        return None
    instructionList=instruction_line.strip().upper().replace(",", "").split()
    print(f"The instruction list is: {instructionList}")
    currentInstruction.name=instructionList[0]


    if (currentInstruction.name == "JAL"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.rd = instructionList[1][1:]
        currentInstruction.label = instructionList[2]
        return currentInstruction

    elif (currentInstruction.name == "JALR"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.rd = instructionList[1][1:]
        currentInstruction.rs1 = instructionList[2][1:]
        currentInstruction.immediate = instructionList[3]
        return currentInstruction
    
    elif  (currentInstruction.name == "BEQ" or currentInstruction.name == "BNE" or currentInstruction.name == "BLT" or 
        currentInstruction.name == "BGE" or currentInstruction.name == "BLTU" or currentInstruction.name == "BGEU"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.rs1 = instructionList[1][1:]
        currentInstruction.rs2 = instructionList[2][1:]
        currentInstruction.label = instructionList[3]
        return currentInstruction

    elif (currentInstruction.name == "LB" or currentInstruction.name == "LH" or currentInstruction.name == "LW" or 
        currentInstruction.name == "LBU" or currentInstruction.name == "LHU" or currentInstruction.name == "SB"
        or currentInstruction.name == "SH" or currentInstruction.name == "SW"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.rd = instructionList[1][1:]
        findBracket = instructionList[2].find("(")
        currentInstruction.immediate = int(instructionList[2][:findBracket])
        currentInstruction.rs1 = instructionList[2][findBracket+2:-1]
        return currentInstruction
    
    elif (currentInstruction.name == "ADDI" or currentInstruction.name == "SLTI" or currentInstruction.name == "SLTIU" or 
        currentInstruction.name == "XORI" or currentInstruction.name == "ORI" or currentInstruction.name == "ANDI" or
        currentInstruction.name == "SLLI" or currentInstruction.name == "SRLI" or currentInstruction.name == "SRAI"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.rd = instructionList[1][1:]
        currentInstruction.rs1 = instructionList[2][1:]
        currentInstruction.immediate = instructionList[3]
        return currentInstruction
    
    elif (currentInstruction.name == "ADD" or currentInstruction.name == "SUB" or currentInstruction.name == "SLL" or currentInstruction.name == "SLT" or
        currentInstruction.name == "SLTU" or currentInstruction.name == "XOR" or currentInstruction.name == "SRL" or currentInstruction.name == "SRA" or
        currentInstruction.name == "OR" or currentInstruction.name == "AND"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.rd = instructionList[1][1:]
        currentInstruction.rs1 = instructionList[2][1:]
        currentInstruction.rs2 = instructionList[3][1:]
        return currentInstruction

    elif (currentInstruction.name == "FENCE"):
        resetCurrentInstruction(currentInstruction)
        currentInstruction.name = "FENCE"
    
    elif (currentInstruction.name == "ECALL" or currentInstruction.name == "EBREAK"): # For example, 'JAL rd, imm' which is J-Type
        resetCurrentInstruction(currentInstruction)
        currentInstruction.name = instructionList[0]
    elif (doesLineContainLabel(currentInstruction.name)):
        currentInstruction.isLabel = True
        labelsDictionary[currentInstruction.name] = instructionAddress

def executeInstruction(currentInstruction, labelsDictionary, stackPointerDictionary, programCounter):
    if (currentInstruction.name == "LUI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = currentInstruction.immediate << 12

    if (currentInstruction.name == "AUIPC"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = (Registers[currentInstruction.immediate].value << 12) + programCounter

    if (currentInstruction.name == "JAL"):
        if (currentInstruction.rd == 0):
            Registers[currentInstruction.rd].value = 0
        else:
            Registers[currentInstruction.rd].value = programCounter + 4
        programCounter = labelsDictionary[currentInstruction.label] - 4
    
    if (currentInstruction.name=="JALR"):
        if (currentInstruction.rd == 0):
            Registers[currentInstruction.rd].value = 0
        else:
            Registers[currentInstruction.rd] = currentInstruction.immediate + Registers[currentInstruction.rs1].value
        programCounter = currentInstruction.immediate + Registers[currentInstruction.rs1].value - 4

    if (currentInstruction.name=="BEQ"):
        if (Registers[currentInstruction.rs1].value == Registers[currentInstruction.rs2].value):
            programCounter = labelsDictionary[currentInstruction.label] - 4

    if (currentInstruction.name=="BNE"):
        if (Registers[currentInstruction.rs1].value != Registers[currentInstruction.rs2].value):
            programCounter = labelsDictionary[currentInstruction.label] - 4

    if (currentInstruction.name=="BLT"):
        if (Registers[currentInstruction.rs1].value < Registers[currentInstruction.rs2].value):
            programCounter = labelsDictionary[currentInstruction.label] - 4

    if (currentInstruction.name=="BGE"):
        if (Registers[currentInstruction.rs1].value >= Registers[currentInstruction.rs2].value):
            programCounter = labelsDictionary[currentInstruction.label] - 4
    
    if (currentInstruction.name=="BLTU"):
        if (Registers[currentInstruction.rs1].value < Registers[currentInstruction.rs2].value):
            programCounter = labelsDictionary[currentInstruction.label] - 4

    if (currentInstruction.name=="BGEU"):
        if (Registers[currentInstruction.rs1].value >= Registers[currentInstruction.rs2].value):
            programCounter = labelsDictionary[currentInstruction.label] - 4
    
    if (currentInstruction.name=="LB"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = currentInstruction.immediate + Registers[currentInstruction.rs1].value
    
    if (currentInstruction.name=="LH"):
        if (currentInstruction.rd == 0):
            return
        else:
           Registers[currentInstruction.rd].value = currentInstruction.immediate + Registers[currentInstruction.rs1].value

    if (currentInstruction.name=="LW"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = currentInstruction.immediate + Registers[currentInstruction.rs1].value

    if (currentInstruction.name=="LBU"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = currentInstruction.immediate + Registers[currentInstruction.rs1].value
    
    if (currentInstruction.name=="LHU"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = currentInstruction.immediate + Registers[currentInstruction.rs1].value
    """
    if (currentInstruction.name=="SB"):
        if (currentInstruction.rs1 == 2):
            stack = Registers[2].value + currentInstruction.immediate
            value = bin(Registers[currentInstruction.rd].value)[2:]
            stackPointerDictionary[stack].dat_val = value
        else:
            startAddress = currentInstruction.immediate + Registers[currentInstruction.rs1].value
            value = bin(Registers[currentInstruction.rd].value)[2:]
            dataMemoryDictionary[startAddress].dat_val = Registers[currentInstruction.rd].value
    
    if (currentInstruction.name=="SH"):
        if (currentInstruction.rs1 == 2):
            stack = Registers[2].value + currentInstruction.immediate
            value = bin(Registers[currentInstruction.rd].value)[2:]
            stackPointerDictionary[stack].dat_val = value
        else:
            startAddress = currentInstruction.immediate + Registers[currentInstruction.rs1].value
            value = bin(Registers[currentInstruction.rd].value)[2:]
            dataMemoryDictionary[startAddress].dat_val = value[8:]
            dataMemoryDictionary[startAddress+1].dat_val = value[:8]
    
    if (currentInstruction.name=="SW"):
        if (currentInstruction.rs1 == 2):
            stack = Registers[2].value + currentInstruction.immediate
            value = bin(Registers[currentInstruction.rd].value)[:32]
            stackPointerDictionary[stack+3].dat_val = value[:8]
            stackPointerDictionary[stack+2].dat_val = value[8:8]
            stackPointerDictionary[stack+1].dat_val = value[16:8]
            stackPointerDictionary[stack].dat_val = value[24:8]
        else:
            startAddress = currentInstruction.immediate + Registers[currentInstruction.rs1].value
            value = bin(Registers[currentInstruction.rd].value)[:32]
            dataMemoryDictionary[startAddress].dat_val = value[24:8]
            dataMemoryDictionary[startAddress+1].dat_val = value[16:8]
            dataMemoryDictionary[startAddress+2].dat_val = value[8:8]
            dataMemoryDictionary[startAddress+3].dat_val = value[:8]
    """
    if (currentInstruction.name=="ADDI"):
        if (currentInstruction.rd == 0):
            return
        elif (currentInstruction.rd == 2 and currentInstruction.rs1 == 2):
            size = currentInstruction.immediate
            if (size < 0):
                while (size != 0):
                    stackPointerDictionary[Registers[2].value+size].dat_val = "00000000"
                    size += 1
            if (size > 0):
                size = size * -1
                while (size != 0):
                    stackPointerDictionary[Registers[2].value+size].dat_val = "00000000"
                    size -= 1
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value + int(currentInstruction.immediate)
    
    if (currentInstruction.name=="SLTI"):
        if (currentInstruction.rd == 0):
            return
        else:
            if (Registers[currentInstruction.rs1].value < currentInstruction.immediate):
                Registers[currentInstruction.rd].value = 1
            else:
                Registers[currentInstruction.rd].value = 0
    
    if (currentInstruction.name=="SLTIU"):
        if (currentInstruction.rd == 0):
            return
        else:
            if (Registers[currentInstruction.rs1].value < currentInstruction.immediate):
                Registers[currentInstruction.rd].value = 1
            else:
                Registers[currentInstruction.rd].value = 0
    
    if (currentInstruction.name=="XORI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value ^ currentInstruction.immediate
    
    if (currentInstruction.name=="ORI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value | currentInstruction.immediate
    
    if (currentInstruction.name=="ANDI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value & currentInstruction.immediate

    if (currentInstruction.name=="SLLI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value << currentInstruction.immediate
    
    if (currentInstruction.name=="SRLI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value >> currentInstruction.immediate
    
    if (currentInstruction.name=="SRAI"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value >> currentInstruction.immediate
    
    if (currentInstruction.name=="ADD"):
        if (currentInstruction.rd == 0):
            return
        else:
            print(Registers[currentInstruction.rd].value)
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value + Registers[currentInstruction.rs2].value

    if (currentInstruction.name=="SUB"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value - Registers[currentInstruction.rs2].value
    
    if (currentInstruction.name=="SLL"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value << Registers[currentInstruction.rs2].value
    
    if (currentInstruction.name=="SLT"):
        if (currentInstruction.rd == 0):
            return
        else:
            if (Registers[currentInstruction.rs1].value < Registers[currentInstruction.rs2].value):
                Registers[currentInstruction.rd].value = 1
            else:
                Registers[currentInstruction.rd].value = 0
    
    if (currentInstruction.name=="SLTU"):
        if (currentInstruction.rd == 0):
            return
        else:
            if (Registers[currentInstruction.rs1].value < Registers[currentInstruction.rs2].value):
                Registers[currentInstruction.rd].value = 1
            else:
                Registers[currentInstruction.rd].value = 0
    
    if (currentInstruction.name=="XOR"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value ^ Registers[currentInstruction.rs2].value

    if (currentInstruction.name=="SRL"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value >> Registers[currentInstruction.rs2].value
    
    if (currentInstruction.name=="SRA"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value >> Registers[currentInstruction.rs2].value
    
    if (currentInstruction.name=="OR"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value | Registers[currentInstruction.rs2].value
    
    if (currentInstruction.name=="AND"):
        if (currentInstruction.rd == 0):
            return
        else:
            Registers[currentInstruction.rd].value = Registers[currentInstruction.rs1].value & Registers[currentInstruction.rs2].value
    
    if (currentInstruction.name=="FENCE"):
        outputRegisters(programCounter)
        exit(0)
    
    if (currentInstruction.name=="ECALL"):
        outputRegisters(programCounter)
        exit(0)

    if (currentInstruction.name=="EBREAK"):
        outputRegisters(programCounter)
        exit(0)