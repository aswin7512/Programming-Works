from random import randint
sn = randint(0,10)
i = 1
while i < 4:
    n = int(input("ENTER A NUMBER: "))
    if n == sn:
        print("HURRAY YOU WON THE GAME!!")
        break
    elif i == 3:
        print("SORRY YOU FAILED THE GAME!!")
    i += 1