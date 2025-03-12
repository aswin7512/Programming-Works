def PUSH_ELEMENT(st):
    if st[2]=='Goa':
        S.append([st[0],st[1]])

def POP_ELEMENT():
    if S==[]:
        print("~~~STACK UNDERFLOW~~~")
    while S!=[]:
        d=S.pop()
        print(d)

S=[]
while input("DO YOU WANT TO ENTER DATA?(y/n): ").lower()=='y':
    a=input("ENTER CUSTOMER NAME: ").title()
    b=int(input("ENTER PHONE NO.: ")) 
    c=input("ENTER CITY: ").title()
    PUSH_ELEMENT([a,b,c])
    print('\n'*2)
POP_ELEMENT()