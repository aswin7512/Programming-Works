b=[]
a=input("ENTER TAG: ")
while a!="":
    b.append(a)
    a=input()
for i in range(len(b)):
    b[i]=b[i][3::]
for i in b:
    print(i,end=',')