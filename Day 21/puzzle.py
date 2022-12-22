import functools
import operator
from typing import Callable


monkeys: dict[str, int | tuple[str, Callable[[int, int], int], str]] = {}
with open('input', 'r') as f:
    for line in f:
        monkey, job = line.split(':')
        match job.split():
            case [a, '+', b]:
                monkeys[monkey] = a, operator.add, b
            case [a, '-', b]:
                monkeys[monkey] = a, operator.sub, b
            case [a, '*', b]:
                monkeys[monkey] = a, operator.mul, b
            case [a, '/', b]:
                monkeys[monkey] = a, operator.floordiv, b
            case [c]:
                monkeys[monkey] = int(c)

@functools.cache
def do_job(monkey: str) -> int:
    if isinstance(c := monkeys[monkey], int):
        return c
    else:
        a, op, b = monkeys[monkey]
        return op(do_job(a), do_job(b))

print(do_job('root'))
            