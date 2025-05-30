from models.books import Book
from models.authors import Author
from models.borrowers import Borrower
from models.borrowing import Borrowing


def exit_program():
    print("Goodbye!")
    exit()

from models.books import Book
from models.authors import Author

def add_book():
    name = input("Enter book title: ")
    author_name = input("Enter the author's name: ")

    author = Author.find_by_name(author_name)
    if not author:
        author = Author(name=author_name)
        author.save()

    book = Book(name=name, author_id=author.id)
    book.save()
    print(f"Book '{name}' by {author_name} added successfully.")


def list_books():
    print("All Books:")
    books = Book.all()
    if not books:
        print("No books in the library.")
    for book in books:
        print(book)

def add_borrower():
    name = input("Enter borrower's name: ")
    borrower = Borrower(name=name)
    borrower.save()
    print(f"Borrower '{borrower.name}' added successfully!")

def list_borrowers():
    print("All borrowers:")
    borrowers = Borrower.all()
    if not borrowers:
        print("No borrowers found.")
    for borrower in borrowers:
        print(borrower)

def borrow_book():
    borrower_name = input("Borrower name: ")
    book_name = input("Book name: ")

    borrower = Borrower.find_by_name(borrower_name)
    book = Book.find_by_name(book_name)

    if borrower and book:
        Borrowing.borrow(book.id, borrower.id)
        print(f"{book.name} borrowed by {borrower.name}")
    else:
        print("Borrower or Book not found in the database.")

def list_borrowed():
    print("Borrowed Books:")
    borrowed = Borrowing.borrowed_books()
    if not borrowed:
        print("No books currently borrowed.")
    for book_name, borrower_name in borrowed:
        print(f"{book_name} borrowed by {borrower_name}")
