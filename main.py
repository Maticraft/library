from contextlib import asynccontextmanager
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocal, engine


def init_db():
    models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    if crud.get_book(db, book.serial_number):
        raise HTTPException(status_code=400, detail="Book with this serial number already exists")
    book = crud.create_book(db, book)
    return book


@app.delete("/books/{serial_number}", response_model=schemas.Book)
def delete_book(serial_number: schemas.SerialNumber, db: Session = Depends(get_db)):
    if not crud.get_book(db, serial_number):
        raise HTTPException(status_code=404, detail="Book not found")
    book = crud.delete_book(db, serial_number)
    return book


@app.get("/books/", response_model=List[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return books


@app.put("/books/{serial_number}", response_model=schemas.Book)
def update_book_status(serial_number: schemas.SerialNumber, status_update: schemas.BookStatusUpdate, db: Session = Depends(get_db)):
    if not crud.get_book(db, serial_number):
        raise HTTPException(status_code=404, detail="Book not found")
    book =  crud.update_book_status(db, serial_number, status_update)
    return book
