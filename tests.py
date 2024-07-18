import unittest
import os
import sys
from io import StringIO

from library_manager import Book, LibraryManager, BOOKS_FILE


class TestLibraryManager(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные и временный файл
        self.manager = LibraryManager()
        self.test_books = [
            Book("Book 1", "Author 1", 2001),
            Book("Book 2", "Author 2", 2002),
            Book("Book 3", "Author 3", 2003)
        ]
        self.manager.books = self.test_books
        self.manager.save_books()

    def tearDown(self):
        # Удаляем временный файл после тестов
        if os.path.exists(BOOKS_FILE):
            os.remove(BOOKS_FILE)

    def test_add_book(self):
        #Тест добавления книги
        title = "New Book"
        author = "New Author"
        year = 2020
        self.manager.add_book(title, author, year)
        self.assertEqual(len(self.manager.books), 4)
        self.assertEqual(self.manager.books[-1].title, title)
        self.assertEqual(self.manager.books[-1].author, author)
        self.assertEqual(self.manager.books[-1].year, year)

    def test_search_books(self):
        #Тест поиска
        results = self.manager.search_books("Book 1", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Book 1")

        results = self.manager.search_books("Author 2", "author")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Author 2")

        results = self.manager.search_books("2003", "year")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, 2003)

    def test_display_books(self):
        #Тест списка книг
        captured_output = StringIO()
        sys.stdout = captured_output
        self.manager.display_books()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split('\n')
        self.assertEqual(len(output), 3)

    def test_change_status(self):
        #Тест изменения статуса
        book_id = self.test_books[0].id
        new_status = "выдана"
        self.manager.change_status(book_id, new_status)
        for book in self.manager.books:
            if book.id == book_id:
                self.assertEqual(book.status, new_status)
    
    def test_remove_book(self):
        #Тест удаления книги
        book_id = self.test_books[0].id
        self.manager.remove_book(book_id)
        self.assertEqual(len(self.manager.books), 2)
        for book in self.manager.books:
            self.assertNotEqual(book.id, book_id)

if __name__ == '__main__':
    unittest.main()
