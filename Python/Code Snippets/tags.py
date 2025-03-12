b=[]
a=input("ENTER TAG: ")
while a!="":
    b.append(a)
    a=input()
for i in range(len(b)):
    n=str(i+1)+". "
    b[i]=n+b[i]
for i in b:
    print(i)