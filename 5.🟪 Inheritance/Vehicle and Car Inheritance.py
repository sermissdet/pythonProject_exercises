
#Car inherits from Vehicle.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):  # Car inherits from Vehicle
    def info(self):
        print(f"Car: {self.make} {self.model}")

# Creating instances
vehicle = Vehicle("Generic Make", "Generic Model")
car = Car("Toyota", "Corolla")

vehicle.info()  # Output: Vehicle: Generic Make Generic Model
car.info()      # Output: Car: Toyota Corolla
