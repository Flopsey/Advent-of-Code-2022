import functools
import itertools
import json


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return itertools.zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


@functools.total_ordering
class Packet:
    def __init__(self, packet) -> None:
        self.packet = packet
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Packet):
            return False
        return self.packet == __o.packet
    
    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, Packet):
            return NotImplemented
        if isinstance(self.packet, int) and isinstance(__o.packet, int):
            if self.packet < __o.packet:
                return True
            elif __o.packet < self.packet:
                return False
            else:
                return None
        elif isinstance(self.packet, list) and isinstance(__o.packet, list):
            for c, d in zip(self.packet, __o.packet):
                cmp = Packet(c) < Packet(d)
                if cmp is not None:
                    return cmp
            if len(self.packet) < len(__o.packet):
                return True
            elif len(self.packet) > len(__o.packet):
                return False
            else:
                return None
        elif isinstance(self.packet, int):
            return Packet([self.packet]) < Packet(__o.packet)
        elif isinstance(__o.packet, int):
            return Packet(self.packet) < Packet([__o.packet])
        else:
            raise ValueError


output = 0
with open('input', 'r') as f:
    for i, (a, b) in enumerate(grouper(map(lambda data: Packet(data), map(json.loads, filter(lambda line: line.strip(), f))), 2, incomplete='strict'), 1):
        if a < b:
            output += i
print(output)

with open('input', 'r') as f:
    packets = list(map(lambda data: Packet(data), map(json.loads, filter(lambda line: line.strip(), f))))
    divider1 = Packet([[2]])
    divider2 = Packet([[6]])
    packets += [divider1, divider2]
    packets.sort()
    idx1 = packets.index(divider1) + 1
    idx2 = packets.index(divider2) + 1
    print(idx1 * idx2)
