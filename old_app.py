import sqlite3

def create_library_database():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Create the 'books' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            ID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER NOT NULL,
            book_type INTEGER NOT NULL CHECK (book_type IN (1, 2, 3))
        )
    """)

    # Create the 'customers' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            ID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    # Create the 'loans' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            CustID INTEGER NOT NULL,
            BookID INTEGER NOT NULL,
            loan_date DATE NOT NULL,
            return_date DATE NOT NULL,
            FOREIGN KEY (CustID) REFERENCES customers (ID),
            FOREIGN KEY (BookID) REFERENCES books (ID)
        )
    """)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_library_database()
