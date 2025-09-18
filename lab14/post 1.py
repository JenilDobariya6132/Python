import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    c1 = Circle(5) # radius is positive
    print(f"Radius: {c1.radius}")
    print(f"Area: {c1.area()}")
    print(f"Perimeter: {c1.perimeter()}")
    c2 = Circle(0) # radius is zero 
    print(f"Radius: {c2.radius}")
    print(f"Area: {c2.area()}")
    print(f"Perimeter: {c2.perimeter()}")
    c3 = Circle(-3) # radius is negative
    print(f"Radius: {c3.radius}")
    print(f"Area: {c3.area()}")
    print(f"Perimeter: {c3.perimeter()}")
