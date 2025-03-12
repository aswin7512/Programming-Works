#ACCESSING DATABASE FROM PYTHON
from mysql import connector
from os import system
p=input('ENTER PASSWORD: ').lower()
system('clear')
conn=connector.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
if conn.is_connected():
    print('CONNECTION ESTABLISHED')
    print()
    mycursor=conn.cursor()
    mycursor.execute('SELECT * FROM STORE;')
    result=mycursor.fetchall()
    for i in result:
        print(i)
    print('TOTAL NO. OF ROWS=',mycursor.rowcount)
    conn.close()
else:
    print('ERROR IN CONNECTION')