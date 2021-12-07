with open('data.in') as f:
    xs = [int(i) for i in f.readline().split(',')]

    mi = 0
    for i in range(1000):
        s = 0
        for j in range(len(xs)):
            x = abs(xs[j] - i)
            s += x * (x + 1) // 2
        if i == 0:
            mi = s
        else:
            mi = min(mi, s)

print(mi)
