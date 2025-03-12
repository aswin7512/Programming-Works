#program to find the second smallest element of a list
l = eval(input("ENTER THE LIST: "))
if len(l) < 2 :
    print("ENTER A LIST OF MINIMUM LENGTH 2!!!")
else :
    smallest, second_smallest = l[0], l[1]
    if smallest > second_smallest:
        smallest, second_smallest = second_smallest, smallest
    for i in l[2::] :
        if i < smallest :
            smallest, second_smallest = i, smallest
        elif i < second_smallest :
            second_smallest = i
    print(f"Second Smallest: {second_smallest}")