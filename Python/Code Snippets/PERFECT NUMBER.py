#, TO PRINT WHETHER A NUMBER IS PERFECT OR NOT
#author: ASWIN P
#date:
print("TO PRINT WHETHER A NUMBER IS PERFECT OR NOT")
print()
n=int(input("ENTER THE NUMBER: "))
print()
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(n,"IS A PERFECT NUMBER")
else:
    print(n,"IS NOT A PERFECT NUMBER")
print()
print("******THANKS FOR USING THIS PROGRAM******")