from sqlalchemy.orm import Session

from . import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(serial_number=book.serial_number, title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book(db: Session, serial_number: schemas.SerialNumber):
    return db.query(models.Book).filter(models.Book.serial_number == serial_number).first()

def delete_book(db: Session, serial_number: schemas.SerialNumber):
    db_book = get_book(db, serial_number)
    db.delete(db_book)
    db.commit()
    return db_book

def update_book_status(db: Session, serial_number: schemas.SerialNumber, status: schemas.BookStatusUpdate):
    db_book = get_book(db, serial_number)
    db_book.is_borrowed = status.is_borrowed
    if status.is_borrowed:
        db_book.borrowed_by = status.borrowed_by
        db_book.borrowed_date = status.borrowed_date
    else:
        db_book.borrowed_by = None
        db_book.borrowed_date = None
    db.commit()
    db.refresh(db_book)
    return db_book
