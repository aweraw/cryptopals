from itertools import takewhile, cycle
from functools import reduce
from itertools import combinations
from base64 import decodebytes
from typing import Callable

from c3 import asciiChrSet, singleByteXorDecrypt, english_test

def concatBytes(seq: iter, mapF: Callable = lambda x: x) -> int:
    return reduce(lambda x, y: (x << 8) + mapF(y), seq, 0)

def str2int(s: str) -> int:
    return concatBytes(s, ord)

def wegnerCount(i: int, acc: int=0) -> int:
    if i == 0: return acc
    return wegnerCount(i & (i - 1), acc + 1)

def binHammingDistance(int1: int, int2: int) -> int:
    return wegnerCount(int1 ^ int2)

def group(it: iter, n: int) -> zip:
    return zip(*[iter(it)]*n)

def take(n: int, seq: iter) -> tuple:
    c = (True for _ in range(n))
    return tuple(takewhile(lambda x: next(c), seq))

def sample_blocks(data: bytes, block_len: int):
    for bs in take(4, group(data, block_len)):
        yield concatBytes(bs)

data = decodebytes(open('6.txt', 'rb').read())

key_size = min(
    (sum(binHammingDistance(i, j) / ks for i, j in combinations(sample_blocks(data, ks), 2)) / 6, ks)
    for ks in range(2, 41)
)[1]

print(f"key size: {key_size}")

key = list()
for transposed_block in zip(*group(data, key_size)):
    results = list()
    for c in asciiChrSet:
        dt = singleByteXorDecrypt(concatBytes(transposed_block), c)
        results.append((data, c, english_test(dt)))
    key.append(reduce(lambda x, y: max(x, y, key=lambda d: d[2]), results)[1])

print(f"key string: {''.join(key)}")

result = ''.join(chr(d ^ k) for d, k in zip(data, cycle(ord(c) for c in key)))

print("decrypted text:\n")
print(result.replace('\x00', ' '))
