#no of words in a sentence
print('TO COUNT NO OF WORDS')
print('————————————————————')
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