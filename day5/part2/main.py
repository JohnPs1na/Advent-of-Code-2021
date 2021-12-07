with open('data.in') as f:
    coordinates = []

    maxi = 0
    line = f.readline()

    while line:
        line = line.replace('\n', '')
        temp = line.split('->')
        cd1 = [int(i) for i in temp[0].split(',')]
        cd2 = [int(i) for i in temp[1].split(',')]

        maxi = max(max(cd1), max(cd2), maxi)

        coordinates.append((cd1, cd2))
        line = f.readline()

slist = [[0 for i in range(maxi+1)] for j in range(maxi+1)]

for coords in coordinates:
    x1 = coords[0][0]
    x2 = coords[1][0]
    y1 = coords[0][1]
    y2 = coords[1][1]

    dix = x2 - x1
    diy = y2 - y1

    ma = max(abs(dix), abs(diy))
    for i in range(1+ma):
        x = x1 + (1 if dix > 0 else (-1 if dix<0 else 0))*i
        y = y1 + (1 if diy > 0 else (-1 if diy<0 else 0))*i
        slist[x][y] += 1

s = 0
for i in range(maxi+1):
    for j in range(maxi+1):
        if slist[i][j] > 1:
            s+=1

print(s)

#got some ideas from yt because my answer was 19930 instead of 19929.
