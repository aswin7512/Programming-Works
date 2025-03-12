#TO READ A FILE AND SEPERATE EACH WORD WITH '#'
#AUTHOR: ASWIN P
#DATE: 14/07/2022

#FUNCTION
def modify():
    a=open('story.txt')
    b=a.read()
    c=b.split()
    for i in c:
        print(i,end='#')
modify()