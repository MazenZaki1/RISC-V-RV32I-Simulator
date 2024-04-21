class riscInstructions:
    def _init_(self, name, opcode, funct3, funct7=None, type=None):
        self.name = name
        self.opcode = opcode
        self.funct3 = funct3
        self.funct7 = funct7
        self.type = type

instructions = {
    "LUI": riscInstructions("LUI", 0b0110111, None, type="U"),
    "AUIPC": riscInstructions("AUIPC", 0b0010111, None, type="U"),
    "JAL": riscInstructions("JAL", 0b1101111, None, type="J"),
    "JALR": riscInstructions("JALR", 0b1100111, 0b000, type="I"),
    "BEQ": riscInstructions("BEQ", 0b1100011, 0b000, type="B"),
    "BNE": riscInstructions("BNE", 0b1100011, 0b001, type="B"),
    "BLT": riscInstructions("BLT", 0b1100011, 0b100, type="B"),
    "BGE": riscInstructions("BGE", 0b1100011, 0b101, type="B"),
    "BLTU": riscInstructions("BLTU", 0b1100011, 0b110, type="B"),
    "BGEU": riscInstructions("BGEU", 0b1100011, 0b111, type="B"),
    "LB": riscInstructions("LB", 0b0000011, 0b000, type="I"),
    "LH": riscInstructions("LH", 0b0000011, 0b001, type="I"),
    "LW": riscInstructions("LW", 0b0000011, 0b010, type="I"),
    "LBU": riscInstructions("LBU", 0b0000011, 0b100, type="I"),
    "LHU": riscInstructions("LHU", 0b0000011, 0b101, type="I"),
    "SB": riscInstructions("SB", 0b0100011, 0b000, type="S"),
    "SH": riscInstructions("SH", 0b0100011, 0b001, type="S"),
    "SW": riscInstructions("SW", 0b0100011, 0b010, type="S"),
    "ADDI": riscInstructions("ADDI", 0b0010011, 0b000, type="I"),
    "SLTI": riscInstructions("SLTI", 0b0010011, 0b010, type="I"),
    "SLTIU": riscInstructions("SLTIU", 0b0010011, 0b011, type="I"),
    "XORI": riscInstructions("XORI", 0b0010011, 0b100, type="I"),
    "ORI": riscInstructions("ORI", 0b0010011, 0b110, type="I"),
    "ANDI": riscInstructions("ANDI", 0b0010011, 0b111, type="I"),
    "SLLI": riscInstructions("SLLI", 0b0010011, 0b001, 0b0000000, type="R"),
    "SRLI": riscInstructions("SRLI", 0b0010011, 0b101, 0b0000000, type="R"),
    "SRAI": riscInstructions("SRAI", 0b0010011, 0b101, 0b0100000, type="R"),
    "ADD": riscInstructions("ADD", 0b0110011, 0b000, 0b0000000, type="R"),
    "SUB": riscInstructions("SUB", 0b0110011, 0b000, 0b0100000, type="R"),
    "SLL": riscInstructions("SLL", 0b0110011, 0b001, 0b0000000, type="R"),
    "SLT": riscInstructions("SLT", 0b0110011, 0b010, 0b0000000, type="R"),
    "SLTU": riscInstructions("SLTU", 0b0110011, 0b011, 0b0000000, type="R"),
    "XOR": riscInstructions("XOR", 0b0110011, 0b100, 0b0000000, type="R"),
    "SRL": riscInstructions("SRL", 0b0110011, 0b101, 0b0000000, type="R"),
    "SRA": riscInstructions("SRA", 0b0110011, 0b101, 0b0100000, type="R"),
    "OR": riscInstructions("OR", 0b0110011, 0b110, 0b0000000, type="R"),
    "AND": riscInstructions("AND", 0b0110011, 0b111, 0b0000000, type="R")
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

        
        