from collections import defaultdict

with open('data.in') as f:
    xs = [int(i) for i in f.readline().split(',')]

    freq = [0 for i in range(9)]

    for i in xs:
        freq[i]+=1

    for i in range(256):
        zero = freq[0]
        for i in range(8):
            freq[i]=freq[i+1]
        freq[8]=zero
        freq[6]+=zero

print(sum(freq))
