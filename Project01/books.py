from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Software Engineering"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt, David Thomas", "category": "Software Engineering"},
    {"title": "You Don't Know JS", "author": "Kyle Simpson", "category": "JavaScript"},
    {"title": "Design Patterns", "author": "Erich Gamma et al.", "category": "Software Architecture"},
    {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "category": "Computer Science"},
    {"title": "You Know TS", "author": "Kyle Simpson", "category": "TypeScript"},

]

# -------- GET message ----------
@app.get("/")
async def get_message() :
    return {"message" : "Hello fastapi learners..!"}

"""
- Run the fastapi application using `uvicorn books:app --reload`

How app Works (Simple Flow)
----------------------------
1. Browser sends request → GET /books
2. Uvicorn receives request
3. Uvicorn passes request to app
4. app matches the route
5. Corresponding function runs
6. Response is returned
"""

# -------- GET all the books ----------
@app.get("/books")
async def read_all_books() :
    return {
        "message" : "books List",
        "data" : books
    }
# -------- GET the specific book ----------

# path parameters
@app.get("/books/{book_title}")
async def read_single_book(book_title: str) :
    for book in books :
        # if book.get('title').casefold() == book_title.casefold() :
        if book.get('title').lower() == book_title.lower() :
            return book

# query parameters
@app.get("/books/")
async def read_category_by_query(category : str) :
    book_to_return = []
    for book in books :
        if book.get('category').lower() == category.lower() :
            book_to_return.append(book)
    return book_to_return
        
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author : str, category: str) :
    books_to_return = []
    for book in books :
        if book.get('author').lower() == book_author.lower() and \
            book.get('category').lower() == category.lower() :
                books_to_return.append(book)
                
    return books_to_return