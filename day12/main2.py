from collections import deque

with open('data.in') as f:
    x = f.read().split('\n')
    di = {}

for i in x:
    line = i.split('-')
    if line[0] not in di:
        di[line[0]] = [line[1]]
    else:
        di[line[0]].append(line[1])
    if line[1] not in di:
        di[line[1]] = [line[0]]
    else:
        di[line[1]].append(line[0])

cnt = 0
start = ('start', {'start'}, None)
que = [start]
while que:
    node, lower, double = que[0][0], que[0][1], que[0][2]
    que.pop(0)

    if node == 'end':
        cnt += 1
        continue
    for neighbor in di[node]:
        if neighbor not in lower:
            new_low = set(lower)
            if neighbor.islower():
                new_low.add(neighbor)
            que.append((neighbor, new_low,double))
        elif neighbor in lower and double is None and neighbor not in ['start','end']:
            que.append((neighbor,lower,1))
print(cnt)
