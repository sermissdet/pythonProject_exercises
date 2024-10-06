
"""
In Python, self is a conventionally used parameter name in instance methods of a class.
It refers to the specific instance of the class that is being created or manipulated.
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Assign the name to the instance
        self.breed = breed  # Assign the breed to the instance

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Accessing methods and attributes
my_dog.bark()  # Output: Buddy says woof!
print(my_dog.breed)  # Output: Golden Retriever
