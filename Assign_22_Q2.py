

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius
    
# Creating an object of Circle class

obj1 = Circle(5)

# Calling methods
print("Area of circle with radius 5 is: ", obj1.area())
print("Circumference of circle with radius 5 is: ", obj1.circumference())