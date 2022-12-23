import io
import itertools


stall = 0
x = [1, 1, 1]
signal_strengths = 0
display_buffer = io.StringIO()
with open('input', 'r') as f:
    for cycle in itertools.count(1):
        if stall > 0:
            stall -= 1
        else:
            line = f.readline()
            if not line:
                break
            match line.split():
                case ['addx', v]:
                    x[2] = x[0] + int(v)
                    stall = 2 - 1
                case ['noop']:
                    x[1] = x[0]
                    stall = 1 - 1

        if cycle in (20, 60, 100, 140, 180, 220):
            signal_strengths += cycle * x[0]
        
        symbol = "#" if abs((cycle - 1) % 40 - x[0]) <= 1 else "."
        newline = "\n" if cycle % 40 == 0 else ""
        print(symbol, end=newline, file=display_buffer)
        
        del x[0]
        x.append(x[-1])

print(signal_strengths)
print(display_buffer.getvalue())
