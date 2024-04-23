import registers

class instructions:
    def __init__(self, name, opcode, funct3, rd=None, rs1=None, rs2=None, funct7=None, immediate=None, type=None, label=None, isLabel=False, commas=-1):
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
        self.commas = commas

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


def decodeInstruction(instruction_line): # This function will help taking each line in the input file to extract the rd, rs1 and rs2
    decodedInstructionObject=[]
    instructionList=instruction_line.strip().replace(" ","").upper().split(",")
    instructionName=instructionList[0]
    try:
        instructionObject=Instructions[instructionName]
    except KeyError:
        print(f"Instruction '{instructionName}' not found")
        return None
    
    if instructionObject.type=="R": # For example, 'ADD rd, rs1, rs2' which is R-Type
        decodedInstructionObject.clear()
        decodedInstructionObject[0]=instructionObject.name # This will be the name of the instruction
        decodedInstructionObject[1]=instructionList[1] # This will be the rd (destination register)
        decodedInstructionObject[2]=instructionList[2] # This will be the rs1 (source register 1)
        decodedInstructionObject[3]=instructionList[3] # This will be the rs2 (source register 2)
        return decodedInstructionObject
    
    elif instructionObject.type=="I": # For example, 'ADDI rd, rs1, imm' which is I-Type
        decodedInstructionObject.clear()
        decodedInstructionObject[0]=instructionObject.name
        decodedInstructionObject[1]=instructionList[1] # This will be the rd
        decodedInstructionObject[2]=instructionList[2] # This will be the rs1
        decodedInstructionObject[3]=instructionList[3] # This will be the immediate value
        return decodedInstructionObject
    
    elif instructionObject.type=="S": # For example, 'SB rs1, imm(rs2)' which is S-Type
        decodedInstructionObject.clear()
        decodedInstructionObject[0]=instructionObject.name # This will be the name of the instruction
        decodedInstructionObject[1]=instructionList[1] # This will be the rs1
        decodedInstructionObject[2]=instructionList[2] # This will be the immediate value
        return decodedInstructionObject
    
    elif instructionObject.type=="B": # For example, 'BEQ rs1, rs2, imm' which is B-Type
        decodedInstructionObject.clear()
        decodedInstructionObject[0]=instructionObject.name # This will be the name of the instruction
        decodedInstructionObject[1]=instructionList[1] # This will be the rs1
        decodedInstructionObject[2]=instructionList[2] # This will be the rs2
        decodedInstructionObject[3]=instructionList[3] # This will be the immediate value
        return decodedInstructionObject

    elif instructionObject.type=="U": # For example, 'LUI rd, imm' which is U-Type
        decodedInstructionObject.clear()
        decodedInstructionObject[0]=instructionObject.name # This will be the name of the instruction
        decodedInstructionObject[1]=instructionList[1] # This will be the rd
        decodedInstructionObject[2]=instructionList[2] # This will be the immediate value
        return decodedInstructionObject
    
    elif instructionObject.type=="J": # For example, 'JAL rd, imm' which is J-Type
        decodedInstructionObject.clear()
        decodedInstructionObject[0]=instructionObject.name # This will be the name of the instruction
        decodedInstructionObject[1]=instructionList[1] # This will be the rd
        decodedInstructionObject[2]=instructionList[2] # This will be the immediate value
        return decodedInstructionObject
    
    else:
        print(f"Instruction '{instructionName}' not found")
        return None
    

def executeInstruction(instruction_line, programCounter, Labels):
    decodedInstructionObject = decodeInstruction(instruction_line)

    if (decodedInstructionObject[0]=="LUI"):
        if (decodedInstructionObject[1] == 0):
            return
        else:
            registers.Registers[decodedInstructionObject[1]] = decodedInstructionObject[2] << 12

    if (decodedInstructionObject[0]=="AUIPC"):
        if (decodedInstructionObject[1] == 0):
            return
        else:
            registers.Registers[decodedInstructionObject[1]] = (registers.Registers[decodedInstructionObject[2]] << 12) + programCounter

    if (decodedInstructionObject[0]=="JAL"):
        if (decodedInstructionObject[1] == 0):
            registers.Registers[decodedInstructionObject[1]] = 0
        else:
            registers.Registers[decodedInstructionObject[1]] = programCounter + 4
            programCounter += decodedInstructionObject[2]
    
    if (decodedInstructionObject[0]=="JALR"):
        if (decodedInstructionObject[1] == 0):
            registers.Registers[decodedInstructionObject[1]] = 0
        else:
            registers.Registers[decodedInstructionObject[1]] = decodedInstructionObject[3] + registers.Registers[decodedInstructionObject[2]]
    programCounter = decodedInstructionObject[3] + registers.Registers[decodedInstructionObject[2]] - 4

    #if (decodedInstructionObject[0]=="BEQ"):

    #if (decodedInstructionObject[0]=="BNE"):

    #if (decodedInstructionObject[0]=="BLT"):

    #if (decodedInstructionObject[0]=="BGE"):

    #if (decodedInstructionObject[0]=="BLTU"):

    #if (decodedInstructionObject[0]=="BGEU"):

    """if (decodedInstructionObject[0]=="LB"):
        if (decodedInstructionObject[1] == 0):
            return
        elif (decodedInstructionObject[2] == 2):"""
    
    if (decodedInstructionObject[0]=="LH"):
        if (decodedInstructionObject[1] == 0):
            return
        else:
            registers.Registers[decodedInstructionObject[1]] = registers.Registers[decodedInstructionObject[2]] + decodedInstructionObject[3]
            