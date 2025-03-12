print('TO CHECK WHETHER A NUMBER IS PRIME OR COMPOSITE')
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('')
num=int(input("ENTER ANY NATURAL NUMBER: "))
n=int(num/2)
print('')
print('')
if num<1:
    print('sorry!!!',num,'IS NOT A NATURAL NUMBER')
else:
    if num!=1:
        for i in range(2,n+1):
             if (num%i)==0:
                 print(num,"IS A COMPOSITE NUMBER")
                 break
        else:
            print(num,"IS A PRIME NUMBER")
    else:
        print(num,'IS NEITHER PRIME NOR COMPOSITE')
print('')
print('')
print('******THANKS FOR USING THIS PROGRAM******')