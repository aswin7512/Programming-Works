#program to print the following pattern
'''
A
BC
DEF
GHIJ
KLMNO
........'''

no_of_lines = int(input("ENTER NO. OF LINES: "))

#to count no. of characters required for the given no. of lines
no_of_characters = 0
for i in range(no_of_lines):
    no_of_characters += (i + 1)

#check whether the no. of lines is possilble to print or not
if no_of_characters <= 28:
    
    #printing the given pattern...
    present_character=65
    for i in range(no_of_lines):
        for j in range(i+1):
            if present_character >= 91:      #checking whether the character is <= "Z"...
                exit()
            
            print(f"{chr(present_character)}",end='')
            present_character += 1          #updating the character to print...
        print()
else:
    print("PLEASE ENTER A LESSER NO. OF LINES WHICH CAN BE LIMITED IN 26 CHARACTERS IN TOTAL")