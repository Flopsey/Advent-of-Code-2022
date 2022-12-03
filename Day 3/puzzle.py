from functools import reduce
from itertools import chain


sum_of_priorites = 0
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        mid = int(len(line) / 2)
        first = line[:mid]
        second = line[mid:]
        item = (set(first) & set(second)).pop()
        if (item.islower()):
            priority = ord(item) - ord('a') + 1
        else:
            priority = ord(item) - ord('A') + 27
        sum_of_priorites += priority
print(sum_of_priorites)

sum_of_priorites = 0
with open('input', 'r') as f:
    for group in zip(*([iter(f)] * 3), strict=True):
        group = list(map(set, map(str.strip, group)))
        item = group[0].intersection(*group[1:]).pop()
        if (item.islower()):
            priority = ord(item) - ord('a') + 1
        else:
            priority = ord(item) - ord('A') + 27
        sum_of_priorites += priority
print(sum_of_priorites)
