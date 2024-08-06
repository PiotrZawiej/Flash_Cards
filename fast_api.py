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

class Word(BaseModel):
    id: int
    word: str
    definition: str
    
    
@app.get("/learn_words", response_model=List[Word])
def read_words() -> List[Word]:
    try:
        records = dbc.import_table_content()  # Fetch data from the database
        if not records:
            raise HTTPException(status_code=404, detail="No words found")

        words = [Word(id=r[0], word=r[1], definition=r[2]) for r in records]  # Format each record
        return words

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

@app.post("/add_word")
def add_words(word: Word):
    try:
        dbc.add_content_table(word.word, word.definition)
        return {"message": "word added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 


@app.delete("/learn_words/{id}",  response_model=List[int])
def deleteFlashCard(id: int):
    try:
        dbc.delete_table_content(id)
        return {"message": "word deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))