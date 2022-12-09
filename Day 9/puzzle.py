from typing import Iterator


def one_by_one_instructions(instructions):
    for instruction in instructions:
        direction, amount = instruction.split()
        for _ in range(int(amount)):
            yield direction


def sign(a):
    return (a > 0) - (a < 0)


def simulate(instructions: Iterator, n: int) -> int:
    tail_positions = {(0, 0)}
    knots = [(0, 0) for _ in range(n)]
    for direction in instructions:
        match direction:
            case 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])
            case 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            case 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            case 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
        for i in range(1, n):
            diff = (knots[i-1][0] - knots[i][0], knots[i-1][1] - knots[i][1])
            if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                knots[i] = (knots[i][0] + sign(diff[0]), knots[i][1])
                knots[i] = (knots[i][0], knots[i][1] + sign(diff[1]))
        tail_positions.add(knots[-1])
    return len(tail_positions)


with open('input', 'r') as f:
    print(simulate(one_by_one_instructions(f), 2))

with open('input', 'r') as f:
    print(simulate(one_by_one_instructions(f), 10))
