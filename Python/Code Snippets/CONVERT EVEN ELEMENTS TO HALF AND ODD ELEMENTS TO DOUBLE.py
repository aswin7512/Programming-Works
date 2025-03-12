#2, TO CONVERT EVEN ELEMENTS TO HALF AND ODD ELEMENTS TO DOUBLE
#auhor: ASWIN P
#date:27/02/2022
print("TO CONVERT EVEN ELEMENTS TO HALF AND ODD ELEMENTS TO DOUBLE")
print()
List=eval(input("ENTER THE LIST: "))
print()
l=len(List)
for i in range(l):
    if List[i]%2==0:
        List[i]//=2
    else:
        List[i]*=2
print("FINAL LIST: ",List)
print()
print("******THANKS FOR USING THIS PROGRAM******")