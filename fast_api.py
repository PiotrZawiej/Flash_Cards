from fastapi import Depends, HTTPException, status, Response, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import hashlib
import python_backend.database_comments as dbc


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Zezwól na dostęp z dowolnego źródła (zmień na konkretny adres, jeśli potrzebujesz)
    allow_credentials=True,
    allow_methods=["*"],  # Zezwól na wszystkie metody (GET, POST, itd.)
    allow_headers=["*"],  # Zezwól na wszystkie nagłówki
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
def log_in(user: UserLogin, response: Response):
    # Pobierz przechowywane hasło na podstawie identyfikatora użytkownika
    stored_password = dbc.import_User_password(user.identifier)

    # Sprawdź, czy wprowadzone hasło pasuje do przechowywanego
    if stored_password is None or user.password != stored_password:
        raise HTTPException(status_code=401, detail="Incorrect identifier or password")

    # Pobierz ID użytkownika na podstawie identyfikatora
    user_id = str(dbc.import_User_id(user.identifier))
    
    # Ustawienie ciasteczka (z zabezpieczeniem dla produkcji)
    response.set_cookie(key="user_id", value=user_id, httponly=True, samesite='None', secure=True, path="/")


@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="user_id", httponly=True, samesite='None', secure=True, path="/")
    return {"message": "Logged out successfully"}

@app.get("/check-auth")
def check_auth_status(request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Pobierz username na podstawie user_id
    username = dbc.import_UserName_by_id(user_id)
    if username is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return {"message": "Authenticated", "user": username}


@app.get("/get_cookie")
def get_cookie(request: Request):
    user_id = request.cookies.get("user_id")
    return {"user_id:": user_id}

