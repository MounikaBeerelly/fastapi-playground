"""
Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.
Enhance each Book to now have a published_date
"""

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book :
    id : int
    title : str
    author : str
    description : str
    rating : int
    published_date : int
    
    def __init__(self, id, title, author, description, rating, published_date) :
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
    
BOOKS = [
    Book(1, "Namasthe React", "Akshay Saini", "A very nice book", 5, 2030),
    Book(2, "system Design", "Akshay Saini", "A great book", 5, 2030),
    Book(3, "Data Structures", "Akshay Saini", "A awesome book", 5, 2029),
    Book(4, "Book01", "Author 01", "Book description", 3, 2028),
    Book(5, "Book02", "Author 02", "Book description", 2, 2027),
    Book(6, "Book03", "Author 03", "Book description", 4, 2026)
]

# pydantic model for data validation
class BookRequest(BaseModel) :
    id : Optional[int] = Field(description = "ID is not needed on create", default = None)
    title : str = Field(min_length = 3)
    author : str = Field(min_length = 1)
    description : str = Field(min_length = 1, max_length = 100)
    rating : int = Field(gt = 0, lt = 6)
    published_date : int = Field(gt = 1999, lt = 2031)
    
model_config = {
    "json_schema_extra" : {
        "example" : {
            "title" : "A new book",
            "author" : "Author 01",
            "description" : "A description of the book",
            "rating" : 4,
            "published_date" : 2029
        }
    }
}

@app.get("/books/publish/")
async def read_books_by_publish_date(published_date : int) :
    book_to_return = []
    for book in BOOKS :
        if book.published_date == published_date :
            book_to_return.append(book)
    return book_to_return