#program to find the square root of a number
x = int(input("ENTER A NUMBER: "))
sqrt = 0
if x > -1:
    for i in range(x):
        if i ** 2 <= x:
            sqrt = i
        else:
            break
else:
    print("ENTER A Non-Negative NUMBER!!!")
print(sqrt)