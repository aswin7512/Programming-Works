amt = int(input("ENTER AMOUNT: "))
div = {}
note = (500, 200, 100, 50, 20, 10, 5, 2, 1)
for i in note:
    j = 1
    while i * j <= amt:
        j += 1
    j -= 1
    if j != 0:
        div[i] = j
        amt -= i * j
    if amt == 0:
        break
tnotes = 0
for i in div.keys():
    print(f"Rs.{i} = {div[i]}")
    tnotes += div[i]
print(f"Total No. of Notes = {tnotes}")
