from models import CURSOR, CONN

class Borrower:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Borrower {self.id}: {self.name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS borrowers (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO borrowers (name) VALUES (?)", (self.name,))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE borrowers SET name = ? WHERE id = ?", (self.name, self.id))
        CONN.commit()

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM borrowers WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM borrowers WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        return None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM borrowers")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1]) for row in rows]