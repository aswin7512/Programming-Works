n=[12,13,34,56,21,79,98,22,35,38]
def PUSH(s,n):
    s.append(n)
def POP(s):
    while True:
        if s!=[]:
            print(s.pop(),end=" ")
        else:
            break
st=[]
for k in n:
    if k>33:
        PUSH(st,k)

POP(st)