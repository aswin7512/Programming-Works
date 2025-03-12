#UPDATE RATE IN A TABLE
from mysql import connector
from os import system
p=input('ENTER PASSWORD: ').lower()
system('clear')
conn=connector.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
if conn.is_connected():
    print('*********************************')
    print('CONNECTION ESTABLISHED')
    print('*********************************')
    mycursor=conn.cursor()
    ino=int(input('ENTER ITEM NO.: '))
    q='SELECT * FROM STORE WHERE ITEMNO='+str(ino)+';'
    #mycursor.execute(q)
    result=mycursor.fetchone()
    if result!=None:
        rate=int(input('ENTER THE NEW RATE: '))
        q='UPDATE STORE SET RATE=%s WHERE ITEMNO=%s;'%(rate,ino)
        #mycursor.execute(q)
        #conn.commit()
        print(mycursor.rowcount,'RECORD(S) UPDTATED')
    else:
        print('ITEM NOT FOUND')
    conn.close()