#program to find the combination elements in a list which sums up to target
l = eval(input("ENTER A LIST OF NUMBERS: "))
t = int(input("ENTER TAGRET: "))
ld = {}
combo = []
for i in range(len(l)):
    ele = t - l[i]
    ld[l[i]] = ele, i

for i in ld:
    if (i in l) and ld[i][0] in l:
        index1 = l.index(ld[i][0])
        l.remove(i)
        index2 = ld[i][1]
        combo = [index1, index2]
        break
print(combo)