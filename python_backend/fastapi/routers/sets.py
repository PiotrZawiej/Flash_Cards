from fastapi import HTTPException, APIRouter
from models import Flashcard_set

import database as dbc


router = APIRouter(prefix="/sets", tags=["Flashcard sets"])


@router.post("/create_Set")
def add_set(set_name: Flashcard_set):
    try:
        dbc.new_Flashcardset(set_name.set_name)
        return {"message": "word added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 