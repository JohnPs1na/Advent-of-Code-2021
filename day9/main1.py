with open('data.in') as f:
    xs = f.read().split('\n')

lrand = len(xs[1])
lcol = len(xs)

lista = [[10 for i in range(lrand+2)] for j in range(lcol+2)]

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
        if x < lista[i+1][j] and x < lista[i-1][j] and x < lista[i][j+1] and x < lista[i][j-1]:
            suma+=x+1

print(suma)
