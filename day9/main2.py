with open('data.in') as f:
    xs = f.read().split('\n')



dl = [-1,0,1,0]
dc = [0,1,0,-1]

lrand = len(xs[1])
lcol = len(xs)

lista = [[10 for i in range(lrand+2)] for j in range(lcol+2)]

mat = [[1 for x in range(lrand+2)] for n in range(lcol+2)]

size_arr = []



def lee(cx,cy):
    global dl,dc,lista,mat,size_arr,lcol,lrand
    #queues
    X = [cx]
    Y = [cy]

    while len(X)!=0:
        x = X[0]
        y = Y[0]

        elem = lista[x][y]

        for i in range(4):
            xx = x + dl[i]
            yy = y + dc[i]
            if elem < lista[xx][yy] and mat[xx][yy] != -1 and lista[xx][yy] != 9 and lista[xx][yy] != 10:
                X.append(xx)
                Y.append(yy)
                mat[xx][yy] = -1
                size_arr[len(size_arr) - 1] += 1
        X.pop(0)
        Y.pop(0)





for i in lista:
    print(i)

print()
for i in range(lcol):
    for j in range(lrand):
        lista[i+1][j+1] = int(xs[i][j])

for i in lista:
    print(i)

suma = 0

for i in range(1,lcol+1):
    for j in range(1,lrand+1):
        x = lista[i][j]
        if x < lista[i+1][j] and x < lista[i-1][j] and x < lista[i][j+1] and x < lista[i][j-1] and mat[i][j]!=-1:
            size_arr.append(1)
            lee(i,j)

size_arr = sorted(size_arr,reverse=True)
print(size_arr[0] * size_arr[1] * size_arr[2])
