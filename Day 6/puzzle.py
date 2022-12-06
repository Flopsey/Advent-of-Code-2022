from itertools import combinations, starmap
import operator


def find_marker(data: str, marker_length: int) -> int:
    for i in range(marker_length - 1, len(data) - 1):
        if all(starmap(operator.ne, combinations(data[i-(marker_length - 1):i+1], 2))):
            return i + 1


with open('input', 'r') as f:
    data = f.read().strip()

print(find_marker(data, 4))
print(find_marker(data, 14))
