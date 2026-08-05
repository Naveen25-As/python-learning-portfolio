# Hierarchical Inheritance – Shape → Circle, Rectangle.

class Shape:
    def message(self):
        print("This is a shape.")
        
class Circle(Shape):
    def area(self, radius):
        print("Area of a Circle : ", 3.14 * radius * radius)
        
class Rectangle(Shape):
    def area(self, length, width):
        print("Area of a Rectangle : ", length * width)

circle = Circle()
circle.message()
circle.area(5)

print()

rectangle = Rectangle()
rectangle.message()
rectangle.area(4, 6)