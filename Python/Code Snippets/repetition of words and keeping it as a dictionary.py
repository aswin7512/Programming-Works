str=input("enter a word or sentence")
dic={}
for i in str:
    if i not in dic:
        dic[i]=str.count(i)
print(dic)