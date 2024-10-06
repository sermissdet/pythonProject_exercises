
def add(a, b):
    return a + b

# Polymorphism in action
print(add(2, 3))           # Output: 5 (integer addition)
print(add("Hello, ", "World!"))  # Output: Hello, World! (string concatenation)


"""
The add function works for both integers and strings, even though the operation (+) behaves differently. This is an
example of function polymorphism.
Summary:
First Example: Shows polymorphism with different classes having the same method name (sound), but different
implementations.
Second Example: Shows polymorphism through inheritance, where subclasses of Shape define their own version of the area
method.
Third Example: Demonstrates function polymorphism where the same function works with different types of data (integers
and strings).
"""