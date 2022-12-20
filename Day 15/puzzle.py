from collections import defaultdict
import re


exclusion_zone: defaultdict[int, set[int]] = defaultdict(set)
pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
with open('input', 'r') as f:
    for line in f:
        match = re.match(pattern, line)
        sensor = (int(match.group(1)), int(match.group(2)))
        beacon = (int(match.group(3)), int(match.group(4)))
        distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        for y in range(sensor[1] - distance, sensor[1] + distance + 1):
            if y != 2000000:
                continue
            width = distance - abs(sensor[1] - y)
            exclusion_zone[y].update(range(sensor[0] - width, sensor[0] + width + 1))
        exclusion_zone[beacon[1]].discard(beacon[0])
# print(sorted(exclusion_zone[2000000]))
print(len(exclusion_zone[2000000]))
