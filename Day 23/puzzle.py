from collections import Counter
from functools import partial
import itertools


def bounding_box(elves):
    x = list(map(lambda elf: elf[0], elves))
    y = list(map(lambda elf: elf[1], elves))
    return (min(x), min(y)), (max(x), max(y))


def print_elves(elves):
    bounds = bounding_box(elves)
    for y in range(bounds[0][1], bounds[1][1] + 1):
        for x in range(bounds[0][0], bounds[1][0] + 1):
            print('#' if (x, y) in elves else '.', end="")
        print()
    print()


def neighbor(field, direction):
    match direction:
        case 'N':
            return field[0], field[1] - 1
        case 'NE':
            return field[0] + 1, field[1] - 1
        case 'E':
            return field[0] + 1, field[1]
        case 'SE':
            return field[0] + 1, field[1] + 1
        case 'S':
            return field[0], field[1] + 1
        case 'SW':
            return field[0] - 1, field[1] + 1
        case 'W':
            return field[0] - 1, field[1]
        case 'NW':
            return field[0] - 1, field[1] - 1


elves: set[tuple[int, int]] = set()
with open('input', 'r') as f:
    for y, line in enumerate(f):
        for x, field in enumerate(line.strip()):
            if field == '#':
                elves.add((x, y))
# print("== Initial State ==")
# print_elves(elves)

directions = [*"NSWE"]
prev_elves = elves.copy()
for round in itertools.count(1):
    proposals = {}

    for elf in elves:
        proposals[elf] = elf
        if all(field not in elves for field in map(partial(neighbor, elf), ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])):
            continue
        for direction in directions:
            match direction:
                case 'N':
                    if all(field not in elves for field in map(partial(neighbor, elf), ['N', 'NE', 'NW'])):
                        proposals[elf] = (elf[0], elf[1] - 1)
                        break
                case 'S':
                    if all(field not in elves for field in map(partial(neighbor, elf), ['S', 'SE', 'SW'])):
                        proposals[elf] = (elf[0], elf[1] + 1)
                        break
                case 'W':
                    if all(field not in elves for field in map(partial(neighbor, elf), ['W', 'NW', 'SW'])):
                        proposals[elf] = (elf[0] - 1, elf[1])
                        break
                case 'E':
                    if all(field not in elves for field in map(partial(neighbor, elf), ['E', 'NE', 'SE'])):
                        proposals[elf] = (elf[0] + 1, elf[1])
                        break
    proposals_count = Counter(proposals.values())
    for elf in elves.copy():
        if proposals_count[proposals[elf]] == 1:
            elves.remove(elf)
            elves.add(proposals[elf])
    # print(f"== End of round {round} ==")
    # print_elves(elves)

    directions.append(directions.pop(0))

    if round == 10:
        bounds = bounding_box(elves)
        total = (bounds[1][0] + 1 - bounds[0][0]) * (bounds[1][1] + 1 - bounds[0][1])
        print(total - len(elves))

    if elves == prev_elves:
        print(round)
        break
    prev_elves = elves.copy()
