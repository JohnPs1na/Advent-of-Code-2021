with open('data.in') as f:
    xs = []
    x = f.readline().split(' | ')

    while x != ['']:
        to_add0 = x[0].split(' ')
        to_add1 = x[1].replace('\n', '').split(' ')

        xs.append((to_add0, to_add1))

        x = f.readline().split(' | ')

suma = 0

cnt = 0

for line in xs:
    for cod in line[1]:
            if len(cod) == 2 or len(cod) == 4 or len(cod) == 7 or len(cod) == 3:
                cnt+=1
print(cnt)






