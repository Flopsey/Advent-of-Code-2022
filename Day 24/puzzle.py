from collections import defaultdict, deque
from typing import Callable


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


blizzard_coords: list[tuple[int, int]] = []
blizzard_directions: list[str] = []
with open('input', 'r') as f:
    puzzle_input = f.readlines()
for y, line in enumerate(puzzle_input[1:-1]):
    line = line.strip()[1:-1]
    for x, field in enumerate(line):
        if field == '.':
            continue
        blizzard_coords.append((x, y))
        blizzard_directions.append(field)
start = (puzzle_input[0][1:-1].index('.'), -1)
end = (puzzle_input[-1][1:-1].index('.'), len(puzzle_input) - 2)
width = len(puzzle_input[0].strip()[1:-1])
height = len(puzzle_input[1:-1])


def print_blizzards(blizzards):
    blizzards = dict(blizzards)
    print("#" + "#" * start[0] + "." + "#" * (width - start[0] - 1) + "#")
    for y in range(height):
        print("#", end="")
        for x in range(width):
            print(blizzards.get((x, y), "."), end="")
        print("#")
    print("#" + "#" * end[0] + "." + "#" * (width - end[0] - 1) + "#", end="\n\n")


def simulate_blizzards(coords, directions) -> list[tuple[int, int]]:
    new_blizzards = []
    for (x, y), direction in zip(coords, directions):
        match direction:
            case '^':
                y = (y - 1) % height
            case 'v':
                y = (y + 1) % height
            case '<':
                x = (x - 1) % width
            case '>':
                x = (x + 1) % width
        new_blizzards.append((x, y))
    # print_blizzards(zip(new_blizzards, directions))
    return new_blizzards


max_t = lcm(width, height)

levels = [blizzard_coords.copy()]
for _ in range(1, max_t):
    blizzard_coords = simulate_blizzards(blizzard_coords, blizzard_directions)
    levels.append(blizzard_coords.copy())


def bfs():
    visited = set()
    queue = deque([(0, start, 0)])
    
    while len(queue) != 0:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node[1] == end:
            return node[2]
        x, y = node[1]
        for nX, nY in [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (nX < 0 or nX >= width or nY < 0 or nY >= height) and not (nX, nY) in (start, end):
                continue
            if (nX, nY) in levels[node[0]]:
                continue
            queue.append(((node[0] + 1) % max_t, (nX, nY), node[2] + 1))


print(bfs() - 1)


# graph: defaultdict[tuple[int, tuple[int, int]], set[tuple[int, tuple[int, int]]], Callable[[],set[tuple[int,tuple[int,int]]]]] = defaultdict(set)
# max_t = lcm(width, height)


# def bfs():
#     visited = set()
#     queue = deque([(0, start)])
#     predecessor = {}

#     def backtrace(node):
#         path = [node]
#         while node in set(predecessor.keys()):
#             node = predecessor[node]
#             path.insert(0, node)
#         return path
    
#     while len(queue) != 0:
#         node = queue.popleft()
#         if node in visited:
#             continue
#         visited.add(node)
#         if node[1] == end:
#             return backtrace(node)
#         for neighbor in graph[node]:
#             if neighbor in visited:
#                 continue
#             predecessor[neighbor] = node
#             queue.append(neighbor)


# for t in range(18):
#     print(f"t={t+1}")
#     # print(blizzard_coords)
#     new_blizzard_coords = simulate_blizzards(zip(blizzard_coords, blizzard_directions))
#     for x in range(0, height):
#         for y in range(0, width):
#             if (x, y) in blizzard_coords:
#                 continue
#             for neighbor in [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#                 if neighbor[0] < 0 or neighbor[0] >= width or neighbor[1] < 0 or neighbor[1] >= height:
#                     continue
#                 if neighbor in new_blizzard_coords:
#                     continue
#                 graph[(t, (x, y))].add(((t + 1) % max_t, neighbor))
#     blizzard_coords = new_blizzard_coords
# graph[(0, start)].add((1, (start[0], start[1] + 1)))
# for t in range(max_t):
#     graph[(t, (end[0], end[1] - 1))].add(((t + 1) % max_t, end))

# print(len(graph))
# path = bfs()
# print(path)
# print(len(path[1:]))
