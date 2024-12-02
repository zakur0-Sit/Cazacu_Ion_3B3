class LibraryItem:
    def __init__(self, title, author, own_copies=0):
        self.title = title
        self.author = author
        self.own_copies = own_copies

    def __str__(self):
        return f"{self.title} by {self.author} - {self.own_copies} copies"

    def check_out(self):
        if self.own_copies > 0:
            self.own_copies -= 1
            print(f"Checking out {self.title}")
        else:
            print(f"No copies of {self.title} available.")

    def return_item(self):
        self.own_copies += 1
        print(f"Returning {self.title}")

class Book(LibraryItem):
    def __init__(self, title, author, pages, own_copies=0):
        super().__init__(title, author, own_copies)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} - {self.pages} pages"

class Magazine(LibraryItem):
    def __init__(self, title, author, issue, own_copies=0):
        super().__init__(title, author, own_copies)
        self.issue = issue

    def __str__(self):
        return f"{super().__str__()} - Issue {self.issue}"

class DVD(LibraryItem):
    def __init__(self, title, author, duration, own_copies=0):
        super().__init__(title, author, own_copies)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} - {self.duration} minutes"

class Library:
    def __init__(self):
        self.library_items = []

    def add_item(self, item):
        self.library_items.append(item)

    def remove_item(self, item):
        self.library_items.remove(item)

    def display_items(self):
        print()
        for item in self.library_items:
            print(item)
        print()

book1 = Book("Harry Potter", "J.K. Rowling", 300, 2)
magazine1 = Magazine("National Geographic", "National Geographic Society", 100, 3)
dvd1 = DVD("Inception", "Christopher Nolan", 120, 2)

library = Library()
library.add_item(book1)
library.add_item(magazine1)
library.add_item(dvd1)

library.display_items()
book1.check_out()
book1.check_out()
book1.check_out()
book1.return_item()

library.display_items()
magazine1.check_out()
magazine1.check_out()

library.display_items()
dvd1.check_out()
print(dvd1)