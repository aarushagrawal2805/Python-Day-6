#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    Name="Abc School"
    def __init__(self, type, max_speed, mileage,brand):
        self.type = type
        self.max_speed = max_speed
        self.mileage = mileage
        self.brand=brand

class Bus(Vehicle):

    def Display(self):
        print("Bus Brand is:",self.brand,"\nBus Type is:",self.type,"\nBus Max Speed is :",self.max_speed,"km/h","\nBus Mileage is:",self.mileage,"km/h")

print("--------School Bus Details--------")
v1=Bus("School Bus",100,10,"Eicher")
print(Vehicle.Name)
v1.Display()