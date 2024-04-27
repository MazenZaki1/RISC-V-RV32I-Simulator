from registers import Registers

def doesLineContainLabel(instruction_line):
    if (instruction_line.find(":")):
        return True
    else:
        return False
    
def binaryToDecimal(binary):
    decimal = 0
    power = 1
    while binary>0:
        rem = binary%10
        binary = binary//10
        decimal += rem*power
        power = power*2

    return decimal

def readStartingAddress(fileName):
    file = open(fileName, 'r')
    startingAddress = file.readline()
    startingAddress = startingAddress.replace(" ", "")
    startingAddress = startingAddress[16:]
    return startingAddress

def outputRegisters(programCounter):
    print("Program has finished running. Here are the final register values:")
    print(f"Program Counter: {programCounter}")
    print("Name   Decimal Value     Binary Value      Hex Value")
    for register in Registers:
        print(f"{Registers[register].name}            {Registers[register].value}              {bin(Registers[register].value)}              {hex(Registers[register].value)}")