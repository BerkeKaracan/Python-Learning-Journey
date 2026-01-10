import sqlite3
import time
class Library:
    def __init__(self):
        self.con = sqlite3.connect('library.db')
        self.cursor = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, publisher TEXT, genre TEXT, status TEXT)"
        self.cursor.execute(query)
        self.con.commit()

    def add_book(self):
        book_name = input("Enter book name: ").strip().title()
        author = input("Enter book author: ").title().strip()
        publisher = input("Enter book publishing house: ").title().strip()
        genre = input("Enter book genre: ").title().strip()
        if len(book_name) == 0 :
            print("Error : Book name can't be empty")
            return
        check_query = "SELECT * FROM books WHERE name = ? "
        self.cursor.execute(check_query, (book_name,))
        existing_books = self.cursor.fetchall()
        if len(existing_books) > 0:
            print("This book is already in the library")
        else:
            insert_query = "INSERT INTO books VALUES (?,?,?,?,?)"
            self.cursor.execute(insert_query, (book_name, author, publisher, genre, "Available"))
            self.con.commit()
            print(f"{book_name} added to the library")

    def delete_book(self):
        book_name = input("Enter book name: ").title().strip()
        checker = "SELECT * FROM books WHERE name = ? "
        self.cursor.execute(checker, (book_name,))
        existing_books = self.cursor.fetchall()
        if len(existing_books) == 0 :
            print("The book doesn't exist.")
        else:
            delete_query= "DELETE FROM books WHERE name = ?"
            self.cursor.execute(delete_query, (book_name,))
            self.con.commit()
            print(f"{book_name} deleted from the library")
    def show_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("The library is empty")
        else:
            for book in books:
                print(f" Name : {book[0]} | Author : {book[1]} | Publishing House : {book[2]} | Genre : {book[3]} | Status : {book[4]}")
                print("*" * 20)


library = Library()
while True :
    print("*" * 40)
    print("📚 LIBRARY MANAGEMENT SYSTEM")
    print("*" * 40)

    a = input('''
    1 - Show books
    2 - Add book
    3 - Remove book
    Q - Quit
    What do you want to do? : 
    ''').upper()
    if a == "1" :
        library.show_books()
    elif a == "2" :
        library.add_book()
    elif a == "3" :
        k = input("Are you sure? This is irreversible.(Y/N) :").upper()
        if k == "Y" :
            library.delete_book()
        else :
            continue
    elif a == "Q" :
        m = input("Are you sure ?(Y/N) : ").upper()
        if m == "Y" :
            break
        else:
            continue
    else:
        print("Invalid option")

    time.sleep(1)

