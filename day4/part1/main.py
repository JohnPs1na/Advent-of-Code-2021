with open('data.in') as f:
    num_list = [int(i) for i in f.readline().split(',')]
    f.readline()
    bingo_list = []
    solved_list = []

    aux = f.read().split('\n\n')
    temp = []
    for i in range(len(aux)):
        temp = aux[i].split('\n')
        bingo_list.append([])
        for j in temp:
            bingo_list[i].append([int(x) for x in j.split()])
        solved_list.append([[0 for i in range(5)] for j in range(5)])


def verif(xs):
    for i in range(len(xs)):
        col_sum = 0
        row_sum = 0
        for j in range(len(xs)):
            row_sum += xs[i][j]
            col_sum += xs[j][i]

        if row_sum == 5 or col_sum == 5:
            return True


def function():
    global bingo_list, solved_list, num_list
    for elem in num_list:
        for poz in range(len(bingo_list)):
            for i in range(5):
                for j in range(5):
                    if bingo_list[poz][i][j] == elem:
                        solved_list[poz][i][j] = 1
                        if verif(solved_list[poz]):
                            return (bingo_list[poz],solved_list[poz],elem)

tup = function()

num = tup[2]
suma = 0

b = tup[0]
s = tup[1]

for i in range(5):
    for j in range(5):
        if s[i][j] == 0:
            suma+=b[i][j]

print(num*suma)
