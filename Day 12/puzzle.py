from collections import defaultdict, deque
import functools
import math
from pprint import pprint


# https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
def a_star(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    def h(node):
        return float(math.sqrt(pow(end[0] - node[0], 2) + pow(end[1] - node[1], 2)))
    
    open_set = {start}
    came_from = {}

    def backtrace(current):
        path = [current]
        while current in came_from.keys():
            current = came_from[current]
            path.insert(0, current)
        return path

    infinity_factory = functools.partial(float, 'inf')
    g_score = defaultdict(infinity_factory, {start: 0.0})
    f_score = defaultdict(infinity_factory, {start: h(start)})

    while len(open_set) != 0:
        current = sorted(open_set, key=lambda entry: f_score[entry[0]])[0]
        if current == end:
            return backtrace(current)
        open_set.remove(current)
        for neighbor in ((current[0] - 1, current[1]),
                         (current[0] + 1, current[1]),
                         (current[0], current[1] - 1),
                         (current[0], current[1] + 1)):
            if neighbor[0] not in range(len(grid)) or neighbor[1] not in range(len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]] - grid[current[0]][current[1]] > 1:
                continue
            tentative_g_score = g_score[current] + 1.0
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)

def bfs(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    visited = set()
    queue = deque((start,))
    predecessor = {}

    def backtrace(node):
        path = [node]
        while node in predecessor.keys():
            node = predecessor[node]
            path.insert(0, node)
        return path

    while len(queue) != 0:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return backtrace(node)
        for neighbor in ((node[0] - 1, node[1]),
                         (node[0] + 1, node[1]),
                         (node[0], node[1] - 1),
                         (node[0], node[1] + 1)):
            if neighbor[0] not in range(len(grid)) or neighbor[1] not in range(len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]] - grid[node[0]][node[1]] > 1:
                continue
            if neighbor in visited:
                continue
            predecessor[neighbor] = node
            queue.append(neighbor)


grid = []
with open('input', 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        row = []
        for j, char in enumerate(line):
            if char == 'S':
                start = (i, j)
                char = 'a'
            if char == 'E':
                end = (i, j)
                char = 'z'
            row.append(ord(char) - ord('a'))
        grid.append(row)
path = bfs(grid, start, end)
symbols = {}
for i in range(1, len(path) - 1):
    match path[i+1][0] - path[i][0], path[i+1][1] - path[i][1]:
        case -1, 0:
            symbols[path[i]] = '^'
        case 1, 0:
            symbols[path[i]] = 'v'
        case 0, -1:
            symbols[path[i]] = '<'
        case 0, 1:
            symbols[path[i]] = '>'
        case _:
            raise ValueError
for i in range(len(grid)):
    for j in range(len(grid[i])):
        symbol = symbols.get((i, j), '.')
        if (i, j) == start:
            symbol = 'S'
        elif (i, j) == end:
            symbol = 'E'
        print(symbol, end='')
    print()
print(len(path) - 1)
