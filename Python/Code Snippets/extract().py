def extract():
    a=open('poem.txt')
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
            else:
                l+=1
    print("NO. OF VOWELS:",v,"NO. OF CONSONANTS:",c,"NO.OF UPPER CASE:",u,"NO.OF LOWER CASE:",l,sep='\n')
extract()