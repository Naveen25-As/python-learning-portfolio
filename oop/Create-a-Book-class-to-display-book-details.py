# Create a Book class to display book details..

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book1.display_details()