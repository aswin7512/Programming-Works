#INSERTING ROW IN A TABLE
from mysql import connector
from os import system
p=input('ENTER PASSWORD: ').lower()
system('clear')
conn=connector.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
if conn.is_connected():
    print('CONNECTED SUCCESFULLY')
    mycursor=conn.cursor()
    print('ENTER THE DETAILS OF THE ITEM TO INSERT')
    print()
    itemno=input('ENTER ITEMNO: ')
    item=input('ENTER ITEM NAME: ').title()
    scode=input('ENTER SCODE: ')
    qty=input('ENTER QTY: ')
    rate=input('ENTER RATE: ')
    lastbuy=input('ENTER LAST BUY DATE [yyyy-mm-dd]: ')
    query="INSERT INTO STORE VALUES(%s,'%s',%s,%s,%s,'%s');"%(itemno,item,scode,qty,rate,lastbuy)
    #mycursor.execute(query)
    #conn.commit()
    print(mycursor.rowcount,'RECORD INSERTED')
    print('DATA SUCCESFULLY ADDED')
    conn.close()