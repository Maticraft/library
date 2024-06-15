from fastapi import FastAPI, HTTPException
from typing import List

from app import schemas, database

app = FastAPI()

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate):
    if database.book_exists(book.serial_number):
        raise HTTPException(status_code=400, detail="Book with this serial number already exists")
    book = database.add_book(book)
    return book

@app.delete("/books/{serial_number}", response_model=schemas.Book)
def delete_book(serial_number: schemas.SerialNumber):
    if not database.book_exists(serial_number):
        raise HTTPException(status_code=404, detail="Book not found")
    status = database.remove_book(serial_number)
    return status

@app.get("/books/", response_model=List[schemas.Book])
def get_books():
    books = database.get_all_books()
    return books

@app.put("/books/{serial_number}", response_model=schemas.Book)
def update_book_status(serial_number: schemas.SerialNumber, status_update: schemas.BookStatusUpdate):
    if not database.book_exists(serial_number):
        raise HTTPException(status_code=404, detail="Book not found")
    status =  database.update_book_status(serial_number, status_update)
    return status
