#TO COUNT NO. OF VOWELS, CONSONANTS, UPPERCASE AND LOWERCASE CHARACTERS
#DATE: 
#AUTHOR: ASWIN P

with open('story.txt') as a:
    b=a.read()
    v,c,u,l=0,0,0,0
    vo=("aeiouAEIOU")
    for i in b:
        if i.isalpha():
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