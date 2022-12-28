from collections import deque


def bfs(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    visited = set()
    queue = deque([start])
    distance = {start: 0}

    while len(queue) != 0:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return distance[node]
        x, y = node
        for nX, nY in ((x - 1, y),
                         (x + 1, y),
                         (x, y - 1),
                         (x, y + 1)):
            if nX not in range(len(grid)) or nY not in range(len(grid[0])):
                continue
            if grid[nX][nY] - grid[x][y] > 1:
                continue
            distance[(nX, nY)] = distance[node] + 1
            queue.append((nX, nY))


grid = []
possible_starts = set()
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
            if char in ('S', 'a'):
                possible_starts.add((i, j))
            row.append(ord(char) - ord('a'))
        grid.append(row)

print(bfs(grid, start, end))

print(min(filter(bool, (bfs(grid, start, end) for start in possible_starts))))
