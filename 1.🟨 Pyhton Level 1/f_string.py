
"""
f-string (formatted string). F-strings allow you to insert the values of variables
and expressions directly inside a string.

How it works:
The f tells Python that you want to format the string.
Inside the string, you can use curly braces {} to insert variables or expressions that will be
replaced with their actual values.
"""

name = "Alice"
age = 5

# Using f-string
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

"""
Step-by-Step:
f before the string: This tells Python to look for variables inside the curly braces {} and replace 
them with their values.
{name} and {age}: Inside the string, {name} gets replaced with the value of the variable name (which is "Alice"),
and {age} gets replaced with 5.
Final String: The resulting string becomes "Hello, my name is Alice and I am 5 years old."
"""