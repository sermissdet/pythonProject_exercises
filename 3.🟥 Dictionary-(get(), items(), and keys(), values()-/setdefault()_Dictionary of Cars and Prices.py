


#the setdefault() method, which returns the value of a specified key. If the key does not exist,
# it inserts the key with a default value

cars = {"Toyota": 30000, "BMW": 55000}
cars.setdefault("Tesla", 70000)  # Adds 'Tesla' with a default value if it doesn't exist
print(cars)
