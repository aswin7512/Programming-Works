#PROGRAM TO IMPLEMENT MONEY COLLECTION
from mysql import connector as msc
from os import system
from sys import exit
from time import sleep
while True:
    try:
        p=input('ENTER PASSWORD: ').lower()
        system('clear')
        a=msc.connect(host='localhost',user='u0_a208',passwd=p)
        break
    except:
        print('NOT CONNECTED')

b=a.cursor()
b.execute('SHOW DATABASES LIKE "MONEY_COLLECTION";')
c=b.fetchone()
if c==None:
    b.execute('CREATE DATABASE MONEY_COLLECTION;')
    a.commit()
    print('~~~DATABASE SUCCESSFULLY CREATED~~~')
    sleep(3)
    system('clear')
b.execute('USE MONEY_COLLECTION;')
print('1. NEW COLLECTION','2. EXISTING COLLECTION','3. EXIT',sep='\n')
print()
e=int(input('ENTER YOUR CHOICE(1/2/3): '))

while True:
    try:
        if e==2:
            b.execute('SHOW TABLES;')
            d=b.fetchall()
            if d!=[]:
                for i in range(len(d)):
                    print(str(i+1)+'.',d[i][0])
                print()
                ch=int(input('ENTER THE NO. OF THE COLLECTION IF NOT FOUND ENTER 0: '))
    except:
        print()