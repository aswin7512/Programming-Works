import csv
a=open("emp.csv",'r')
c=csv.reader(a)
for i in c:
    print(i)