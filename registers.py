class registers:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

Registers = {
    "0": registers("x0"),
    "1": registers("x1"),
    "2": registers("x2", 1),
    "3": registers("x3"),
    "4": registers("x4"),
    "5": registers("x5"),
    "6": registers("x6"),
    "7": registers("x7"),
    "8": registers("x8"),
    "9": registers("x9"),
    "10": registers("x10"),
    "11": registers("x11"),
    "12": registers("x12"),
    "13": registers("x13"),
    "14": registers("x14"),
    "15": registers("x15"),
    "16": registers("x16"),
    "17": registers("x17"),
    "18": registers("x18"),
    "19": registers("x19"),
    "20": registers("x20"),
    "21": registers("x21"),
    "22": registers("x22"),
    "23": registers("x23"),
    "24": registers("x24"),
    "25": registers("x25"),
    "26": registers("x26"),
    "27": registers("x27"),
    "28": registers("x28"),
    "29": registers("x29"),
    "30": registers("x30"),
    "31": registers("x31")
}

def getRegisterInfo(register):
    if register in Registers:
        return f"{Registers[register].name}, {Registers[register].value}"
    else:
        return "Register not defined"