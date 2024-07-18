from library_manager import LibraryManager


def main():
    manager = LibraryManager()
    
    while True:
        print("\n1. Добавить книгу\n2. Удалить книгу\n3. Поиск книги\n4. Показать все книги\n5. Изменить статус книги\n6. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            try:
                year = int(year)
                manager.add_book(title, author, year)
            except ValueError:
                print("Год издания должен быть числом.")
        elif choice == '2':
            book_id = input("Введите ID книги для удаления: ")
            manager.remove_book(book_id)
        elif choice == '3':
            field = input("По какому полю искать (title, author, year): ")
            keyword = input("Введите ключевое слово для поиска: ")
            if field in ['title', 'author', 'year']:
                results = manager.search_books(keyword, field)
                if results:
                    for book in results:
                        print(book)
                else:
                    print(f"Книги по запросу '{keyword}' не найдены.")
            else:
                print("Неверное поле для поиска.")
        elif choice == '4':
            manager.display_books()
        elif choice == '5':
            book_id = input("Введите ID книги для изменения статуса: ")
            status = input("Введите новый статус (в наличии, выдана): ")
            if status in ['в наличии', 'выдана']:
                manager.change_status(book_id, status)
            else:
                print("Неверный статус.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
