#program to print the following pattern
"""
1
2 3
4 5 6
.......
"""

no_of_lines = int(input("ENTER NO. OF LINES: "))        #input no. of lines from user

#printing the pattern....
number = 1
for i in range(no_of_lines):
    
    for j in range(i+1):
        
        print("%5s" %number, end=' ')
        number += 1
        
    print()
