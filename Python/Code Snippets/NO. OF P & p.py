#TO SEPERATE EACH WORD BY #
#DATE: 
#AUTHOR: ASWIN P

with open ('poem.txt') as a:
    b=a.readlines()
    cp,cP=0,0
    for i in b:
        if i[0]=='p':
            cp+=1
        elif i[0]=='P':
            cP+=1
    print("NO. OF LINES STARTING WITH 'P'=",cP,"& NO. OF LINES STARTIING WITH 'p'=",cp)