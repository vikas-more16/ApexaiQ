"""  Library System with Classes: Book, Member, Library

library system :
-- Book class: Stores title and availability.
-- Member class: Can borrow or return books. Keeps track of borrowed books.
-- Library class: Stores books, tracks which are available and borrowed."""

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
