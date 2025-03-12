n=int(input("ENTER THE no. OF TERMS: "))
p=1
for i in range(1,2*n+1,2):
    p*=i
print("PRODUCT OF FIRST",n,"ODD NUMBERS ARE",p)