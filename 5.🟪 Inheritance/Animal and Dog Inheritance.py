

#inheritance in Python, which allows a class to inherit attributes and methods from another class.
#Dog inherits from Animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print(f"{self.name} says woof!")

# Creating instances
animal = Animal("Generic Animal")
dog = Dog("Buddy")

animal.speak()  # Output: Generic Animal makes a sound.
dog.speak()     # Output: Buddy says woof!
