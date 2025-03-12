n=int(input("ENTER A NUMBER: "))
rv=0
while n!=0:
    r=n%10
    rv=rv*10+r
    n//=10
while rv!=0:
    r=rv%10
    print('*'*r)
    rv//=10