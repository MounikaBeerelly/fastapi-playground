from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book :
    id : int
    title : str
    author : str
    description : str
    rating : int
    
    def __init__(self, id, title, author, description, rating) :
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
    
BOOKS = [
    Book(1, "Namasthe React", "Akshay Saini", "A very nice book", 5),
    Book(2, "system Design", "Akshay Saini", "A great book", 5),
    Book(3, "Data Structures", "Akshay Saini", "A awesome book", 5),
    Book(4, "Book01", "Author 01", "Book description", 3),
    Book(5, "Book02", "Author 02", "Book description", 2),
    Book(6, "Book03", "Author 03", "Book description", 4)
]

# pydantic model for data validation
class BookRequest(BaseModel) :
    id : Optional[int] = Field(description = "ID is not needed on create", default = None)
    title : str = Field(min_length = 3)
    author : str = Field(min_length = 1)
    description : str = Field(min_length = 1, max_length = 100)
    rating : int = Field(gt = 0, lt = 6)
    
model_config = {
    "json_schema_extra" : {
        "example" : {
            "title" : "A new book",
            "author" : "Author 01",
            "description" : "A description of the book",
            "rating" : 4
        }
    }
}

@app.get("/books")
async def read_all_books() :
    return BOOKS

@app.post("/add-book")
async def create_book(book_request=Body()) :
    BOOKS.append(book_request)
    
# add validations using pydantic
@app.post("/create-book")
async def create_book(book_request : BookRequest) :
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    
def find_book_id(book : Book) :
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


# ------- fetch single book -------
@app.get("/books/{book_id}")
async def read_book(book_id : int = Path(gt = 0)) :
    for book in BOOKS :
        if book.id == book_id :
            return book
        
# ------ Fetch book by rating --------
@app.get("/books/")
async def read_book_by_rating(book_rating : int = Query(gt = 0, lt = 6)) :
    books_to_return = []
    for book in BOOKS :
        if book.rating == book_rating :
            books_to_return.append(book)
    return books_to_return

# ------ Update book using PUT method ------
@app.put("/books/update_book")
async def update_book(book : BookRequest) :
    for i in range(len(BOOKS)) :
        if BOOKS[i].id == book.id :
            BOOKS[i] = book
            
# ------- Delete Book using DELETE method -------
@app.delete("/books/{book_id}")
async def delete_book(book_id : int = Path(gt = 0)):
    for i in range(len(BOOKS)) :
        if BOOKS[i].id == book_id :
            BOOKS.pop(i)
            break
        