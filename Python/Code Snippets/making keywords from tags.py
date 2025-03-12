a=input("ENTER THE TEXT: ")
b=a.split(",")
for i in range(len(b)):
    n=str(i+1)+". "
    b[i]=n+b[i]
for i in b:
    print(i)