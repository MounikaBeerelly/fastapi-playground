from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, sessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db() :
    db = sessionLocal()
    try :
        yield db
    finally :
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
      
@app.get("/todos")
async def read_all_todos(db: db_dependency) :
    return db.query(Todos).all()
