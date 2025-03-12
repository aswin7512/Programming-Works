n=int(input("Enter the number of employees: "))
d={}
for i in range(n):
    emp=input("enter the employee name")
    sal=int(input("enter the sallary"))
    d[emp]=sal
search=input("enter the name to search")
for i in d:
    if search=='emp':
        print('salary of',i,'is',d[i])
        break
    else:
         print('employee not found')