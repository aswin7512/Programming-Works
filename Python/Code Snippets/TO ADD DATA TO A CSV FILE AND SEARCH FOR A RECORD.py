#TO CREATE A CSV FILE 'EMP.CSV' AND ENTER DATA INTO THE FILE AND SEARCH RECORDS WITH EMPLOYEE NO.
#DATE: 30/09/2022
#AUTHOR: ASWIN P

import csv
a=open("emp.csv",'a')
fl=[]
b=csv.writer(a)
while input("DO YOU WANT TO ENTER DATA? (y/n): ").lower()=='y':
    print('','',sep='\n')
    eno=int(input("ENTER EMPLOYEE NUMBER: "))
    en=input("ENTER EMPLOYEE NAME: ")
    pno=int(input("ENTER EMPLOYEE PHONE NUMBER: "))
    fl.append([eno,en,pno])
    print('','',sep='\n')
b.writerows(fl)
a.close()
print('','',sep='\n')
while input("DO YOU WANT TO SEARCH ANY RECORD (y/n): ").lower()=='y':
    print()
    s=int(input("ENTER EMPLOYEE NUMBER TO SEARCH: "))
    print('','',sep='\n')
    print("EMPLOYEE RECORD")
    print('____________________')
    print()
    print('%20s'%'EMPLOYEE NUMBER','%30s'%'NAME','%30s'%'MOBILE NUMBER')
    print('_______________________________________________________________________________________________')
    print()
    n=0
    a=open('emp.csv','r')
    c=csv.reader(a)
    for i in c:
        if int(i[0])==s:
            print("%20s"%i[0],"%30s"%i[1],"%30s"%i[2])
            n=1
    if n==0:
        print("NO RECORD FOUND !!!")
    print('','',sep='\n')
a.close()