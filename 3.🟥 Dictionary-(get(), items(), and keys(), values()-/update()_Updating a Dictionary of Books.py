
#the update() method, which updates a dictionary with items from another dictionary

books = {"1984": "George Orwell", "Brave New World": "Aldous Huxley"}
new_books = {"Fahrenheit 451": "Ray Bradbury", "Dune": "Frank Herbert"}
books.update(new_books)
print(books)
