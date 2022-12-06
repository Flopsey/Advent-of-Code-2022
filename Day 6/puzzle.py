import itertools
import operator


with open('input', 'r') as f:
    data = f.read().strip()

for i in range(3, len(data) - 1):
    if all(map(lambda pair: operator.ne(*pair), itertools.combinations(data[i-3:i+1], 2))):
        print(i + 1)
        break

for i in range(13, len(data) - 1):
    if all(map(lambda pair: operator.ne(*pair), itertools.combinations(data[i-13:i+1], 2))):
        print(i + 1)
        break
