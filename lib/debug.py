from models import CONN
from models.books import Book
from models.authors import Author
from models.borrowers import Borrower
from models.borrowing import Borrowing

CURSOR = CONN.cursor()
CURSOR.execute("DROP TABLE IF EXISTS borrowings")
CURSOR.execute("DROP TABLE IF EXISTS books")
CURSOR.execute("DROP TABLE IF EXISTS borrowers")
CURSOR.execute("DROP TABLE IF EXISTS authors")
CONN.commit()

Author.create_table()
Book.create_table()
Borrower.create_table()
Borrowing.create_table()

authors = [
    Author(name="Robert Greene"),
    Author(name="Paulo Coelho"),
    Author(name="Markus Zusak"),
    Author(name=" Delia Owens")
]
for author in authors:
    author.save()

books = [
    Book(name="The 48 Laws of Power", author_id=authors[0].id),
    Book(name="The Alchemist", author_id=authors[1].id),
    Book(name="The Midnight Library ", author_id=authors[1].id),
    Book(name="Dune", author_id=authors[2].id),
    Book(name="Educated ", author_id=authors[3].id),
    Book(name="The Silent Patient ", author_id=authors[2].id)
]
for book in books:
    book.save()

borrowers = [
    Borrower(name="Bruise Wayne"),
    Borrower(name="Kendrik"),
    Borrower(name="Diddy")
]
for borrower in borrowers:
    borrower.save()

Borrowing.borrow(books[0].id, borrowers[0].id)  
Borrowing.borrow(books[1].id, borrowers[0].id)  
Borrowing.borrow(books[2].id, borrowers[1].id)  
Borrowing.borrow(books[5].id, borrowers[1].id)  
Borrowing.borrow(books[4].id, borrowers[2].id)  
Borrowing.borrow(books[3].id, borrowers[2].id)

print(" Borrowed Books:")
borrowed = Borrowing.borrowed_books()
for book_title, borrower_name in borrowed:
    print(f"{book_title}:  Borrowed By : {borrower_name}")



