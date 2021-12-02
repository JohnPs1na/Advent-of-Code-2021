with open('data.in') as f:
    xs = [0]
    cnt = -1
    x = f.readline()
    while x:
        if int(x) > xs[len(xs) - 1]:
            cnt+=1
        xs.append(int(x))
        x = f.readline()

print(cnt)
