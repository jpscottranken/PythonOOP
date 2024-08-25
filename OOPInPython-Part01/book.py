'''
	OOPInPython-Part01
	https://levelup.gitconnected.com/oop-in-python-a-comprehensive-guide-to-key-terms-and-concepts-f19bcfd08dc6
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class Library:
    def __init__(self):
        self.books = [] # aggregation
    
    def add_book(self, book):
        self.books.append(book)
        print(f'{book.title} by {book.author} added to the library')

book1 = Book('The Catcher in the Rye', 'J.D. Salinger')
library = Library()
library.add_book(book1)

book2 = Book('To Kill a Mockingbird', 'Harper Lee')
library.add_book(book2)