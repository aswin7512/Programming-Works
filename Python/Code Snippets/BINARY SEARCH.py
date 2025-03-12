def search(l,s):
    start=0
    end=len(l)-1
    while start<=end:
        m=(start+end)//2
        if l[m]==s:
            print(s,"found at",m+1,"th position after sorting")
            return l
        elif l[m]<s:
            start=m+1
        elif l[m]>s:
            end=m-1
        
    else:
        print("SORRY!",s,"NOT FOUND")
        return l

l=eval(input("ENTER THE LIST: "))
item=int(input("ENTER THE ITEM TO SEARCH: "))
list=sorted(l)
search(list,item)