def doesLineContainLabel(instruction_line):
    if (instruction_line.find(":") != -1):
        return True
    else:
        return False