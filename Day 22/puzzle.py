import re


def print_grid(grid):
    for y in range(1, max(list(zip(*grid.keys()))[1]) + 1):
        for x in range(1, max(list(zip(*grid.keys()))[0]) + 1):
            print(grid.get((x, y), " "), end="")
        print()
    print()


grid: dict[tuple[int, int], str] = {}
with open('input', 'r') as f:
    for y, row in enumerate(f, 1):
        if row.strip('\n') == "":
            break
        for x, field in enumerate(row.strip('\n'), 1):
            if field == " ":
                continue
            grid[(x, y)] = field
    instructions = f.readline()

pattern = re.compile(r'(\d+)|([RL])')
x, y = min(map(lambda coords: coords[0], filter(lambda coords: coords[1] == 1, grid.keys()))), 1
facing = 0
for instruction in map(lambda match: match[0], re.finditer(pattern, instructions)):
    row = list(map(lambda coords: coords[0], filter(lambda coords: coords[1] == y, grid.keys())))
    col = list(map(lambda coords: coords[1], filter(lambda coords: coords[0] == x, grid.keys())))
    leftmost = min(row)
    rightmost = max(row)
    topmost = min(col)
    bottommost = max(col)

    def wrap_x(value):
        return leftmost + ((value - leftmost) % (rightmost - leftmost + 1))
    
    def wrap_y(value):
        return topmost + ((value - topmost) % (bottommost - topmost + 1))
    
    match instruction:
        case 'L':
            facing = (facing - 1) % 4
        case 'R':
            facing = (facing + 1) % 4
        case steps:
            for _ in range(int(steps)):
                grid[(x, y)] = ['>', 'v', '<', '^'][facing]
                match facing:
                    case 0:  # right
                        new_x = wrap_x(x + 1)
                        if grid.get((new_x, y), ' ') not in ('.', '<', '>', '^', 'v'):
                            break
                        x = new_x
                    case 1:  # down
                        new_y = wrap_y(y + 1)
                        if grid.get((x, new_y), ' ') not in ('.', '<', '>', '^', 'v'):
                            break
                        y = new_y
                    case 2:  # left
                        new_x = wrap_x(x - 1)
                        if grid.get((new_x, y), ' ') not in ('.', '<', '>', '^', 'v'):
                            break
                        x = new_x
                    case 3:  # up
                        new_y = wrap_y(y - 1)
                        if grid.get((x, new_y), ' ') not in ('.', '<', '>', '^', 'v'):
                            break
                        y = new_y
    # print_grid(grid)
# print(f"{x=}, {y=}, {facing=}")
print(1000 * y + 4 * x + facing)
