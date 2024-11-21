from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, flashacrds, sets
from database.users import Insert_User, import_User_password, import_User_id, import_UserName_by_id
from database.Flashcard_sets import new_Flashcardset, select_Flashcard_SetID
from database.flashcard import import_Words, delete_table_content, insert_Words

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(auth.router)
app.include_router(flashacrds.router)
app.include_router(sets.router)

@app.get("/")
def read_root():
    return {"App": "Flashcards"}







