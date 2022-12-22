original_file: list[int] = []
file1: list[tuple[int, int]] = []
file2: list[tuple[int, int]] = []
with open('sample_input', 'r') as f:
    for i, line in enumerate(f):
        line = int(line)
        original_file.append(line)
        file1.append((i, line))
        file2.append((i, line * 811589153))

def mix(file, original_file):
    for i, n in enumerate(original_file):
        idx = file1.index((i, n))
        el = file1.pop(idx)
        idx = (idx + el[1]) % len(file1)
        if idx == 0:
            idx = len(file1)
        file1.insert(idx, el)
        # print(list(map(lambda el: el[1], file)))

mix(file1, original_file)
val0 = file1.index((original_file.index(0), 0))
print(file1[(val0 + 1000) % len(file1)][1] + file1[(val0 + 2000) % len(file1)][1] + file1[(val0 + 3000) % len(file1)][1])
