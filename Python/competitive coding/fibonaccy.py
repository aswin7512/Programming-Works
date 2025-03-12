#program to find nth fibonacci number
n = int(input("ENTER nth term TO FIND: "))
fa, fb = 0, 1
for i in range(n -1):
    fa, fb = fb, fa + fb
if n == 0:
    print(fa)
else:
    print(fb)