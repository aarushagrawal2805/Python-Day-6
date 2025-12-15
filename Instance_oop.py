class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

#built-in isinstance() function 
#It means to check is this object is of vehicle class or not
print(isinstance(School_bus, Vehicle))