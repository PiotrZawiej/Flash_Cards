from fastapi import HTTPException, APIRouter
from models import Flashcard_set
from pydantic import BaseModel

import database.Flashcard_sets as dbc

router = APIRouter(prefix="/sets", tags=["Flashcard sets"])


@router.post("/create_Set")
def add_set(request: Flashcard_set):
    try:
        dbc.new_Flashcardset(request.set_name, request.user_id)
        return {"message": "set added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    

class FlashcardSetResponse(BaseModel):
    set_id: int
    set_name: str
    user_id: int

@router.get("/list", response_model=list[FlashcardSetResponse])
def list_flashcard_sets():
    try:
        sets = dbc.select_Flashcard_SetID()
        if not sets:
            raise HTTPException(status_code=404, detail="No flashcard sets found")
        return [FlashcardSetResponse(set_id=row[0], set_name=row[1], user_id=row[2]) for row in sets]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))