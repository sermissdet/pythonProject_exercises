
#the setdefault() method, which returns the value of a specified key. If the key does not exist,
# it inserts the key with a default value

countries = {"USA": "Washington", "France": "Paris"}
countries.setdefault("Japan", "Tokyo")  # Adds 'Japan' with default value if it doesn't exist
print(countries)
