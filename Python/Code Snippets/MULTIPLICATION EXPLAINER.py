#how multiplication works step by step procedure
#getting the numbers
a,b=int(input("ENTER 1st NUMBER: ")),int(input("ENTER 2nd NUMBER: "))
r=a*b #calculating the product
m=[]
l1,l2,lr=len(str(a)),len(str(b)),len(str(r))
l=lr
if l1>l2:      #to get the largest number
    lu=l1
else:
    lu=l2
for i in range(l2):          #splitting the digits of the number for multiplication
    m.append(int(str(b)[i]))
c="%"+str(lr)+"s"
print(c%a)           #formatting the procedure
print(c%b)
ul="="*(lu+1)
print(c%ul)

cn=lr
for i in range(l2-1,0,-1):   #printing various steps
    num=int(m[i])*a
    nm="%"+str(cn)+"s"
    print(nm%num)
    cn-=1
print("="*lr)
print(r)       #printing the final product