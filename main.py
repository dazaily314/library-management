from classes.book import Book
from classes.library import Library
from classes.librarian import Librarian
from classes.member import Member


library = Library()

librarian = Librarian("anouar",21,"A123")

member = Member("oussama",19,"0U25")

while True:
    print("welcome to anouar's library")
    print("please chose from the menu what you want")
    print("type 1 if you are a librarian\ntype 2 if you are a member")
    role = input("--:")
    while role == "1":
        print("1 ----------- add book")
        print("2 ----------- remove book")
        print("3 ----------- show books")
        print("0 ----------- exit")
        choice = input("---:")
        if choice == "1":
            title = input("title: ")
            author = input("author: ")
            isbn = input("isbn: ")
            librarian.addBook(library,Book(title,author,isbn))
        elif choice == "2":
            title = input("type the title of the book you want to remove: ")
            librarian.removeBook(library,title)
        elif choice == "3":
            library.displayBooks()
        elif choice == "0":
            break
        else:
            print("please chose a valid number")
    while role == "2":
        print("1 ----------- borrow book")
        print("2 ----------- return book")
        print("3 ----------- show borrowed books 'status = borrowed'")
        print("0 ----------- exit")
        choice = input("---:")
        if choice == "1":
            title = input("title: ")
            member.borrowBook(library,title)
        elif choice == "2":
            title = input("type the title of the book you want to return: ")
            member.returnBook(library,title)
        elif choice == "3":
            member.showBorrowedBooks()
        elif choice == "0":
            break
        else:
            print("please chose a valid number")

















