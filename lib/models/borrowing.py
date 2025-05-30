from models import CURSOR, CONN

class Borrowing:
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY,
                book_id INTEGER,
                borrower_id INTEGER,
                FOREIGN KEY(book_id) REFERENCES books(id),
                FOREIGN KEY(borrower_id) REFERENCES borrower(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def borrow(cls, book_id, borrower_id):
        CURSOR.execute(
            "INSERT INTO borrowings (book_id, borrower_id) VALUES (?, ?)",
            (book_id, borrower_id)
        )
        CONN.commit()

    @classmethod
    def borrowed_books(cls):
        sql = """
            SELECT books.name, borrowers.name
            FROM borrowings
            JOIN books ON borrowings.book_id = books.id
            JOIN borrowers ON borrowings.borrower_id = borrowers.id;
        """
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM borrowings")
        return CURSOR.fetchall()