"""
Library Management System

This program defines a simple library system with classes for Book, Member, and Library.
Members can borrow and return books, and the library keeps track of available and borrowed books.
"""

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        is_borrowed (bool): Indicates whether the book is currently borrowed.
    """

    def __init__(self, title):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
        """
        self.title = title
        self.is_borrowed = False


class Member:
    """
    Represents a library member who can borrow and return books.

    Attributes:
        name (str): The name of the member.
        borrowed_books (list of Book): List of books currently borrowed by the member.
    """

    def __init__(self, name):
        """
        Initializes a new Member instance.

        Args:
            name (str): The name of the member.
        """
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Allows the member to borrow a book if it is available.

        Args:
            book (Book): The book to borrow.

        Prints:
            A message indicating whether the book was successfully borrowed
            or if it is already borrowed.
        """
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        """
        Allows the member to return a book they have borrowed.

        Args:
            book (Book): The book to return.

        Prints:
            A message indicating whether the book was successfully returned
            or if the member did not borrow it.
        """
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")


class Library:
    """
    Represents a library that manages a collection of books.

    Attributes:
        books (list of Book): List of all books in the library.
    """

    def __init__(self):
        """Initializes a new Library instance with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """
        Adds a new book to the library's collection.

        Args:
            book (Book): The book to add.
        """
        self.books.append(book)

    def available_books(self):
        """
        Returns a list of titles of books that are not currently borrowed.

        Returns:
            list of str: Titles of available books.

        Prints:
            The list of available books.
        """
        available = [book.title for book in self.books if not book.is_borrowed]
        print("Available books:", available)
        return available

    def borrowed_books(self):
        """
        Returns a list of titles of books that are currently borrowed.

        Returns:
            list of str: Titles of borrowed books.

        Prints:
            The list of borrowed books.
        """
        borrowed = [book.title for book in self.books if book.is_borrowed]
        print("Borrowed books:", borrowed)
        return borrowed


# Example Usage
if __name__ == "__main__":
    lib = Library()
    b1 = Book("Python Programming")
    b2 = Book("Data Structures")
    lib.add_book(b1)
    lib.add_book(b2)

    member = Member("Vikas")
    lib.available_books()
    member.borrow_book(b1)
    lib.available_books()
    member.return_book(b1)
    lib.available_books()
