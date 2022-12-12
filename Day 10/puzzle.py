x = 1
cycle = 1
stall = 0
signal_strengths = 0
with open('input', 'r') as f:
    while True:
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            signal_strengths += cycle * x
        if stall > 0:
            stall -= 1
            continue
        line = f.readline()
        if not line:
            break
        match line.split():
            case ['addx', v]:
                stall = 2 - 1
                x += int(v)
            case ['noop']:
                stall = 1 - 1
print(signal_strengths)
