# Library Management System.

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")
        
    def show_book(self):
        print("Books in the library:")
        for book in self.books:
            print(f"- {book}")
            
library = Library()

library.add_book("The Great Gatsby")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")

library.show_book()
        