#Manager inherits from Employee.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_info(self):
        print(f"{self.name} works as a {self.position}.")

class Manager(Employee):  # Manager inherits from Employee
    def show_info(self):
        print(f"{self.name} is a manager.")

# Creating instances
employee = Employee("Alice", "Developer")
manager = Manager("Bob", "Manager")

employee.show_info()  # Output: Alice works as a Developer.
manager.show_info()   # Output: Bob is a manager.
