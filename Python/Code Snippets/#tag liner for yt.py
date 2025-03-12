b=[]
a=input("ENTER TAG: ").lower()
while a!="":
    b.append(a)
    a=input().lower()
for i in range(len(b)):
    print(b[i],end=', ')