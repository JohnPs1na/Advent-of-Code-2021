with open('data.in') as f:
    xs = [int(i) for i in f.readline().split(',')]
    s = 0
    mi = 0
    for i in range(len(xs)):
        for j in range(len(xs)):
            s+=abs(xs[j] - xs[i])
        if i == 0:
            mi = s
        else:
            mi = min(mi,s)
        s = 0

print(mi)
