#7, TO PRINT NO OF WORDS IN A STRING
#author: ASWIN P
#date:
print('TO COUNT NO OF WORDS')
print('')
str=input('Enter the sentence: ')
c=1
for i in str:
    if (i.isspace()):
        c+=1
print('')
print('No of words =',c)
print('')
print('THANKS FOR USING THIS PROGRAM')