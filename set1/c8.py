from c6 import group

for line in open('8.txt'):
    blocks = [int(''.join(block), 16) for block in group(line.strip(), 32)]
    if len(blocks) != len(set(blocks)):
        print(line.strip())
