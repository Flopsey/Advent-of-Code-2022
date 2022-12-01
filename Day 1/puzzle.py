def total_per_elf(lines):
    sum = 0
    for line in lines:
        line = line.strip()
        if line == "":
            yield sum
            sum = 0
        else:
            sum += int(line)


with open('input', 'r') as f:
    sums = list(total_per_elf(f))

sums.sort(reverse=True)
print(sums[0])
print(sum(sums[0:3]))
