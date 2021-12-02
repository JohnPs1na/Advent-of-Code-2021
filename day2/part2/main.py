with open('data.in') as f:
    horizontal = 0
    aim = 0
    depth = 0
    xs = []
    x = f.readline().split()
    while x:
        if x[0] == 'forward':
            horizontal+=int(x[1])
            depth += aim * int(x[1])
        elif x[0] == 'down':
            aim+=int(x[1])
        elif x[0] == 'up':
            aim-=int(x[1])
        x = f.readline().split()

print(horizontal * depth)
