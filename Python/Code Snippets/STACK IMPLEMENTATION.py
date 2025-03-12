#STACK IMPLEMENTATION USING USER DEFINED FUNCTIONS
#DATE: 13/10/2022
#AUTHOR: ASWIN P

s=[]
import os
import sys
def CHOICE():
    c=0
    while c <1 or c>4:
        (lambda: os.system("clear"))()
        print('\t'*5,"STACK IMPLEMENTATION")
        print('\t'*5,"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
        print("\t"*2,"1, PUSH",'\n',"\t"*2,"2, POP",'\n','\t'*2,"3, DISPLAY",'\n','\t'*2,"4, EXIT")
        c=int(input("ENTER YOUR CHOICE(1/2/3/4): "))
    return c
def PUSH(elm):
    s.append(elm)
    print("\t"*2,elm,'SUCCESSFULLY PUSHED!!!')
def POP():
    if s==[]:
        print('\t'*2,"STACK UNDERFLOW!!!")
    else:
        return s.pop()
def DISPLAY():
    if s==[]:
        print('\t'*2,"STACK UNDERFLOW!!!")
    else:
        sd=s[::-1]
        for i in sd:
            print('\t'*2,i,end='\n')
def EXIT():
    sys.exit()

while True:
    c=CHOICE()
    if c==1:
        PUSH(input("ENTER ITEM TO PUSH: "))
    elif c==2:
        print('\t'*2,"POPPED ELEMENT:",POP())
    elif c==3:
        DISPLAY()
    elif c==4:
        EXIT()
    print('\n'*3)
    input("≈≈≈PRESS ENTER KEY TO CONTINUE≈≈≈")