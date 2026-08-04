# Create a Circle class to find area and circumference.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14159 * self.radius

circle1 = Circle(5)
print("Area of the circle:", circle1.area())
print("Circumference of the circle:", circle1.circumference())



