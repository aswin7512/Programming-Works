from mysql import connector as m
from os import system
p=input("ENTER PASSWORD: ").lower()
system('clear')
a=m.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
if a.is_connected():
    print("connected")
    b=a.cursor()
    q="create table sales_representatives(SALESMAN_NAME varchar(15),CODE int primary key,ADDRESS varchar(40),COMMISION varchar(20),SALARY int )"
    #b.execute(q)
    #a.commit()
    a.close()