#9, TO STORE ITEM NAME AND PRICE IN A DICTIONARY AND PRINT IT
#auhor: ASWIN P
#date:27/02/2022
print("TO STORE ITEM NAME AND PRICE IN A DICTIONARY AND PRINT IT")
print()
ino=int(input("ENTER THE NO OF ITEMS: "))
Ditem={}
for i in range(ino):
    print("#",i+1)
    inam=input("ENTER THE NAME OF ITEM: ")
    print()
    iprice=float(input("ENTER THE PRICE OF THE ITEM: "))
    Ditem[inam]=iprice
print()
print(Ditem)