#program to make a python_class rectangle


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    
    def calculate_area(self):
        return self.width * self.height
    
    
    def calculate_perimeter(self):
        return 2 *(self.width + self.height)


rect=Rectangle(int(input("ENTER WIDTH: ")),
            int(input("ENTER HEIGHT: ")))

print(f"PERIMETER = {rect.calculate_perimeter()} units")
print(f"AREA = {rect.calculate_area()} sq. units")