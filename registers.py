class registers:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

Registers = {
    "x0": registers("x0"),
    "x1": registers("x1"),
    "x2": registers("x2", 12000),
    "x3": registers("x3"),
    "x4": registers("x4"),
    "x5": registers("x5"),
    "x6": registers("x6"),
    "x7": registers("x7"),
    "x8": registers("x8"),
    "x9": registers("x9"),
    "x10": registers("x10"),
    "x11": registers("x11"),
    "x12": registers("x12"),
    "x13": registers("x13"),
    "x14": registers("x14"),
    "x15": registers("x15"),
    "x16": registers("x16"),
    "x17": registers("x17"),
    "x18": registers("x18"),
    "x19": registers("x19"),
    "x20": registers("x20"),
    "x21": registers("x21"),
    "x22": registers("x22"),
    "x23": registers("x23"),
    "x24": registers("x24"),
    "x25": registers("x25"),
    "x26": registers("x26"),
    "x27": registers("x27"),
    "x28": registers("x28"),
    "x29": registers("x29"),
    "x30": registers("x30"),
    "x31": registers("x31"),
}