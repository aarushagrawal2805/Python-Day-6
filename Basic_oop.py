#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self,max_speed,mileage): #Instance Atrributes
        self.max_speed=max_speed
        self.mileage=mileage
    
    def Display(self):
        print(" Max Speed is :",self.max_speed,"km/h","\nMileage is :",self.mileage,"km/h")

v1= Vehicle(200,15) # Parameters
v1.Display()