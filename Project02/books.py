from fastapi import Body, FastAPI
from pydantic import BaseModel

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
    id : int
    title : str
    author : str
    description : str
    rating : int
    
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
    BOOKS.append(new_book)