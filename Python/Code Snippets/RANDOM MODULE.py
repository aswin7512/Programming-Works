user=int(input("enter the serial no: "))
import random
s=random.randint(1000,9999)
if user==s:
    print("you have won the lottery")
else:
    print("better luck next time")
    print("lucky no=",s)