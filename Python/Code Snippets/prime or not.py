#TO CHECK WHETHER A NUMBER IS PRIME OR NOT
#AUTHOR: ASWIN P
#DATE: 12/07/2022

#FUNCTION
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True

#PROGRAM
a=int(input("ENTER THE NUMBER: "))
x=prime(a)
if x==True:
    print(a,"is a PRIME number!!!")
else:
    print(a,"is NOT a PRIME number!!!")