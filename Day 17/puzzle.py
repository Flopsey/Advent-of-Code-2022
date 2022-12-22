import itertools
from pprint import pprint


rocks = itertools.cycle([
    ['####', '....', '....', '....'],
    ['.#..', '###.', '.#..', '....'],
    ['###.', '..#.', '..#.', '....'],
    ['#...', '#...', '#...', '#...'],
    ['##..', '##..', '....', '....'],
])
with open('input', 'r') as f:
    jets = itertools.cycle(f.read().strip())


def move(grid: set[tuple[int, int]], rock: list[str], coords: tuple[int, int], direction: str) -> tuple[tuple[int, int], bool]:
    match direction:
        case '<':
            translate = lambda x, y: (x - 1, y)
        case '>':
            translate = lambda x, y: (x + 1, y)
        case 'v':
            translate = lambda x, y: (x, y - 1)
    for j in range(4):
        for i in range(4):
            if rock[j][i] != '#':
                continue
            new_pos = translate(coords[0] + i, coords[1] + j)
            if new_pos[1] < 0 or new_pos in grid:
                return coords, True
            if new_pos[0] < 0 or new_pos[0] >= 7:
                return coords, False
    return translate(*coords), False


def print_grid(grid: set[tuple[int, int]], current_rock: list[str] | None = None, coords: tuple[int, int] | None = None) -> None:
    new_grid = {}
    for rock in grid:
        new_grid[rock] = '#'
    if current_rock is not None:
        for j in range(4):
            for i in range(4):
                if current_rock[j][i] == '#':
                    new_grid[coords[0] + i, coords[1] + j] = '@'
    for y in range(max(new_grid.keys(), key=lambda coords: coords[1], default=(0, -1))[1], -1, -1):
        print(f"{y:4d} ", "|", *(new_grid.get((x, y), ".") for x in range(7)), "|", sep="")
    print(" " * 5, "+", "-" * 7, "+", sep="", end="\n\n")



grid: set[tuple[int, int]] = set()
for round, rock in enumerate(itertools.islice(rocks, 2022)):
    top = max(grid, key=lambda coords: coords[1], default=(0, -1))[1]
    x = 2
    y = top + 4
    # print_grid(grid, rock, (x, y))
    while True:
        (x, y), _ = move(grid, rock, (x, y), next(jets))
        # print_grid(grid, rock, (x, y))
        (x, y), stop = move(grid, rock, (x, y), 'v')
        if stop:
            break
        # print_grid(grid, rock, (x, y))
    for j in range(4):
        for i in range(4):
            if rock[j][i] != '#':
                continue
            grid.add((x + i, y + j))
# print_grid(grid)
print(max(grid, key=lambda coords: coords[1], default=(0, -1))[1] + 1)
