print('TO PRINT FIBONACCI SERIES')
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print('')
n1,n2,fs=0,1,0
end=int(input("ENTER THE LAST POSITION: "))
print('')
while fs < end:
    print(n1)
    n3=n1+n2
    fs+=1               #fs=fs+1
    n1=n2
    n2=n3
print('')
print('******THANKS FOR USING THIS PROGRAM******')