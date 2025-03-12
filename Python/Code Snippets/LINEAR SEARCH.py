#TO SEARCH AN ELEMENT FROM A LIST
#AUTHOR: ASWIN P
#DATE: 12/7/2022

#FUNCTION
def search(l,s):
    it=0
    pos=[]
    for i in range(len(l)):
        if l[i]==s:
            it+=1
            pos.append(i+1)
    if it==0:
        print("element",s,"is NOT present")
    else:
        print("element",s,"is PRESENT",it,"time(s) at the position(s)",pos)

#PROGRAM
n=int(input("ENTER THE NO.OF ELEMENTS: "))
list=[]
for i in range(n):
    s=int(input("ENTER THE ELEMENT: "))
    list.append(s)
item=int(input("ENTER THE ITEM TO SEARCH: "))
search(list,item)