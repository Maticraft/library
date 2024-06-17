from datetime import date
from typing import Optional

from typing_extensions import Annotated

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator


def validate_serial_number(v: str) -> str:
    if not v.isdigit():
        raise ValueError('string of 6 digits required')
    if len(v) != 6:
        raise ValueError('string of 6 digits required')
    return v

SerialNumber = Annotated[str, AfterValidator(validate_serial_number)]

class Book(BaseModel):
    serial_number: SerialNumber
    title: str
    author: str
    is_borrowed: bool
    borrowed_by: Optional[SerialNumber] = None
    borrowed_date: Optional[date] = None


class BookCreate(BaseModel):
    serial_number: SerialNumber
    title: str
    author: str


class BookStatusUpdate(BaseModel):
    is_borrowed: bool
    borrowed_by: Optional[SerialNumber] = None
    borrowed_date: Optional[date] = None
