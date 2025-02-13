from classes.person import Person

class Member(Person):
    def __init__(self,name,age,member_id):
        super().__init__(name,age)
        self.member_id = member_id
        self.borrowedBooks = []

    def borrowBook(self,library,bookTitle):
        book = library.borrowBook(bookTitle)
        if book:
            self.borrowedBooks.append(book)
            print(f"{book.title} is borrowed by {self.name}")

    def returnBook(self,library,bookTitle):
        book = library.returnBook(bookTitle)
        if book:
            self.borrowedBooks.remove(book)
            print(f"{book.title} just been returned by {self.name}")

    def showBorrowedBooks(self):
        for book in self.borrowedBooks:
            print(f"title: {book.title}, author: {book.author}, isbn: {book.isbn}")
