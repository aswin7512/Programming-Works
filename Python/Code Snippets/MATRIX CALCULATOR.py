import pickle
import numpy as np
import os

def add(m,n):
    l1,l2,l3,l4,l5,l6,l7,l8,l9=[],[],[],[],[],[],[],[],[]
    print('',"ENTER ELEMENTS OF FIRST MATRIX",'',sep='\n')
    for i in range(1,m+1):
        for j in range(1,n+1):
            ele='a'+str((i*10)+j)+' : '
            a=float(input(ele))
            l1.append(a)
    print()
    print("ENTER ELEMENTS OF SECOND MATRIX")
    print()
    for i in range(1,m+1):
        for j in range(1,n+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l2.append(a)
    for i in range(len(l1)):
        l3.append(l1[i]+l2[i])
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l4.append(l1[j])
        l5.append(l4)
        l4=[]
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l6.append(l2[j])
        l7.append(l6)
        l6=[]
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l8.append(l3[j])
        l9.append(l8)
        l8=[]
    lis=[l5,'+',l7,'=',l9]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return l9

def sub(m,n):
    l1,l2,l3,l4,l5,l6,l7,l8,l9=[],[],[],[],[],[],[],[],[]
    print()
    print("ENTER ELEMENTS OF FIRST MATRIX")
    print()
    for i in range(1,m+1):
        for j in range(1,n+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l1.append(a)
    print()
    print("ENTER ELEMENTS OF SECOND MATRIX")
    print()
    for i in range(1,m+1):
        for j in range(1,n+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l2.append(a)
    for i in range(len(l1)):
        l3.append(l1[i]-l2[i])
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l4.append(l1[j])
        l5.append(l4)
        l4=[]
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l6.append(l2[j])
        l7.append(l6)
        l6=[]
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l8.append(l3[j])
        l9.append(l8)
        l8=[]
    lis=[l5,'-',l7,'=',l9]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return l9

def smul(m,n):
    l1,l2,l3,l4,l5=[],[],[],[],[]
    print()
    print("ENTER ELEMENTS OF MATRIX")
    print()
    for i in range(1,m+1):
        for j in range(1,n+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l1.append(a)
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l4.append(l1[j])
        l5.append(l4)
        l4=[]
    b=float(input("ENTER THE SCALAR VALUE: "))
    for i in range(len(l1)):
        l1[i]*=b
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l2.append(l1[j])
        l3.append(l2)
        l2=[]
    lis=[l5,'×',[b],'=',l3]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return l3

def mul(n1,m1,n2,m2):
    l1,l2,l3,l4,l5,l6,l7,l8,l9=[],[],[],[],[],[],[],[],[]
    print()
    print("ENTER ELEMENTS OF FIRST MATRIX")
    print()
    for i in range(1,n1+1):
        for j in range(1,m1+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l1.append(a)
    print()
    print("ENTER ELEMENTS OF SECOND MATRIX")
    print()
    for i in range(1,n2+1):
        for j in range(1,m2+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l2.append(a)
    for i in range(0,len(l1),m1):
        for j in range(i,m1+i):
            l3.append(l1[j])
        l5.append(l3)
        l3=[]
    for i in range(0,len(l2),m2):
        for j in range(i,m2+i):
            l4.append(l2[j])
        l6.append(l4)
        l4=[]
    for i in range(n1):
        for j in range(m2):
            l7.append(0)
    for i in range(0,len(l7),m2):
        for j in range(i,m2+i):
            l8.append(l7[j])
        l9.append(l8)
        l8=[]
    for i in range(len(l5)):
        for j in range(len(l6[0])):
            for k in range(len(l6)):
                l9[i][j]+=(l5[i][k]*l6[k][j])
    lis=[l5,'×',l6,'=',l9]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return l9

def deter(l6):
    l7,l8,l9=[],[],[]
    if len(l6)==3:
        print(l6)
        for j in range(len(l6)):
            n=0
            for k in range(len(l6)):
                for l in range(len(l6)):
                    if k!=0 and l!=j:
                        c=l6[0][j]
                        print(k,l)
                        l7.append(l6[k][l])
                if l7!=[]:
                    l8.append(l7)
                    l7=[]
            if len(l8)!=2:
                g=deter(l8)
                h=0
            else:
                h=0
                g=c*((l8[0][0]*l8[1][1])-(l8[0][1]*l8[1][0]))
            if j%2!=0:
                g*=(-1)
            l9.append(g)
            l8=[]
        for i in l9:
            h+=i
        l9=[]
        n+=h
    elif len(l6)==1:
        n=l6[0]
    elif len(l6)>3:
        mat=np.array(l5) 
        n=round(np.linalg.det(mat))
    else:
        n=((l6[0][0]*l6[1][1])-(l6[0][1]*l6[1][0]))
        
    lis=["DETERMINANT OF",l6,"=",[n]]
    with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
    return n

def adj(m):
    l1,l2,l3,l4,l5,l6,l7,l8,l9=[],[],[],[],[],[],[],[],[]
    print()
    print("ENTER ELEMENTS OF MATRIX")
    print()
    for i in range(1,m+1):
        for j in range(1,m+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l1.append(a)
    print()
    for i in range(0,len(l1),m):
        for j in range(i,m+i):
            l2.append(l1[j])
        l3.append(l2)
        l2=[]
    
    for i in range(m):
        for j in range(m):
            for k in range(m):
                for l in range(m):
                    if k!=i and l!=j:
                        l4.append(l3[k][l])
                if l4!=[]:
                    l5.append(l4)
                    l4=[]            
            d=deter(l5)
            l5=[]
            l6.append(d)
        l7.append(l6)
        l6=[]
    for i in range(len(l7)):
        for j in range(len(l7[i])):
            if (i+j)%2!=0:
                l7[i][j]*=-1
    for i in range(len(l7)):
        for j in range(len(l7[i])):
            l8.append(round(l7[j][i]))
        l9.append(l8)
        l8=[]
    
    lis=["ADJOINT OF",l3,"=",l9]
    with open ("history.dat",'ab') as f:
        pickle.dump(lis,f)
    return l3,l9

def inverse(m):
    ad,aj=adj(m)
    d=deter(ad)
    if d==0:
        print("INVERSE DOESNOT EXISTS")
    else:
        for i in range(len(aj)):
            for j in range(len(aj[i])):
                aj[i][j]/=d
        lis=["INVERSE OF",ad,"=",aj]
        with open ("history.dat",'ab') as f:
            pickle.dump(lis,f)
        return aj

def trans(m,n):
    l1,l2,l3,l4,l5,l6,=[],[],[],[],[],[]
    print()
    print("ENTER ELEMENTS OF MATRIX")
    print()
    for i in range(1,m+1):
        for j in range(1,n+1):
            el=(i*10)+j
            elm='a'+str(el)
            ele=elm+' : '
            a=float(input(ele))
            l1.append(a)
    for i in range(0,len(l1),n):
        for j in range(i,n+i):
            l2.append(l1[j])
        l3.append(l2)
        l2=[]
    
    for i in range(len(l3[0])):
        for j in range(len(l3)):
            l4.append(l3[j][i])
    
    for i in range(0,len(l4),m):
        for j in range(i,m+i):
            l5.append(l4[j])
        l6.append(l5)
        l5=[]
    
    lis=["TRANSPOSE OF",l3,"=",l6]
    with open ("history.dat",'ab') as f:
        pickle.dump(lis,f)
    return l6

def history():
    with open('history.dat','rb') as f:
        fl=True
        no=1
        
        while True:
            try:
                a=pickle.load(f)
                print('\t'+str(no)+',','',sep='\n')
                no+=1
                fl=False
                if a[1]=='+' or a[1]=='-' or a[1]=='×':
                    for i in a:
                        for j in i:
                            print('\t',j)
                    print('\t ===========================','','',sep='\n')
                    
                elif a[0]=="DETERMINANT OF":
                    print('\t',a[0])
                    print()
                    for i in a[1]:
                        print('\t',i)
                    print()
                    print('\t',a[2],a[3])
                    print('\t ===========================','','',sep='\n')
                    
                elif a[0]=="INVERSE OF" or a[0]=="TRANSPOSE OF" or a[0]=="ADJOINT OF":
                    print('\t',a[0])
                    print()
                    for i in a[1]:
                        print('\t',i)
                    print('\t',a[2])
                    for i in a[3]:
                        print('\t',i)
                    print('\t ===========================','','',sep='\n')
            except EOFError:
                print()
                print()
                if fl==False:
                    print("NO FURTHER DATA AVAILABLE!!!")
                else:
                    print("NO HISTORY AVAILABLE")
                print()
                print()
                return fl
                break                

def clr():
    f=open('history.dat','wb')
    f.close()
    print("HISTORY SUCCESSFULLY CLEARED!!!")

while True:
    try:
        os.system("clear")
        print('\t'*5,"MATRIX CACULATOR")
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''",'','',sep='\n')
        print('\n'*2)
        print("OPERATIONS ON MATRICES")
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        
        print("1, ADDITION OF 2 MATRICES","2, SUBSTRACTION OF 2 MATRICES","3, SCALAR MULTIPLICATION OF MATRICES","4, MULTIPLICATION OF 2 MATRICES","5, DETERMINANT CALCULATION","6, ADJOINT OF A MATRIX","7, INVERSE OF A MATRIX","8, TRANSPOSE OF A MATRIX","9, HISTORY","10, EXIT",sep="\n")

        print()
        a=int(input("ENTER YOUR CHOICE(1/2/3/4/5/6/7/8/9/10): "))
        print()
    
        if a==1:
            b=int(input("ENTER THE NO. OF ROWS: "))
            c=int(input("ENTER THE NO. OF COLUMNS:"))
            if b==0 or c== 0:
                print("ENTER VALID ORDER")
            else:
                d=add(b,c)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                for i in d:
                    print(i)
                print('\n'*3)
        elif a==2:
            e=int(input("ENTER THE NO. OF ROWS: "))
            f=int(input("ENTER THE NO. OF COLUMNS:"))
            if e==0 or f== 0:
                print("ENTER VALID ORDER")
            else:
                g=sub(e,f)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                for i in g:
                    print(i)
                print('\n'*3)
                    
        elif a==3:
            e=int(input("ENTER THE NO. OF ROWS: "))
            f=int(input("ENTER THE NO. OF COLUMNS:"))
            if e==0 or f== 0:
                print("ENTER VALID ORDER")
            else:
                g=smul(e,f)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                for i in g:
                    print(i)
                print('\n'*3)
                    
        elif a==4:
            e=int(input("ENTER THE NO. OF ROWS OF FIRST MATRIX: "))
            f=int(input("ENTER THE NO. OF COLUMNS OF FIRST MATRIX: "))
            g=int(input("ENTER THE NO. OF ROWS OF SECOND MATRIX: "))
            h=int(input("ENTER THE NO. OF COLUMNS OF SECOND MATRIX: "))
            if e==0 or f== 0 or g==0 or h==0:
                print("ENTER VALID ORDER")
            elif f!=g:
                print("NO. OF COLUMNS OF FIRST MATRIX SHULD BE EQUAL TO THE NUMBER OF ROWS OF SECOND MATRIX")
            else:
                I=mul(e,f,g,h)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                for i in I:
                    print(i)
                print('\n'*3)
                    
        elif a==5:
            e=int(input("ENTER THE NO. OF ROWS: "))
            if e==0:
                print("ENTER VALID ORDER")
            else:
                l1,l4,l5,d=[],[],[],0
                print()
                print("ENTER ELEMENTS OF MATRIX")
                print()
                for i in range(1,e+1):
                    for j in range(1,e+1):
                        el=(i*10)+j
                        elm='a'+str(el)
                        ele=elm+' : '
                        a=float(input(ele))
                        l1.append(a)
                for i in range(0,len(l1),e):
                    for j in range(i,e+i):
                        l4.append(l1[j])
                    l5.append(l4)
                    l4=[]
                m=deter(l5)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                print("determinant=",m)
                print('\n'*3)
        
        elif a==6:
            e=int(input("ENTER THE NO. OF ROWS: "))
            if e==0:
                print("ENTER A VALID ORDER")
                
            else:
                p,r=adj(e)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                for i in r:
                    print(i)
                print('\n'*3)
        
        elif a==7:
            e=int(input("ENTER THE NO. OF ROWS: "))
            if e==0:
                print("ENTER VALID ORDER")
            else:
                o=inverse(e)
                if type(o) == list:
                    print()
                    print("RESULT")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    print()
                    for i in o:
                        print(i)
                    print('\n'*3)
    
        elif a==8:
            e=int(input("ENTER THE NO. OF ROWS: "))
            f=int(input("ENTER THE NO. OF COLUMNS:"))
            if e==0 or f== 0:
                print("ENTER VALID ORDER")
            else:
                n=trans(e,f)
                print()
                print("RESULT")
                print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                print()
                for i in n:
                    print(i)
                print('\n'*3)
    
        elif a==9:
            print()
            print("RESULT")
            print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            print()
            fl=history()
            print('\n'*3)
            
            if fl==False:
                if input("DO YOU WANT TO CLEAR HISTORY?(y/n): ").lower()=='y':
                    clr()
            
        elif a==10:
            break
        
        else:
            print()
            print()
            print("ENTER A VALID CHOICE!!!")
            print('\n'*3)
        input("~~~PRESS ENTER TO CONTINUE~~~")
    
    except:
        print('\n'*3)
        print("~~~SOME ERROR OCCURED!!!~~~")
        print()
        input("~~~PRESS ENTER TO RESTART~~~")

    print('\n'*3)
print("APP DEVELOPED BY","ASWIN P","CLASS 12A 2k22-23 BATCH","KENDRIYA VIDYALAYA ADOOR","SHIFT 1","","THANK YOU",sep='\n')

input()