#the setdefault() method, which returns the value of a specified key. If the key does not exist,
# it inserts the key with a default value

products = {"apple": 2, "banana": 5}
products.setdefault("orange", 3)  # Adds 'orange' with default value if it doesn't exist
print(products)
