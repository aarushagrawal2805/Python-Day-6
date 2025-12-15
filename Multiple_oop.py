#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle: #Parent Class
    Color="White"
    def __init__(self, type, max_speed, mileage,brand):
        self.type = type
        self.max_speed = max_speed
        self.mileage = mileage
        self.brand=brand
    
    def Display(self):
        print("Color :",Vehicle.Color,"\nBus Brand is:",self.brand,"\nBus Type is:",self.type,"\nBus Max Speed is :",self.max_speed,"km/h","\nBus Mileage is:",self.mileage,"km/h")

class Bus(Vehicle): #1 Child Class
    pass
    

class Van(Vehicle): #2Child Class
    pass

print("--------School Vehicle Details--------\n")
v1=Van("School Bus",100,10,"Eicher")
v2=Van("School Van",50,10,"Maruti")

print("----------Vehicle 1 Information----------\n")
v1.Display()
print("----------Vehicle 2 Information----------\n")
v2.Display()