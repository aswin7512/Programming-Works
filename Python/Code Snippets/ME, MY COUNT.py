def count():
    a=open("poem.txt")
    b=a.read()
    c=b.split()
    me,my=0,0
    for i in c:
        if i.lower()=='me':
            me+=1
        elif i.lower()=='my':
            my+=1
    print("NO. of 'ME':",me,"NO. of'MY':",my,sep='\n')