n = int(input("ENTER A NUMBER: "))
nc = n
da, db = [], []
l = (1000, 500, 100, 50, 10, 5, 1)
rn = ("M", "D", "C", "L", "X", "V", "I")
for i in range(len(l)):
    if n != 0:
        if n // l[i] != 0:
            val = lambda x: x if x != 4 else -1
            da.append(rn[i])
            db.append(val(n // l[i]))
            if db[-1] == -1:
                da.append(rn[i-1])
                db.append(1)
            n = n %(l[i]*(n // l[i]))
        else:
            for j in range(0, len(l), 2):
                if l[j] > n:
                    cl = l[j]
                    ind = j
            if (n + cl)// l[i] >= 0:
                da.append(rn[ind+2])
                da.append(rn[ind])
                db += [1, 1]
                n = n // l[i]
                    
    else:
        break
rm = ""
for i in range(len(da)):
    if db[i] != -1:
        rm += (da[i]*db[i])
    else:
        rm += da[i]

print(rm)