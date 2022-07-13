from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from typing import Optional,List
#from . import models
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
import logging 
log=logging.getLogger(__name__)



models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Todo(BaseModel):
    id:str
    message:str
    class Config:
        orm_mode=True

app=FastAPI(title="Todo App",version="V1")

store_todo=[]

@app.get('/')
async def home():
    return{"Hello":"Universe! "}

@app.post('/todo/')
async def create_todo(todo:Todo,db: Session = Depends(get_db)):
    _todo=models.Todo(message=todo.message)
    db.add(_todo)
    db.commit()
    db.refresh(_todo)
    

    print('todo: %s', store_todo)
    return todo

@app.get('/todo')
async def get_all_todos(db: Session = Depends(get_db)):
    todo_list= db.query(models.Todo).all()
    return todo_list
@app.get('/todo/{id}')
async def get_todo(id:int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")
    
@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):

    try:

        store_todo[id] = todo
        return store_todo[id]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")

@app.delete('/todo/{id}') 
async def delete_todo(id:int):
    try:
        obj=store_todo[id]
        store_todo.pop(id)
        return obj
    except:
           raise HTTPException(status_code=404, detail="Todo Not Found")
    
    

    

