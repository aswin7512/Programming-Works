def countrec():
    import pickle
    a=open("student.dat",'rb')
    c=0
    while True:
        try:
            l=pickle.load(a)
            if l[-1]>75:
                c+=1
                print(l)
        except EOFError:
            break
    print("NO. OF STUDENTS SCORED ABOVE 75% =",c)
countrec()