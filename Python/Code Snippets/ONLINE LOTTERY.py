#TO SIMULATE ONLINE LOTTERY
#DATE:
#AUTHOR: ASWIN P

import random as r
a=int(input("ENTER YOUR 4 DIGIT NO: "))
b=r.randint(1000,9999)
if a==b:
    print("HURRAY!!! YOU WON THE LOTTERY")
else:
    print("BETTER LUCK NEXT TIME")
    print("LUCKY NUMBER IS:",b)