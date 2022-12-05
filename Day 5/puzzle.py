import copy
import re


MOVE_PATTERN = re.compile(r'move (\d+) from (\d+) to (\d+)')

stacks1: list[list[str]] = []
with open('sample_input', 'r') as f:
    for line in f:
        if line.strip() == "":
            break
        if line[1].isdigit():
            continue
        crates = line[1::4]
        for i, crate in enumerate(crates):
            if i > len(stacks1) - 1:
                stacks1.append([])
            if crate.isalpha():
                stacks1[i].insert(0, crate)
    stacks2 = copy.deepcopy(stacks1)
    for line in f:
        n, origin, destination = map(int, re.match(MOVE_PATTERN, line).groups())
        for _ in range(n):
            crate = stacks1[origin - 1].pop()
            stacks1[destination - 1].append(crate)
        crates = stacks2[origin - 1][-n:]
        del stacks2[origin - 1][-n:]
        stacks2[destination - 1].extend(crates)
print(*(stack[-1] for stack in stacks1), sep='')
print(*(stack[-1] for stack in stacks2), sep='')
