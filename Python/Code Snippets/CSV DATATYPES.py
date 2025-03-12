import csv
a=open('emp.csv','r+')
b=csv.reader(a)
c=csv.writer(a)
print(" reader: ",b,'\n','\t',"datatype: ",type(b),'\n',"writer: ",c,'\n','\t',"datatype: ",type(c))