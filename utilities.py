def doesLineContainLabel(instruction_line):
    if (instruction_line.find(":") != -1):
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


       