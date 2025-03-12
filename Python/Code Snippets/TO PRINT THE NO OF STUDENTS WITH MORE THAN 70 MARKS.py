#5, TO PRINT THE NO OF STUDENTS WITH MORE THAN 70 MARKS
#auhor: ASWIN P
#date:27/02/2022
print("TO PRINT THE NO OF STUDENTS SECURED MORE THAN 70 MARKS")
print()
c=0
ts=int(input("ENTER THE TOTAL NO OF STUDENTS: "))
print()
for i in range(ts):
    print("#",i+1)
    m=int(input("ENTER THE MARK: "))
    if m>70:
        c+=1
print()
print("NO OF STUDENTS WITH MORE THAN 70 MARKS=",c)
print()
print("******THANKS FOR USING THIS PROGRAM******")