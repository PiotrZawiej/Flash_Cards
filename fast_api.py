from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from python_backend.database_comments import import_table_content
from python_backend.database_comments import add_content_table
from typing import List,Dict
from pydantic import BaseModel



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


@app.get("/learn_words")
def read_words() -> List[Dict[str, str]]:
    records = import_table_content()  # Fetch data from the database
    words = [{"word": r[0], "definition": r[1]} for r in records]  # Format each record
    return words


class Word(BaseModel):
    word: str
    definition: str

@app.post("/add_word")
def add_words(word: Word):
    try:
        add_content_table(word.word, word.definition)
        return {"message", "word added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    
@app.get("/quiz_words")
def get_quiz_words() -> List[Dict[str, str]]:
    records = import_table_content()  # Fetch data from the database
    words = [{"word": r[0], "definition": r[1]} for r in records]  # Format each record
    return words
