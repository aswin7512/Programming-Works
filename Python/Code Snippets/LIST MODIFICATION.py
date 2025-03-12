#TO HALF EVEN ELEMENTS AND DOUBLE ODD ELEMENTS IN A LIST THROUGH FUNCTION
#AUTHOR: ASWIN P
#DATE:8/7/2022

#FUNCTION
def change_list(list):
    for i in range(len(list)):
        if list[i]%2==0:
            list[i]//=2
        else:
            list[i]*=2
    print(list)

#PROGRAM  
n=int(input("ENTER THE NO. OF ELEMENTS: "))
l=[]
for i in range(n):
    e=int(input("ENTER THE ELEMENT: "))
    l.append(e)
change_list(l)