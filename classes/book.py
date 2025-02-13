class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def displayBook(self):
        status = "available" if self.available else "borrowed"
        print(f"title: {self.title}, author: {self.author}, isbn: {self.isbn}, status: {status}")
