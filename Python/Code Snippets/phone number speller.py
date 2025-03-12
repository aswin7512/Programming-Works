#program to write phone number in words
numbers={
    '0' : "Zero",
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four",
    '5' : "Five",
    '6' : "Six",
    '7' : "Seven",
    '8' : "Eight",
    '9' : "Nine"
}

phone_no = input("ENTER YOUR PHONE NUMBER: ")

for i in phone_no:
    print(numbers.get(i,''), end = ' ')