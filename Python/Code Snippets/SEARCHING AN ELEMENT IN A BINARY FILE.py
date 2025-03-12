import pickle
a=open("student.dat",'rb')
c=int(input("ENTER THE ADMISSION NUMBER: "))
d=0
while True:
    try:
        b=pickle.load(a)
        if b[0]==c:
            print(b)
            d=1
    except EOFError:
        break
if d==0:
    print("SORRY!!! RECORD NOT FOUND")