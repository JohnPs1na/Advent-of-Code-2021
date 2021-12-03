with open('data.in') as f:
    xs = []
    x = f.readline()

    while x:
        temp = []
        for i in x:
            if i!='\n':
                temp.append(int(i))
        xs.append(temp)
        x = f.readline()

copy_xs = [i for i in xs]

oxy = []
carb = []

row_size = len(xs[0])

for j in range(row_size):
    cnt = 0
    for i in range(len(xs)):
        if xs[i][j]: # == True
            cnt+=1
        else:
            cnt-=1
    if cnt >= 0:
        oxy = [i for i in xs if i[j] == 1]
    else:
        oxy = [i for i in xs if i[j] == 0]
    xs = oxy

for j in range(row_size):
    cnt = 0
    for i in range(len(copy_xs)):
        if copy_xs[i][j]: # == True
            cnt+=1
        else:
            cnt-=1
    if cnt >= 0:
        carb = [i for i in copy_xs if i[j] == 0]
    else:
        carb = [i for i in copy_xs if i[j] == 1]
    if len(carb) == 1:
        break
    copy_xs = carb

oxy = oxy[0]
carb = carb[0]

o = 0
c = 0

for i in range(row_size):
    o+=oxy[i]*(2**(row_size-i-1))
    c+=carb[i]*(2**(row_size-i-1))

print(o*c)




