def countlines():
    a=open("story.txt")
    b=a.readlines()
    c=0
    for i in b:
        if i[0].lower()=='a':
            c+=1
    print("NO. of lines starting with 'A'=",c)
countlines()