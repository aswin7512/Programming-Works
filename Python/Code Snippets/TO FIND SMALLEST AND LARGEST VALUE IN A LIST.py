#3, TO FIND SMALLEST AND LARGEST VALUE IN A LIST
#auhor: ASWIN P
#date:27/02/2022
print("TO FIND SMALLEST AND LARGEST VALUE IN A LIST")
print()
List=eval(input("ENTER THE LIST: "))
print()
low,high,pos1,pos2,l=List[0],List[0],0,0,len(List)
for i in range(l):
    if low>List[i]:
        low=List[i]
        pos1=i
for j in range(l):
    if high<List[j]:
        high=List[j]
        pos2=i
print("smallest value=",low)
print("index position=",pos1)
print()
print("highest value=",high)
print("index position=",pos2)