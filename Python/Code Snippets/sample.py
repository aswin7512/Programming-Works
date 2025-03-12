'''
a=open('story.txt','w')
b=['The Lion and The Mouse',' abcd',' fvuifvujhc',' hjcuiejciuidcj',' fveufvufvuy89',' hufvuhfve8u9f']
a.writelines(b)
a.close()

b=open('poem.txt','w')
b.write("Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth; Then took the my other, as just as fair, And having perhaps the better Me claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same, And both that morning equally lay In leaves no step had trodden black. Oh, I kept the first for another day! Yet knowing how way leads on to way, I doubted if I me should ever come back. I shall be telling this my with a sigh Somewhere my ages and ages hence: Two roads diverged in a wood, and I— I took the one my less traveled by, And that has made all the difference.")
b.close()

import pickle
f=open("student.dat",'wb')
ans='y'
while ans.lower()=='y':
    ano=int(input("ENTER THE ADMISSION NO.: "))
    nam=input("ENTER NAME: ")
    pr=int(input("ENTER MARK%: "))
    x=[ano,nam,pr]
    pickle.dump(x,f)
    ans=input("continue?(y/n)")
f.close()'''

'''f=open('abcd.txt','w')
a='y'
l=[]
while a.lower()=='y':
    b=input('enter the line: ')
    l.append(b)
    l.append('\n')
    a=input('continue?(y/n)')
f.writelines(l)
f.close()'''

import csv
a=open("emp.csv",'a')
b=csv.writer(a)
c=input("ihdf")
d=input("dfji")
e=input("ijogio")
f=[c,d,e]
b.writerow(f)
a.close()