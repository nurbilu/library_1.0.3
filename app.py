import sqlite3
from book import Book
from customer import Customer
from loan import Loan

class LibraryClient:
    def __init__(self, db_file="library.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def display_menu(self):
        while True:
            print("\nLibrary Management System Menu:")
            print("1. Add a new customer")
            print("2. Add a new book")
            print("3. Loan a book")
            print("4. Return a book")
            print("5. Display all books")
            print("6. Display all customers")
            print("7. Display all loans")
            print("8. Display late loans")
            print("9. Find book by name")
            print("10. Find customer by name")
            print("11. Remove book")
            print("12. Remove customer")
            print("0. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.loan_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.display_all_books()
            elif choice == "6":
                self.display_all_customers()
            elif choice == "7":
                self.display_all_loans()
            elif choice == "8":
                self.display_late_loans()
            elif choice == "9":
                self.find_book_by_name()
            elif choice == "10":
                self.find_customer_by_name()
            elif choice == "11":
                self.remove_book()
            elif choice == "12":
                self.remove_customer()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_customer(self):
        name = input("Enter customer name: ")
        city = input("Enter customer city: ")
        age = int(input("Enter customer age: "))

        # Insert the new customer into the 'customers' table
        self.cursor.execute("INSERT INTO customers (name, city, age) VALUES (?, ?, ?)", (name, city, age))
        self.conn.commit()

        print(f"Customer {name} added successfully!")

    def add_book(self):
        name = input("Enter book name: ")
        author = input("Enter book author: ")
        year_published = int(input("Enter year of publication: "))
        book_type = int(input("Enter book type (1/2/3): "))

        # Insert the new book into the 'books' table
        self.cursor.execute("INSERT INTO books (name, author, year_published, book_type) VALUES (?, ?, ?, ?)",
                            (name, author, year_published, book_type))
        self.conn.commit()

        print(f"Book {name} added successfully!")

    def loan_book(self):
        cust_id = int(input("Enter customer ID: "))
        book_id = int(input("Enter book ID: "))
        loan_date = input("Enter loan date (YYYY-MM-DD): ")
        return_date = input("Enter return date (YYYY-MM-DD): ")

        # Insert the new loan into the 'loans' table
        self.cursor.execute("INSERT INTO loans (CustID, BookID, loan_date, return_date) VALUES (?, ?, ?, ?)",
                            (cust_id, book_id, loan_date, return_date))
        self.conn.commit()

        print("Book loaned successfully!")

    def return_book(self):
        book_id = int(input("Enter book ID to return: "))

        # Delete the loan record for the book from the 'loans' table
        self.cursor.execute("DELETE FROM loans WHERE BookID = ?", (book_id,))
        self.conn.commit()

        print("Book returned successfully!")


    def display_all_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Year Published: {book.year_published}, Type: {book.book_type}")

    def display_all_customers(self):
        for customer in self.customers:
            print(f"ID: {customer.id}, Name: {customer.name}, City: {customer.city}, Age: {customer.age}")

    def display_all_loans(self):
        for loan in self.loans:
            print(f"Customer ID: {loan.cust_id}, Book ID: {loan.book_id}, Loan Date: {loan.loan_date}, Return Date: {loan.return_date}")

    def display_late_loans(self):
        # Implement code to display late loans based on return_date
        pass

    def find_book_by_name(self):
        book_name = input("Enter book name to search for: ")
        found_books = [book for book in self.books if book.name == book_name]
        if found_books:
            for book in found_books:
                print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Year Published: {book.year_published}, Type: {book.book_type}")
        else:
            print("Book not found.")

    def find_customer_by_name(Customer):
        customer_name = input("Enter customer name to search for: ")
        found_customers = [customer for customer in self.customers if customer.name == customer_name]
        if found_customers:
            for customer in found_customers:
                print(f"ID: {customer.id}, Name: {customer.name}, City: {customer.city}, Age: {customer.age}")
        else:
            print("Customer not found.")

    def remove_book(self):
        book_id = int(input("Enter book ID to remove: "))
        
        # Find and remove the book from the books list
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print("Book removed successfully!")
                return
        
        print("Book not found.")

    def remove_customer(self):
        cust_id = int(input("Enter customer ID to remove: "))
        
        # Find and remove the customer from the customers list
        for customer in self.customers:
            if customer.id == cust_id:
                self.customers.remove(customer)
                print("Customer removed successfully!")
                return
        
        print("Customer not found.")

if __name__ == "__main__":
    library_client = LibraryClient()
    library_client.display_menu()

