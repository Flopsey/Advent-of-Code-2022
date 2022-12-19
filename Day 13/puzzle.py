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


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif b < a:
            return False
        else:
            return None
    elif isinstance(a, list) and isinstance(b, list):
        for c, d in zip(a, b):
            cmp = compare(c, d)
            if cmp is not None:
                return cmp
        if len(a) < len(b):
            return True
        elif len(a) > len(b):
            return False
        else:
            return None
    elif isinstance(a, int):
        return compare([a], b)
    elif isinstance(b, int):
        return compare(a, [b])
    else:
        raise ValueError


output = 0
with open('input', 'r') as f:
    for i, (a, b) in enumerate(grouper(map(json.loads, filter(lambda line: line.strip(), f)), 2, incomplete='strict'), 1):
        if compare(a, b):
            output += i
print(output)
