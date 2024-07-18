import json
import os
import uuid

from typing import List


BOOKS_FILE = "books.json"

class Book:
    """Класс для определения сущности книги"""
    def __init__(self, title: str, author: str, year: int):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data: dict):
        book = Book(data['title'], data['author'], data['year'])
        book.id = data['id']
        book.status = data['status']
        return book
    
    def __repr__(self):
        return f"Book(id='{self.id}', title='{self.title}', author='{self.author}', year={self.year}, status='{self.status}')"
    

class LibraryManager:
    """Класс-менеджер для работы библиотеки"""
    def __init__(self):
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        if not os.path.exists(BOOKS_FILE):
            return []
        with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
            books_data = json.load(f)
        return [Book.from_dict(book) for book in books_data]

    def save_books(self):
        with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {new_book.id}.")
        return new_book

    def remove_book(self, book_id: str):
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()
        print(f"Книга с ID {book_id} удалена.")

    def search_books(self, keyword: str, field: str) -> List[Book]:
        if field == 'year':
            results = [book for book in self.books if str(book.year) == keyword]
        else:
            results = [book for book in self.books if keyword.lower() in getattr(book, field).lower()]
        return results

    def display_books(self):
        for book in self.books:
            print(book)

    def change_status(self, book_id: str, status: str) -> bool:
        for book in self.books:
            if book.id == book_id:
                book.status = status
                self.save_books()
                return True
        return False
        