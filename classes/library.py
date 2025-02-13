class Library:
    def __init__(self):
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        print(f"{book.title} is been added to the library")

    def removeBook(self,book_title):
        for book in self.books:
            if book == book_title:
                self.books.remove(book)
                print(f"{book.title} is removed")
                return
        print("this book is not found")
    def borrowBook(self,bookTitle):
        for book in self.books:
            if book == bookTitle and book.available:
                book.available = False
                return book
        print("book not available")

    def returnBook(self,book):
        book.available = True

    def displayBooks(self):
        for book in self.books:
            book.displayBook()



