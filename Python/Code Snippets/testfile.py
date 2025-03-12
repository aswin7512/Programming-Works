f=open('poem.txt','r')
str=f.readlines()
acount,bcount,ccount=0,0,0
for i in str:
    if i[0].lower() == 'a':
        acount+=1
    elif i[0].lower()=='b':
        bcount+=1
    elif i[0].lower()=='c':
        ccount+=1
nocount=len(str)
print(f'''The number of lines in the file is: {nocount}
The number of lines starting with letter a:{acount}
The number of lines starting with letter b:{bcount}
The number of lines starting with letter c:{ccount}''')
