import itertools


def snafu2dec(snafu: str) -> int:
    conversion_table = {
        '=': -2,
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2,
    }
    return sum((5 ** exp) * conversion_table[digit] for exp, digit in enumerate(snafu[::-1]))


def dec2snafu(dec: int) -> str:
    if dec == 0:
        return "0"
    conversion_table = {
        0: '0',
        1: '1',
        2: '2',
        3: '=',
        4: '-',
    }
    snafu = []
    while dec:
        dec, mod = divmod(dec, 5)
        snafu.append(conversion_table[mod])
        if mod > 2:
            dec += 1
    return "".join(snafu[::-1])


test_values = [
    (        1,              "1"),
    (        2,              "2"),
    (        3,             "1="),
    (        4,             "1-"),
    (        5,             "10"),
    (        6,             "11"),
    (        7,             "12"),
    (        8,             "2="),
    (        9,             "2-"),
    (       10,             "20"),
    (       15,            "1=0"),
    (       20,            "1-0"),
    (     2022,         "1=11-2"),
    (    12345,        "1-0---0"),
    (314159265,  "1121-1110-1=0"),
]
for dec, snafu in test_values:
    assert snafu2dec(snafu) == dec
    assert dec2snafu(dec) == snafu

with open('input', 'r') as f:
    s = sum(map(snafu2dec, map(str.strip, f.readlines())))
    print(s)
    print(dec2snafu(s))
