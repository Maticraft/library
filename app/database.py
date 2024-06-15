from typing import Dict, List

from app.schemas import SerialNumber, Book, BookCreate, BookStatusUpdate

# in real world, this should be some database e.g. PostgreSQL, MySQL, etc.
BOOKS_DB: Dict[SerialNumber, Book] = {}

def book_exists(serial_number: SerialNumber) -> bool:
    return serial_number in BOOKS_DB

def add_book(book_create: BookCreate) -> Book:
    new_book = Book(
        serial_number=book_create.serial_number,
        title=book_create.title,
        author=book_create.author,
        is_borrowed=False
    )
    BOOKS_DB[new_book.serial_number] = new_book
    return new_book

def remove_book(serial_number: SerialNumber) -> Book:
    book = BOOKS_DB.pop(serial_number, None)
    return book

def get_all_books() -> List[Book]:
    return list(BOOKS_DB.values())

def update_book_status(serial_number: SerialNumber, status_update: BookStatusUpdate) -> Book:
    book = BOOKS_DB[serial_number]
    book.is_borrowed = status_update.is_borrowed
    book.borrowed_by = status_update.borrowed_by
    book.borrowed_date = status_update.borrowed_date
    if not book.is_borrowed:
        book.borrowed_by = None
        book.borrowed_date = None
    return book
