from c1 import hex2int

def hexXor(hex1: str, hex2: str) -> int:
    return hex2int(hex1) ^ hex2int(hex2)

hexChrSet = '0123456789abcdef'
def int2hex(i: int) -> str:
    outStr = list()
    while i:
        outStr.append(hexChrSet[i % 16])
        i = i >> 4
    return ''.join(reversed(outStr))

def fixedXor(hex1: str, hex2: str) -> str:
    return int2hex(hexXor(hex1, hex2))
