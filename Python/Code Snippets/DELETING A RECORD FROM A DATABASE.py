from mysql import connector as m
from os import system
p=input("ENTER PASSWORD: ").lower()
system('clear')
a=m.connect(host='localhost',user='u0_a208',passwd=p,database='cs2k23')
if a.is_connected():
    print("connected")
    b=a.cursor()
    q="DELETE FROM TEACHER WHERE TID=9"
    #b.execute(q)
    #a.commit()
    a.close()