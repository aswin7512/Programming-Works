a=float(input("ENTER THE FIRST NUMBER: "))
b=float(input("ENTER THE SECOND NUMBER: "))
o=input("ENTER THE OPERATOR: ")
if o=='+':
    print(a,'+',b,'=',a+b)
elif o=='-':
    print(a,'-',b,'=',a-b)
elif o=='*':
    print(a,'*',b,'=',a*b)
elif o=='/':
    print(a,'/',b,'=',a/b)
elif o=='**':
    print(a,'**',b,'=',a**b)
if o=='//':
    print(a,'//',b,'=',a//b)