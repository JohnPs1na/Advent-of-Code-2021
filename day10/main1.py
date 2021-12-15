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
    if c == ')' : return 3
    elif c==']' : return 57
    elif c=='}' : return 1197
    else : return 25137

suma = 0

for rand in xs:
    st = []
    for c in rand:
        if c == '(' or c == '[' or c == '{' or c == '<':
            st.append(c)
        else:
            if check(c,st):
                st.pop()
            else:
                suma+=hsh(c)
                break

print(suma)



