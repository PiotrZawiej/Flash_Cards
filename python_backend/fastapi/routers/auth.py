from fastapi import HTTPException, APIRouter, Response, Request
from models import User, UserLogin
import database.users as dbc


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register_user(user: User):
    try:
        dbc.Insert_User(user.email, user.username, user.password, user.birth_date)
        return {"message": "User added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/login")
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


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="user_id", httponly=True, samesite='None', secure=True, path="/")
    return {"message": "Logged out successfully"}


@router.get("/check-auth")
def check_auth_status(request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Pobierz username na podstawie user_id
    username = dbc.import_UserName_by_id(user_id)
    if username is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return {"message": "Authenticated", "user": username}


@router.get("/get_cookie")
def get_cookie(request: Request):
    user_id = request.cookies.get("user_id")
    return {"user_id:": user_id}