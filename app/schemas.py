import datetime
from typing import Optional

from pydantic import BaseModel


class SerialNumber(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise ValueError('string required')
        if not v.isdigit():
            raise ValueError('string of 6 digits required')
        if len(v) != 6:
            raise ValueError('string of 6 digits required')
        return v
    

# Define schema for the Date
class Date(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            datetime.datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date, should be valid date in format YYYY-MM-DD")
        return v


class Book(BaseModel):
    serial_number: SerialNumber
    title: str
    author: str
    is_borrowed: bool
    borrowed_by: Optional[SerialNumber] = None
    borrowed_date: Optional[Date] = None


class BookCreate(BaseModel):
    serial_number: SerialNumber
    title: str
    author: str


class BookStatusUpdate(BaseModel):
    is_borrowed: bool
    borrowed_by: Optional[SerialNumber] = None
    borrowed_date: Optional[Date] = None
