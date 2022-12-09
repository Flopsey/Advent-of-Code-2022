def one_by_one_instructions(instructions):
    for instruction in instructions:
        direction, amount = instruction.split()
        for _ in range(int(amount)):
            yield direction


def sign(a):
    return (a > 0) - (a < 0)


with open('input', 'r') as f:
    instructions = one_by_one_instructions(f)
    head = (0, 0)
    tail = (0, 0)
    tail_positions = {(0, 0)}
    for direction in instructions:
        match direction:
            case 'L':
                head = (head[0] - 1, head[1])
            case 'R':
                head = (head[0] + 1, head[1])
            case 'D':
                head = (head[0], head[1] - 1)
            case 'U':
                head = (head[0], head[1] + 1)
        diff = (head[0] - tail[0], head[1] - tail[1])
        if abs(diff[0]) > 1 or abs(diff[1]) > 1:
            tail = (tail[0] + sign(diff[0]), tail[1])
            tail = (tail[0], tail[1] + sign(diff[1]))
        tail_positions.add(tail)

print(len(tail_positions))
