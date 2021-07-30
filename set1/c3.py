from collections import Counter
from functools import reduce

from c2 import hex2int

asciiChrSet = ''.join(chr(n) for n in range(256))
def singleByteXorDecrypt(i: int, key: str) -> str:
    outStr = list()
    kInt = ord(key)
    while i:
        outStr.append(asciiChrSet[(i % 256) ^ kInt])
        i = i >> 8
    return ''.join(reversed(outStr))

letter_frequency = {
    'a':  0.08167,
    'b':  0.01492,
    'c':  0.02782,
    'd':  0.04253,
    'e':  0.1270,
    'f':  0.02228,
    'g':  0.02015,
    'h':  0.06094,
    'i':  0.06966,
    'j':  0.00153,
    'k':  0.00772,
    'l':  0.04025,
    'm':  0.02406,
    'n':  0.06749,
    'o':  0.07507,
    'p':  0.01929,
    'q':  0.00095,
    'r':  0.05987,
    's':  0.06327,
    't':  0.09056,
    'u':  0.02758,
    'v':  0.00978,
    'w':  0.02360,
    'x':  0.00150,
    'y':  0.01974,
    'z':  0.00074,
}

def english_test(data: str) -> float:
    counter = Counter(data.lower())
    ln = len(data)
    return sum(
        (letter_frequency.get(char, 0) * count / ln)**0.5
        for char, count in counter.items()
    )

def find_best(h: str):
    results = list()
    for c in asciiChrSet:
        data = singleByteXorDecrypt(hex2int(h), c)
        results.append((data, c, english_test(data)))

    return reduce(lambda x, y: max(x, y, key=lambda d: d[2]), results)
