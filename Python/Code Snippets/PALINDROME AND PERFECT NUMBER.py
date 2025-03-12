#palindrome or perfect number
#AUTHOR: ASWIN P
#DATE: 5/7/2022

#PERFECT NUMBER
def checkpn(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print(n,"IS A PERFECT NUMBER")
    else:
        print(n,"IS NOT A PERFECT NUMBER")

#PALINDROME
def checkpl(n):
    nt=n
    r=0
    while n>0:
        dt=n%10
        r=(r*10)+dt
        n//=10
    if nt==r:
        print(nt,"is a PALINDROME NUMBER")
    else:
        print(nt,"is NOT a PALINDROME NUMBER")

#PROGRAM
x=int(input("ENTER THE NUMBER: "))
checkpl(x)
checkpn(x)