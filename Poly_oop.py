class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Overriding the area method
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # Overriding the area method
        return self.side * self.side

shapes = Circle(5)
print("Area of Circle is :",shapes.area()) 
shapes = Square(5)
print("Area of Sqaure is :",shapes.area())