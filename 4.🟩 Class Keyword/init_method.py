
"""
The __init__ method in Python is a special method known as a constructor.
It is automatically called when an instance (object) of the class is created.

"""

class Car:
    def __init__(self, make, model, year):
        self.make = make  # Initialize the make attribute
        self.model = model  # Initialize the model attribute
        self.year = year  # Initialize the year attribute

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)  # Output: 2020
