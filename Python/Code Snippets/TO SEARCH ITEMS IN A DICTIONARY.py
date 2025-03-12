#4, TO SEARCH ITEMS IN A DICTIONARY
#auhor: ASWIN P
#date:27/02/2022
print("TO SEARCH FOR ITEMS IN  A DICTIONARY")
print()
dic={}
n=int(input("ENTER THE NO OF ITEMS TO BE ADDED: "))
print()
for i in range(n):
    print("#",i+1)
    kk=input("ENTER THE ITEM: ")
    v=int(input("ENTER THE RATE OF ITEM: "))
    print()
    k=kk.upper()
    dic[k]=v
ss=input("ENTER THE ITEM TO SEARCH: ")
s=ss.upper()
print()
for j in dic:
    if s==j:
        print("ITEM FOUND",s,"₹",dic[s])
        break
else:
    print("SORRY! ITEM NOT FOUND")
print()
print("******THANKS FOR USING THIS PROGRAM******")