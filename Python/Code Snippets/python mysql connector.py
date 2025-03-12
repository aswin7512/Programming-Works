import mysql.connector as mys
a=mys.connect(host='localhost',user='root',passwd='olakkente mood@9011')
if a.is_connected():
    print('CONNECTED SUCCESSFULLY')
else:
    print('NOT CONNECTED')