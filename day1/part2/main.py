with open('data.in') as f:
    xs = [0]
    x = f.readline()
    while x:
        xs.append(int(x))
        x = f.readline()

xs2 = [0]
cnt = -1
for i in range(len(xs) - 3):
    if sum(xs[i:i+3]) > xs2[len(xs2)-1]:
        cnt+=1
    xs2.append(sum(xs[i:i+3]))

print(cnt)
