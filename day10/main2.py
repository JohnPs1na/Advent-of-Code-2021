with open('data.in') as f:
    xs = f.read().split('\n')

def check(c,st):
    if c == ')' and st[len(st) - 1] == '(':
        return True
    elif c == ']' and st[len(st) - 1] == '[':
        return True
    elif c == '}' and st[len(st) - 1] == '{':
        return True
    elif c == '>' and st[len(st) - 1] == '<':
        return True
    return False

def hsh(c):
    if c == '(' : return 1
    elif c=='[' : return 2
    elif c=='{' : return 3
    else : return 4


scos = [0 for i in range(len(xs))]
score_list = []
for i in range(len(xs)):
    st = []
    rand = xs[i]
    score = 0

    for c in rand:
        if c == '(' or c == '[' or c == '{' or c == '<':
            st.append(c)
        else:
            if check(c,st):
                st.pop()
            else:
                scos[i] = 1
                break
                
    if not scos[i]:
        while len(st):
            score*=5
            score+=hsh(st[len(st)-1])
            st.pop()
        score_list.append(score)

print(sorted(score_list)[len(score_list)//2])
