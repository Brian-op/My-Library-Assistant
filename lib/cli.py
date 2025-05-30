from models import CURSOR, CONN
from models.books import Book
from models.authors import Author
from models.borrowers import Borrower
from models.borrowing import Borrowing

def tables():
    Book.create_table()
    Author.create_table()
    Borrower.create_table()
    Borrowing.create_table()

from helpers import (
    exit_program,
    add_book,
    list_books,
    add_Borrower,
    borrow_book,
    list_borrowed,
    list_Borrowers
)

def main():
    tables()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
             add_Borrower()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
             list_Borrowers()
        elif choice == "6":
             list_borrowed()
        
        else:
            print("Invalid choice")

def menu():
    print("Pick any of the following:")
    print("0. Leave the program")
    print("1. Add A Book")
    print("2. List of All Books")
    print("3. Add a Borrower")
    print("4. Borrow Book")
    print("5. List of All Borrowers")
    print("6. List of Borrowed Books")
    

if __name__ == "__main__":
    main()
