#class_Car
class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    
    
    def accelerate(self, speed_to_accelerate):
        self.speed += speed_to_accelerate
        print(f"SPEED SUCCESSFULLY ACCELERATED TO {self.speed}KM/H...")
    
    
    def brake(self):
        self.speed = 0
        print("CAR IS STOPPED...")
    
    def get_speed(self):
        return self.speed


c1 = Car(make = input("ENTER MANUFACTURER OF THE CAR: "),
         model = input("ENTER MODEL OF THE CAR: "),
         year = int(input("ENTER YEAR OF MANUFACTURE: ")),
         speed = float(input("ENTER THE SPEED OF THE CAR: ")))

c1.accelerate(speed_to_accelerate = int(input("ENTER THE SPEED TO BE ACCELERATED: ")))

c1.brake()
c1.accelerate(80)
print(f"PRESENT SPEED OF CAR IS {c1.get_speed()}KM/H")