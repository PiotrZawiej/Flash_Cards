from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import python_backend.database_comments as dbc
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
    records = dbc.import_table_content()  # Fetch data from the database
    words = [{"word": r[0], "definition": r[1]} for r in records]  # Format each record
    return words


class Word(BaseModel):
    word: str
    definition: str

@app.post("/add_word")
def add_words(word: Word):
    try:
        dbc.add_content_table(word.word, word.definition)
        return {"message", "word added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 