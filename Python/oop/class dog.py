#program to create a python_class Dog with attributes name, age, proce and species

class Dog:
  def __init__(self,name, age, price, species):
    self.name = name
    self.age = age
    self.price = price
    self.species=species

  
  def details(self):
    print(f"NAME: {self.name}\nAGE: {self.age}\nPRICE: {self.price}\nSPECIES: {self.species}")


jacky = Dog(name = input("ENTER NAME OF YOUR DOG: "),
            age = int(input("ENTER AGE OF YOUR DOG: ")),
            price = int(input("ENTER PRICE OF YOUR DOG: ")),
            species = input("ENTER THE SPECIES OF YOUR DOG: "))


jacky.details()