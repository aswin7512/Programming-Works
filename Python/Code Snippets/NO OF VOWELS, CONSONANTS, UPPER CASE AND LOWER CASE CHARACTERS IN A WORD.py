#9, TO PRINT NO OF VOWELS, CONSONANTS, UPPER CASE AND LOWER CASE CHARACTERS IN A STRING
#author: 
#date: 
print("TO PRINT THE NO OF VOWELS, CONSONANTS, UPPER CASE AND LOWER CASE CHARACTERS IN A WORD")
print()
str=input("ENTER THE WORD: ")
print()
v,c,u,l=0,0,0,0
vo=("aeiouAEIOU")
for i in str:
    if i in vo:
        v+=1
    else:
        c+=1
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("NO. OF VOWELS=",v)
print("NO. OF CONSONANTS=",c)
print("NO. OF UPPER CASE=",u)
print("NO. OF LOWER CASE=",l)
print()
print("******THANKS FOR USING THIS PROGRAM******")