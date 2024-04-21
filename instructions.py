class instructions:
    def _init_(self, name, opcode, funct3, funct7=None, type=None):
        self.name = name
        self.opcode = opcode
        self.funct3 = funct3
        self.funct7 = funct7
        self.type = type

Instructions = {
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
    "AND": instructions("AND", 0b0110011, 0b111, 0b0000000, type="R")
}

"""
def decodeInstruction(instructiona):
    instructionList=instructiona.strip().replace(" ","").upper().split(",")
    instructionName=instructionList[0]
    try:
        instructionObject=instructions[instructionName]
    except KeyError:
        print("Instruction '{instructionName}' not found")
        return None
    
    if instructionObject.type=="R":
"""

        
        