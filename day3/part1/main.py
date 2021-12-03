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

gamma = []
epsilon = []

row_size = len(xs[0])
col_size = len(xs)

for j in range(row_size):
    cnt = 0
    for i in range(col_size):
        if xs[i][j]: # == True
            cnt+=1
        else:
            cnt-=1
    if cnt > 0:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

g_rez = 0
e_rez = 0

for i in range(row_size):
    g_rez+=gamma[i]*(2**(row_size-i-1))
    e_rez+=epsilon[i]*(2**(row_size-i-1))

print(g_rez*e_rez)
