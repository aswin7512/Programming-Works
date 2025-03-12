import pickle
def Createfile():
    f=open("book.dat",'ab')
    a='y'
    while a.lower()=='y':
        bno=int(input("ENTER THE BOOK NO.: "))
        bnam=input("ENTER BOOK NAME: ").title()
        aut=input("ENTER THE AUTHOR NAME: ").title()
        pr=int(input("ENTER THE PRICE: "))
        x=[bno,bnam,aut,pr]
        pickle.dump(x,f)
        a=input("continue?(y/n)")
    f.close()
def countrec(author):
    f=open("book.dat",'rb')
    c=0
    while True:
        try:
            a=pickle.load(f)
            if a[2]==author:
                c+=1
        except EOFError:
            print("NO. OF BOOKS WRITTEN BY",author,'=',c)
            break
    return c
Createfile()
countrec(input("ENTER AUTHOR TO SEARCH: ").title())