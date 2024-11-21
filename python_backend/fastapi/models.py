from pydantic import BaseModel


class LearnWord(BaseModel):
    id: int
    word: str
    definition: str


class Flashcard_set(BaseModel):
    set_name: str


class Word(BaseModel):
    word: str
    definition: str  


class User(BaseModel):
    email: str
    username: str
    password: str
    birth_date: str

class UserLogin(BaseModel):
    identifier: str  # This will be either the username or email
    password: str