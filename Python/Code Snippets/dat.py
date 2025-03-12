import pickle
st=open('student.dat','rb')
while True:
    try:
        x=pickle.load(st)
        print('%10s'%x['r'],'%20s'%x['n'],'%20s'%x['m'],'%')
    except EOFError:
        break