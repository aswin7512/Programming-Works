#program to check whether a number is palindrome or not
x = input("ENTER A NUMBER: ")
cnt = len(x)
palindrome = 1
for i in range(int(cnt / 2 + 1)): 
    cnt -= 1
    if x[i] != x[cnt]: 
        palindrome = 0
        break
if palindrome: 
    print(True)
else:
    print(False)