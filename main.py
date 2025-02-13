from classes.book import Book
from classes.library import Library
from classes.librarian import Librarian
from classes.member import Member


library = Library()

librarian = Librarian("anouar",21,"A123")

member = Member("oussama",19,"0U25")

book1 = Book("the prince","mikiavily",123)
book2 = Book("algebra for noobs","alkhawarizmi",1234)
book3 = Book("physics west","einshtein",12345)
book4 = Book("harry potter","martin kiwel",123)


librarian.addBook(library,book1)
librarian.addBook(library,book2)
librarian.addBook(library,book3)
librarian.addBook(library,book4)

librarian.removeBook(library,book4)
librarian.removeBook(library,book3)

library.displayBooks()


member.borrowBook(library,book2)
library.displayBooks()







