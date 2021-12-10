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
    decoded = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
        0:0,
    }
    while cnt < 10:
        for cod in line[0]:
            if len(cod) == 2 and not decoded[1]:
                decoded[1] = cod
                cnt+=1
            elif len(cod) == 3 and not decoded[7]:
                decoded[7] = cod
                cnt+=1
            elif len(cod) == 4 and not decoded[4]:
                decoded[4] = cod
                cnt+=1
            elif len(cod) == 7 and not decoded[8]:
                cnt+=1
                decoded[8] = cod
            elif len(cod) == 5 and decoded[7] and not decoded[3]:
                tmp_cnt = 0
                for i in cod:
                    if i in decoded[7]:
                        tmp_cnt+=1
                if tmp_cnt == 3:
                    cnt+=1
                    decoded[3] = cod
            elif len(cod) == 6 and decoded[3] and not decoded[9]:
                tmp_cnt = 0
                for i in decoded[3]:
                    if i in cod:
                        tmp_cnt+=1
                if tmp_cnt == 5:
                    cnt+=1
                    decoded[9] = cod
            elif len(cod) == 6 and decoded[9] and decoded[1] and not decoded[0]:
                tmp_cnt = 0
                for i in decoded[1]:
                    if i in cod:
                        tmp_cnt += 1
                if tmp_cnt == 2:
                    decoded[0] = cod
                    cnt+=1
            elif len(cod) == 6 and decoded[9] and decoded[1] and not decoded[6]:
                tmp_cnt = 0
                for i in decoded[1]:
                    if i in cod:
                        tmp_cnt+=1
                if tmp_cnt<2:
                    decoded[6] = cod
                    cnt+=1
            elif len(cod) == 5 and decoded[6] and not decoded[5]:
                tmp_cnt = 0
                for i in decoded[6]:
                    if i in cod:
                        tmp_cnt+=1
                if tmp_cnt == 5:
                    decoded[5] = cod
                    cnt+=1
            elif len(cod) == 5 and decoded[6] and decoded[3] and not decoded[2]:
                tmp_cnt = 0
                for i in decoded[6]:
                    if i in cod:
                        tmp_cnt+=1
                if tmp_cnt!=5 and sorted(cod) != sorted(decoded[3]):
                    decoded[2] = cod
                    cnt+=1
    numba = 0

    for cod in line[1]:
        for j in range(10):
            if sorted(cod) == sorted(decoded[j]):
                numba+=j
                numba*=10

    numba/=10
    print(line[1],numba)
    suma+=numba
    cnt = 0

print(suma)






