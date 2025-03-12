#Q)1 
print("TO PRINT SIMPLE INTEREST AND COMPOUND INTEREST")
print()
p=int(input("enter principal amount: ")) 
t=int(input("enter time: ")) 
r=int(input("enter rate: ")) 
si=(p*t*r)/100
print()
print("simple interest is : ", si)
print()
amt= p*(1+(r/100))**t
ci=amt-p
print("compound interest is :",ci)
print()
print("******THANKS FOR USING THIS PROGRAM******")