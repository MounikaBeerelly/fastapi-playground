"""
Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
"""

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books/byAuthor/{author}")
async def read_books_by_author_path(author : str) :
    books_to_return = []
    for book in BOOKS :
        if book.get('author').lower() == author.lower() :
            books_to_return.append(book)
    return books_to_return
        