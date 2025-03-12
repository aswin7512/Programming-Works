from mysql import connector as m
from time import sleep
from os import system
p=input("ENTER PASSWORD: ")
system('clear')
a=m.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
if a.is_connected():
    b=a.cursor()
    q="SELECT * FROM EMPLOYEE;"
    b.execute(q)
    c=b.fetchall()
    print('%10s'%'EMPNO.','%10s'%'ENAME','%10s'%'SALARY','%10s'%'BONUS','%10s'%'DEPTID.','%15s'%'JOB','%10s'%'MGR','%15s'%'HIREDATE')
    print('='*98,'\n')
    sleep(1)
    for i in c:
        print('%10s'%i[0],'%10s'%i[1],'%10s'%i[2],'%10s'%i[3],'%10s'%i[4],'%15s'%i[5],'%10s'%i[6],'%15s'%i[7])
        sleep(1)
    a.close()