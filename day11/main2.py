with open('data.in') as f:
    xs = [[int(x) for x in rand] for rand in f.read().split('\n')]

nrand = len(xs)
ncol = len(xs[1])

lista = [[-100000000000 for i in range(nrand + 2)] for j in range(ncol + 2)]

for i in range(nrand):
    for j in range(ncol):
        lista[i + 1][j + 1] = xs[i][j]

for i in lista:
    print(i)

dl = [0, -1, 0, 1, -1, 1, -1, 1]
dc = [-1, 0, 1, 0, 1, -1, -1, 1]

cnt = 0

while True:

    cnt+=1

    marked = {}
    flashes = []

    for i in range(1,nrand+1):
        for j in range(1,ncol+1):
            lista[i][j] += 1
            if lista[i][j] > 9:
                if (i, j) not in marked and (i,j) not in flashes:
                    flashes.append((i, j))

    while len(flashes):
        coords = flashes[0]
        flashes.pop(0)
        x = coords[0]
        y = coords[1]

        if coords not in marked:
            marked[coords] = 1
            lista[x][y] = 0

            for i in range(8):
                xx = x + dl[i]
                yy = y + dc[i]
                if (xx,yy) not in marked:
                    lista[xx][yy] += 1
                    if lista[xx][yy] > 9:
                        flashes.append((xx, yy))
    suma = 0
    for k,v in marked:
        suma += 1
    if suma == 100:
        break

for i in lista:
    print(i)
print(cnt)

