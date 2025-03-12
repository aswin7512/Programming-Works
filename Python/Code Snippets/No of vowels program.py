#no of vowels in a sentence
print('TO COUNT N0 OF VOWELS')
print('—————————————————————')
print('')
str=input('Enter the sentence: ')
c=0
vowels=('aeiouAEIOU')
for i in str:
    if(i in vowels):
        c+=1
print('')
print('no of vowels =',c)
print('')
print('******THANKS FOR USING THIS PROGRAM******')