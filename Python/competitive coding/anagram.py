s = input("ENTER STRING 1: ")
t = input("ENTER STRING 2: ")
anag = 1
sc = ""
for i in range(len(t)):
    if not(t[i] in s):
        anag = 0
        break
    for j in range(len(s)):
        if t[i] != s[j]:
            sc += s[j]
    s = sc
if anag:
    print(True)
else:
    print(False)