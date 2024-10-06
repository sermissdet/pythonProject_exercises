"""
Both Rectangle and Circle inherit from Shape and provide their own implementation of the area method. The same method
 call (area()) behaves differently based on the object type.
"""

class Shape:
    def area(self):
        pass  # Placeholder for subclasses to define

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(f"The area is: {shape.area()}")
