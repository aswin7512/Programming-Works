#class_Person
from datetime import date, datetime
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    
    def introduce(self):
        print(f"MY NAME IS {self.name.upper()}.")
        print(f"I AM {self.age} YEATS OLD.")
        print(f"I'M {self.gender}.")
    
    
    def birthday(self, bdate, bmonth):
        today = datetime.today()
        month = today.month
        if month < bmonth:
            year = today.year
        else:
            year = today.year + 1
        birthdate = f"{year}-{bmonth}-{bdate}"
        birthdate_format = "%Y-%m-%d"
        datetime_obj = datetime.strptime(birthdate, birthdate_format)
        time_left = datetime_obj - today
        print(f"{time_left} left for your next birthday")
        

p1 = Person(name = input("ENTER YOUR NAME: "),
            age = int(input("ENTER YOUR AGE: ")),
            gender = input("ENTER YOUR GENDER: "))

p1.introduce()

p1.birthday(bdate = int(input("ENTER YOUR BIRTH DATE: ")),
            bmonth = int(input("ENTER YOUR BIRTH MONTH IN NUMBER: ")))
