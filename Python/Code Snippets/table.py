import mysql.connector as msc
from os import system


def len_cal(l1, l2):
    length, n = {}, 0
    for i in l1:
        length[n] = len(i[0]) + 1
        n += 1
    for i in l2:
        n = 0
        for j in range(len(i)):
            l = len(str(i[j])) + 1
            if l > length[n]:
                length[n] = l
            n += 1
    return length


def print_line(length):
    print('\n+', end = "")
    for i in length:
        print("-"*length[i] + "+", end = "")


def print_table(length, l1, l2):
    print_line(length)
    
    print("\n|", end = "")
    for i in length:
        print(f"%{length[i]}s|"%l1[i][0], end = "")
    print_line(length)
    
    for i in l2:
        print("\n|", end = "")
        for j in length:
            print(f"%{length[j]}s|"%i[j], end = "")
    
    print_line(length)
    print()
        

conn = msc.connect(host = "localhost", user = "root", passwd = input("Enter Password: "), database = "company")
system("cls")
cur = conn.cursor()
ch = 1
while(ch):
    tbl_nme = input("Enter Table Name: ")
    cur.execute(f"desc {tbl_nme};")
    r = cur.fetchall()
    cur.execute(f"Select * from {tbl_nme};")
    res = cur.fetchall()

    length = len_cal(r, res)
    print_table(length, r, res)
    
    ch = int(input("\nHave more to print?(0/1): "))

conn.close()
cur.close()
