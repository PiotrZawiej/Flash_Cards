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


app.get("/learn_words", response_model=List[Dict[str, str]])
def read_words() -> List[Dict[str, str]]:
    try:
        records = dbc.import_table_content()  # Fetch data from the database
        if not records:
            raise HTTPException(status_code=404, detail="No words found")

        words = [{"word": r[0], "definition": r[1]} for r in records]  # Format each record
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


@app.delete("/learn_words")
def deleteFlashCard(id: int):
    try:
        dbc.delete_table_content(id)
        return {"message": "word deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))