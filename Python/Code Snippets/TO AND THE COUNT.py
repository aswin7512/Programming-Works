#TO SEPERATE EACH WORD BY #
#DATE: 
#AUTHOR: ASWIN P

with open('poem.txt') as a:
    b=a.read()
    c=b.split()
    to,the=0,0
    for i in c:
        if i.lower()=='to':
            to+=1
        elif i.lower()=='the':
            the+=1
    print("NO. of 'TO':",to,"NO. of'THE':",the,sep='\n')