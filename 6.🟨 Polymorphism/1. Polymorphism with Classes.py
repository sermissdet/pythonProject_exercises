
"""
Polymorphism allows objects of different classes to be treated as objects of a
common parent class, even though they may implement their methods differently.
Here, both the Dog and Cat classes have a sound method, but they implement it differently.
The animal_sound function can take any object (dog or cat) and call their respective sound method
"""

class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Polymorphism in action
def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
