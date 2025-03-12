#PERIODIC TABLE QUIZ
import shutil
from os import system
import sys
from time import sleep
from mysql import connector as msc
RESET = '\033[0m'         # Reset to default color
GREEN = '\033[32m'        # Green text color
while True:
    try:
        p=input('ENTER PASSWORD: ').lower()
        system('cls')
        a=msc.connect(host='localhost',user='root',passwd=p,database='quiz_data')
        break
    except:
        print('NOT CONNECTED')
cursor=a.cursor()

def quiz():
    global point
    cursor.execute('SELECT * FROM QUIZ;')
    data=cursor.fetchall()
    for i in data:
        print('\n'*2)
        print("Q"+str(i[0])+'.',i[1])
        print()
        print("(a)",i[2])
        print("(b)",i[3])
        print("(c)",i[4])
        print("(d)",i[5])
        ans=input("ENTER YOUR OPTION(a/b/c/d): ")
        if i[2]==i[6]:
            cans='a'
        elif i[3]==i[6]:
            cans='b'
        elif i[4]==i[6]:
            cans='c'
        elif i[5]==i[6]:
            cans='d'
        if ans==cans:
            point+=1
        print()
        print('CORRECT ANSWER:',GREEN + i[6] + RESET)

def matchf():
    global point
    ans=[]
    cursor.execute('SELECT * FROM MATCHF;')
    data=cursor.fetchall()
    for i in data:
        print('%20s'% str(i[0])+'. '+i[1],'%20s'%'('+i[2]+') '+i[3])
    
    for i in range(len(data)):
        s=str(data[i][0])+'==>?: '
        a=input(s)
        for j in range(len(data)):
            if data[i][4]==data[j][3]:
                ans.append([str(data[i][0])+'. '+data[i][1],'('+data[j][2]+') '+data[j][3]])
                k=j
                break
        if a==data[k][2]:
            point+=2

    for i in ans:
        print('%20s'%GREEN+i[0]+RESET,'%20s'%GREEN+i[1]+RESET)

def guess():
    global point
    
    cursor.execute('SELECT * FROM guess;')
    data=cursor.fetchall()
    for i in data:
        print('\n'*2)
        print("Q"+str(i[0])+'.')
        print('PROPERTIES','\n',i[1])
        print()
        print("(a)",i[2])
        print("(b)",i[3])
        print("(c)",i[4])
        print("(d)",i[5])
        g=input("ENTER YOUR OPTION(a/b/c/d): ")
        print(data,i,sep='\n')
        if i[2]==i[6]:
            cg='a'
        elif i[3]==i[6]:
            cg='b'
        elif i[4]==i[6]:
            cg='c'
        elif i[5]==i[6]:
            cg='d'
        if g==cg:
            point+=2
        print()
        print('CORRECT ANSWER:',GREEN + i[6] + RESET)

def last():
    print()

#structuring the app

app='PERIODIC TABLE QUIZ'
c = shutil.get_terminal_size().columns
print(app.center(c))
print(('='*len(app)).center(c))
print()
name=input('ENTER YOUR NAME: ').upper()
while True:
    try:
        system('cls')
        point=0
        print(app.center(c))
        print(('='*len(app)).center(c))
        print()
        print('HI',name+',','WELCOME TO THE PERIODIC TABLE QUIZ')
        print()
        print('1. Quiz','2. Match The Following','3. Guess The Element','4. <to be added>','5. exit',sep='\n')
        a=int(input('ENTER YOUR CHOICE NUMBER(1/2/3/4/5): '))
        if a==1:
            quiz()
        elif a==2:
            matchf()
        elif a==3:
            guess()
        elif a==4:
            last()
        elif a==5:
            print('THANK YOU',name)
            print('BYE👋👋')
            break
        else:
            print('PLEASE ENTER A VALID CHOICE')
        print()
        print("CONGRAGULATIONS",name+',',"YOU HAVE SECURED",str(point)+'/10',"POINTS")
        print('\n'*3)
        if input('DO YOU WANT TO CONTINUE?(y/n); ')=='n':
            print('THANK YOU',name)
            print('BYE👋👋')
            break
    except:
        print('SOME ERROR OCCURED PLEASE RETRY!!!')
        sleep(5)
        sys.exit()