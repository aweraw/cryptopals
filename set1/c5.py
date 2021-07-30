from itertools import cycle

def repeating_key_xor(data, key):
    rKey = cycle(ord(c) for c in key)
    iData = (ord(c) for c in data)
    encData = 0
    for d, k in zip(iData, rKey):
        encData = encData << 8
        encData += d ^ k
    return hex(encData)
