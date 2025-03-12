import mysql.connector as m
import os
p=input("ENTER PASSWORD: ").lower()
os.system("clear")
a=m.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
b=a.cursor()
while input("continue?: ")=='':
    os.system('clear')
    if a.is_connected:
        print("~~~CONNECTED SUCCESSFULLY~~~")
        c=input("TID: ")
        d=input("NAME: ").upper()
        e=input("AGE: ")
        f=input("DEPARTMENT: ").upper()
        g=input("DATE OF JOIN: ")
        h=input("SALARY: ")
        i=input("GENDER: ").upper()
        q="insert into TEACHER values(%s,'%s',%s,'%s','%s',%s,'%s');"%(c,d,e,f,g,h,i)
        print(q)
        #b.execute(q)
        #a.commit()
a.close()