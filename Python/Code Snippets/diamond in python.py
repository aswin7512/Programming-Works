n=int(input("ENTER NO. OF ROWS: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(2*i-1):
        print("*", end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print("*", end="")
    print()