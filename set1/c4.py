from functools import reduce

from c3 import find_best

results = list()
for line in open('4.txt').read().split('\n'):
    results.append(find_best(line))

best = reduce(lambda x, y: max(x, y, key=lambda d: d[2]), results)
print(best)
