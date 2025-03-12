#TO SEPERATE EACH WORD BY #
#DATE: 
#AUTHOR: ASWIN P

with open ('story.txt') as a:
    b=a.read()
    c=b.split()
    for i in c:
        print(i,end='#')