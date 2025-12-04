 # Simplified & Shortened Library Management System



## 📂 Project Structure


## 📌 `library_manager/__init__.py`



## 📌 `library_manager/book.py`

# ```python
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status,
        }



## 📌 `library_manager/inventory.py`

# ```python
import json
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, filepath):
        self.file = Path(filepath)
        self.books = []
        self.load()

    def load(self):
        if self.file.exists():
            try:
                data = json.load(open(self.file))
                self.books = [Book(**b) for b in data]
            except:
                self.books = []
        else:
            self.books = []

    def save(self):
        json.dump([b.to_dict() for b in self.books], open(self.file, "w"), indent=2)

    def add_book(self, book):
        self.books.append(book)
        self.save()

    def search_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def search_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def issue(self, isbn):
        b = self.search_isbn(isbn)
        if b and b.status == "available":
            b.status = "issued"
            self.save()
            return True
        return False

    def return_book(self, isbn):
        b = self.search_isbn(isbn)
        if b and b.status == "issued":
            b.status = "available"
            self.save()
            return True
        return False
