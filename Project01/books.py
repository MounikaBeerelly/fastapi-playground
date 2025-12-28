from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Software Engineering"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt, David Thomas", "category": "Software Engineering"},
    {"title": "You Don't Know JS", "author": "Kyle Simpson", "category": "JavaScript"},
    {"title": "Design Patterns", "author": "Erich Gamma et al.", "category": "Software Architecture"},
    {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "category": "Computer Science"}
]

# -------- GET message ----------
@app.get("/")
async def get_message() :
    return {"message" : "Hello fastapi learners..!"}

# -------- GET all the books ----------
@app.get("/books")
async def read_all_books() :
    return {
        "message" : "books List",
        "data" : books
    }
# -------- GET all the books ----------


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