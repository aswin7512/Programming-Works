#TO FIND THE FACTORIAL OF A NUMBER
#AUTHOR: ASWIN P
#DATE: 5/7/2022

#FUNCTION
def factorial(n):
    s=1
    for i in range(1,n+1):
            s*=i
    return s

#PROGRAM
n=int(input("ENTER A NUMBER: "))
a=factorial(n)
print("FACTORIAL OF",n,"=",a)