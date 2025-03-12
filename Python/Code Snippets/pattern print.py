import time
i=0
while(True):
    i+=1
    for j in range(1,i+1):
        print(j,end=' ')
    time.sleep(1)
    print('\n')