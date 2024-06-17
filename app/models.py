from sqlalchemy import Column, String, Boolean, Date

from .database import Base

class Book(Base):
    __tablename__ = "books"

    serial_number = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    is_borrowed = Column(Boolean, default=False)
    borrowed_by = Column(String, nullable=True)
    borrowed_date = Column(Date, nullable=True)

