#TO REMOVE LINE WITH 'a'' AND ADD IT TO ANOTHER FILE
#DATE: 18/08/2022
#AUTHOR: ASWIN P

a=open("abcd.txt")
d=open("mod.txt",'w')
b=a.readlines()
l1,l2=[],[]
for i in b:
    if 'a' in i:
        l1.append(i)
    else:
        l2.append(i)
d.writelines(l1)
d.close()
a.close()
f=open("abcd.txt",'w')
f.writelines(l2)
f.close()