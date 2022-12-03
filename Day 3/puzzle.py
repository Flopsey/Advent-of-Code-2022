def priority(item):
    if (item.islower()):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


sum_of_priorites = 0
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        mid = int(len(line) / 2)
        item = (set(line[:mid]) & set(line[mid:])).pop()
        sum_of_priorites += priority(item)
print(sum_of_priorites)

sum_of_priorites = 0
with open('input', 'r') as f:
    for group in zip(*([iter(f)] * 3)):
        group = list(map(set, map(str.strip, group)))
        item = group[0].intersection(*group[1:]).pop()
        sum_of_priorites += priority(item)
print(sum_of_priorites)
