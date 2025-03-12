n=int(input("ENTER THE NUMBER"))
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