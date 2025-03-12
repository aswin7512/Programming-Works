#TO CREATE A BINARY FILE 'STUDENT.DAT' AND ENTER DATA INTO THE FILE AND UPDATE VALUES WITH ROLL NO.
#DATE: 23/09/2022
#AUTHOR: ASWIN P

import pickle
import os
print("STUDENT RECORD")
print("___________________")
print()
dic={}
st=open("student.dat",'ab')
while input("DO YOU WANT TO ENTER DATA? (y/n): ").lower()=='y':
    dic['r']=int(input("ENTER THE ROLL NO.: "))
    dic['n']=input("ENTER THE NAME: ")
    dic['m']=float(input("ENTER THE MARK: "))
    pickle.dump(dic,st)
    print()
st.close()

print()

print()
while input("DO YOU WANT TO UPDATE DATA? (y/n): ").lower()=='y':
    st=open("student.dat",'rb')
    st1=open('temp.dat','wb')
    nu=0
    s=int(input("ENTER THE ROLL NUMBER TO UPDATE: "))
    print('','','','','',sep='\n')
    while True:
        try:
            x=pickle.load(st)
            if x['r']==s:
                print()
                x['n']=input("ENTER THE NEW NAME: ")
                print("DATA SUCCESSFULLY UPDATED !!!")
                print('','',sep='\n')
                nu=1
            pickle.dump(x,st1)
        except EOFError:
            if nu==0:
                print("NO RECORD FOUND WITH ROLL NO.",s)
            print('','',sep='\n')
            break
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")
    st1.close()
    st.close()
    print('','','',sep='\n')
st=open("student.dat",'rb')
print("STUDENT RECORD")
print('____________________')
print()
print('%10s'%'ROLL NO.','%20s'%'NAME','%20s'%'MARKS')
print('___________________________________________________________')
while True:
    try:
        x=pickle.load(st)
        print('%10s'%x['r'],'%20s'%x['n'],'%20s'%x['m'],'%')
    except EOFError:
        break