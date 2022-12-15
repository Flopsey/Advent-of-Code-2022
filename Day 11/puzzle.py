from collections import Counter
import re
from typing import Callable


class Monkey:
    monkeys: dict[int, 'Monkey'] = {}

    def __init__(self, match: re.Match) -> None:
        self.id = int(match.group('id'))
        self.items = list(map(int, match.group('items').split(',')))
        self.operation = lambda old: eval(match.group('operation'), None, {'old': old})
        self.test = lambda worry_level: worry_level % int(match.group('test')) == 0
        self.destination = lambda condition: Monkey.monkeys[int(match.group('true' if condition else 'false'))]
        self.monkeys[self.id] = self
    
    def inspect_and_throw(self) -> int:
        print(f"Monkey {self.id}:")
        inspections = 0
        while len(self.items) != 0:
            inspections += 1
            print(f"  Monkey inspects an item with a worry level of {self.items[0]}.")
            item = self.items.pop(0)
            print(f"    Worry level is updated with {self.operation} to {self.operation(item)}.")
            item = self.operation(item)
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item // 3}")
            item = item // 3
            print(f"    Test {self.test} for current worry level yields {self.test(item)}")
            condition = self.test(item)
            print(f"    Item with worry level {item} is thrown to monkey {self.destination(condition).id}")
            self.destination(condition).catch(item)
        return inspections

    def catch(self, item: int):
        self.items.append(item)


pattern = re.compile(
    r'Monkey (?P<id>\d+):\s*' \
    r'Starting items:(?: (?P<items>(?:\d+, )*\d+))\s*' \
    r'Operation: new = (?P<operation>\w+ . \w+)\s*' \
    r'Test: divisible by (?P<test>\d+)\s*' \
    r'If true: throw to monkey (?P<true>\d+)\s*' \
    r'If false: throw to monkey (?P<false>\d+)',
    re.MULTILINE)
inspection_count = {}
with open('input', 'r') as f:
    for match in re.finditer(pattern, f.read()):
        monkey = Monkey(match)
        inspection_count[monkey.id] = 0
for round in range(20):
    for monkey in Monkey.monkeys.values():
        inspection_count[monkey.id] += monkey.inspect_and_throw()
m1, m2 = sorted(inspection_count.values(), reverse=True)[:2]
print(m1 * m2)
