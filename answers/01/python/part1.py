import re

total = 0
with open('../../../inputs/01') as f:
    for line in f:
        first = re.search(r'\d', line)
        last = re.search(r'(\d)\D*$', line)
        if first and last:
            total += int(first.group() + last.group(1))

print(total)
