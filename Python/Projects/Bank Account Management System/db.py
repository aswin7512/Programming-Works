import mysql.connector as msc

access = msc.connect(host = 'localhost', 
                        user = 'root',
                        passwd = 'olakkente mood@9011',
                        database = 'bank_account')
access.autocommit = True


def lex_sum(string):
    sum = 0
    for ch in string:
        sum += ord(ch)
    return sum


def xoscrypii(value, key):
    a = ""
    for i in str(value ^ lex_sum(key)):
        a += chr(int(i))
    return a


'''def doscrypii(value, key):
    a = ''
    for i in value:
        a += str(ord(i))
    return int(a) ^ lex_sum(key)'''


def init_table(tname):
    curs = access.cursor()
    tname_tuple = eval(f"'{tname}',")
    curs.execute("SHOW TABLES;")
    if tname_tuple not in curs:
        curs.execute(f"""CREATE TABLE {tname}(
        username VARCHAR(30) PRIMARY KEY,
        acc_no INT UNIQUE NOT NULL,
        name VARCHAR(50) NOT NULL,
        pin VARCHAR(50) NOT NULL,
        balance DECIMAL(15,2) NOT NULL);""")
    curs.close()
    return tname
def create_user(table_name, username, name, pin, balance):
    curs = access.cursor()
    acc_no = 1001
    curs.execute(f"SELECT MAX(acc_no) from {table_name}")
    acc_max = curs.fetchone()
    if acc_max[0] is not None:
        acc_no = acc_max[0] + 1
    pin = xoscrypii(pin, username)
    query = f"INSERT INTO {table_name} VALUES('{username}',\
    {acc_no},\
    '{name}',\
    '{pin}',\
    {balance});"
    curs.execute(query)
    tbl_name = '_' + str(acc_no)
    query = f"""CREATE TABLE {tbl_name}(statements DECIMAL(15,2) NOT NULL,
    current_bal DECIMAL(15,2) NOT NULL)"""
    curs.execute(query)
    query = "INSERT INTO {0} VALUES({1},{1});".format(tbl_name,balance)
    curs.execute(query)
    curs.close()


def does_uname_exist(tname, uname):
    curs = access.cursor()
    query = f"SELECT username FROM {tname} WHERE username = '{uname}'"
    curs.execute(query)


    uname_table = curs.fetchone()
    curs.close()
    return uname_table == eval(f"('{uname}',)")


def authenticate(tname, uname, pin):
    curs = access.cursor()
    pin = xoscrypii(pin, uname)
    query = f"SELECT * FROM {tname} WHERE \
    username = '{uname}' AND \
    pin = '{pin}';"
    curs.execute(query)
    user_data = curs.fetchone()
    if user_data is None:
        return None, None, None, None, None
    else:
        return user_data


def update_balance(tname, acc_no, amount):
    curs = access.cursor()
    statement_table = '_' + str(acc_no)

    query = f"""UPDATE {tname} 
    SET balance = balance + {amount} 
    WHERE acc_no = {acc_no};"""
    curs.execute(query)
    query = f"SELECT balance FROM {tname} WHERE acc_no = {acc_no}"
    curs.execute(query)
    balance = (curs.fetchone())[0]

    query = f"INSERT INTO {statement_table} VALUES({amount}, {balance});"
    curs.execute(query)
    curs.close()


def get_statement(acc_no):
    statement_table = '_' + str(acc_no)
    curs = access.cursor()

    query = f"SELECT * FROM {statement_table}"
    curs.execute(query)

    return curs.fetchall()


def valid_acc_no(tname, acc_no, name):
    curs = access.cursor()
    query = f"SELECT * FROM {tname} WHERE acc_no = {acc_no} AND name = '{name}';"
    curs.execute(query)
    result = curs.fetchone()
    return result is not None

def fetch_balance(tname, user_name):
    curs = access.cursor()
    query = f"SELECT balance FROM {tname} \
    WHERE username = '{user_name}'"
    curs.execute(query)
    bal = curs.fetchone()
    return bal[0]


def close_conn():
    access.close()