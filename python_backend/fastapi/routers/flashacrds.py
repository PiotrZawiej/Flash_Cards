from fastapi import HTTPException, APIRouter
from typing import List
from models import LearnWord, Word
import database.flashcard as dbc


router = APIRouter(prefix="/flashcard", tags=["Flashcards"])


@router.get("/learn_words", response_model=List[LearnWord])
def read_words() -> List[LearnWord]:
    try:
        records = dbc.import_Words()
        if not records:
            raise HTTPException(status_code=404, detail="No words found")

        words = [LearnWord(id=r[0], word=r[1], definition=r[2]) for r in records]  # Format each record
        return words

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/add_word")
def add_words(word: Word):
    try:
        dbc.add_content_table(word.word, word.definition)
        return {"message": "word added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/learn_words/{id}")
def deleteFlashCard(id: int):
    try:
        dbc.delete_table_content(id)
        return {"message": "word deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))