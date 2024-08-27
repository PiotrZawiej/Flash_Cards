from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import bcrypt

import python_backend.database_comments as dbc


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"App": "Flashcards"}

class LearnWord(BaseModel):
    id: int
    word: str
    definition: str

@app.get("/learn_words", response_model=List[LearnWord])
def read_words() -> List[LearnWord]:
    try:
        records = dbc.import_Words()
        if not records:
            raise HTTPException(status_code=404, detail="No words found")

        words = [LearnWord(id=r[0], word=r[1], definition=r[2]) for r in records]  # Format each record
        return words

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class Word(BaseModel):
    word: str
    definition: str   

@app.post("/add_word")
def add_words(word: Word):
    try:
        dbc.add_content_table(word.word, word.definition)
        return {"message": "word added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/learn_words/{id}")
def deleteFlashCard(id: int):
    try:
        dbc.delete_table_content(id)
        return {"message": "word deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
class User(BaseModel):
    email: str
    username: str
    password: str
    birth_date: str
    
    
@app.post("/register")
def register_user(user: User):
    try:
        dbc.Insert_User(user.email, user.username, user.password, user.birth_date)
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
class UserLogin(BaseModel):
    identifier: str  # This will be either the username or email
    password: str
 
@app.post("/login")
def log_in(user: UserLogin):
    stored_password = dbc.import_User_data(user.identifier)
    
    if stored_password is None:
        raise HTTPException(status_code=404, detail="User not found")

    if not bcrypt.checkpw(user.password.encode('utf-8'), stored_password.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Incorrect identifier or password")
    
    return {"message": "Login successful"}