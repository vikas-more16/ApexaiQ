"""
Library Management System

This program defines a simple library system with classes for Book, Member, and Library.
Members can borrow and return books, and the library keeps track of available and borrowed books.

Classes:
- Book: Represents a book with a title and borrowed status.
- Member: Represents a library member who can borrow and return books.
- Library: Manages a collection of books and tracks availability.
"""

class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def available_books(self):
        available = [book.title for book in self.books if not book.is_borrowed]
        print("Available books:", available)
        return available

    def borrowed_books(self):
        borrowed = [book.title for book in self.books if book.is_borrowed]
        print("Borrowed books:", borrowed)
        return borrowed


# Example Usage
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
