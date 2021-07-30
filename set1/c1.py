
def hex2int(hexStr: str) -> int:
    i = 0
    for c in hexStr:
        i += int(c, 16)
        i = i << 4
    return i >> 4

b64ChrSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
def int2b64(i: int) -> str:
    outStr = list()
    while i:
        outStr.append(b64ChrSet[i % 64])
        i = i >> 6
    return ''.join(reversed(outStr))

def hex2b64(hexStr: str) -> str:
    return int2b64(hex2int(hexStr))
