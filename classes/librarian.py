from classes.person import Person

class Librarian(Person):
    def __init__(self,name,age,librarian_id):
        super().__init__(name,age)
        self.librarian_id = librarian_id

    def addBook(self,library,book):
        library.addBook(book)

    def removeBook(self,library,book):
        library.removeBook(book)