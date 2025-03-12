#TO CREATE A BINARY FILE 'student.dat' WITH ROLLNO., NAME, AND MARKS AND SEARCH FOR A GIVEN RECORD USING ROLLNO.
#DATE:15/09/2022
#AUTHOR: ASWIN P

import pickle
print("STUDENT RECORD")
print("___________________")
print()
dic={}
st=open("student.dat",'ab+')
a=input("DO YOU WANT TO ENTER DATA? (y/n): ")
while a.lower()=='y':
    r=int(input("ENTER THE ROLL NO.: "))
    n=input("ENTER THE NAME: ")
    m=float(input("ENTER THE MARK: "))
    dic['r']=r
    dic['n']=n
    dic['m']=m
    pickle.dump(dic,st)
    print()
    a=input("DO U WANT TO CONTINUE? (y/n): ")
print()
an=input("DO YOU WANT TO SEARCH DATA (y/n): ")
while an.lower()=='y':
    st.seek(0)
    n=0
    s=int(input("ENTER THE ROLL NUMBER TO SEARCH: "))
    print('','','','','',sep='\n')
    print("STUDENT RECORD")
    print('____________________')
    print()
    print('%10s'%'ROLL NO.','%20s'%'NAME','%20s'%'MARKS')
    print('___________________________________________________________')
    while True:
        try:
            x=pickle.load(st)
            if x['r']==s:
                print('%10s'%x['r'],'%20s'%x['n'],'%20s'%x['m'],'%')
                print('','','','',sep='\n')
                n=1
        except EOFError:
            if n==0:
                print("NO RECORD FOUND WITH ROLL NO.",s)
            break
    an=input("DO YOU WANT TO SEARCH ANY OTHER STUDENT RECORD? (y/n): ")