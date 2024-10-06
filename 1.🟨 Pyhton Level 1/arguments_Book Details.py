def book_info(title, author, year_published=2020):
    '''This function prints details of a book.'''
    print("The book '{}' is written by {} and was published in {}.".format(title, author, year_published))

# Example usage# Output: The book 'The Great Gatsby' is written by F. Scott Fitzgerald and was published in 1925.
book_info("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# Output: The book 'The Great Gatsby' is written by F. Scott Fitzgerald and was published in 1925.

book_info("The Catcher in the Rye", "J.D. Salinger")
