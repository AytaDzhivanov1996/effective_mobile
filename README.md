# Library Manager

Консольное приложение для управления библиотекой книг.

## Функционал

- Добавление книги
- Удаление книги
- Поиск книги
- Отображение всех книг
- Изменение статуса книги

## Использование

1. Запустите приложение:
    ```
    python main.py
    ```
2. Следуйте инструкциям в меню для выполнения различных операций с книгами.

## Пример работы

1. Добавление книги:
    ```
    Введите название книги: Преступление и наказание
    Введите автора книги: Ф. М. Достоевский
    Введите год издания книги: 1866
    Книга 'Преступление и наказание' добавлена с ID <уникальный идентификатор>.
    ```

2. Удаление книги:
    ```
    Введите ID книги для удаления: <уникальный идентификатор>
    Книга с ID <уникальный идентификатор> удалена.
    ```

3. Поиск книги:
    ```
    По какому полю искать (title, author, year): author
    Введите ключевое слово для поиска: Достоевский
    Book(id='<уникальный идентификатор>', title='Преступление и наказание', author='Ф. М. Достоевский', year=1866, status='в наличии')
    ```

4. Отображение всех книг:
    ```
    Book(id='<уникальный идентификатор>', title='Преступление и наказание', author='Ф. М. Достоевский', year=1866, status='в наличии')
    ```

5. Изменение статуса книги:
    ```
    Введите ID книги для изменения статуса: <уникальный идентификатор>
    Введите новый статус (в наличии, выдана): выдана
    Статус книги с ID <уникальный идентификатор> изменен на 'выдана'.
    ```

## Примечания

- Данные о книгах сохраняются в файле `books.json`.
- Обработка ошибок и исключений включена для основных операций.
