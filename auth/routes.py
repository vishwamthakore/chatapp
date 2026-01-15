from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.get("/")
def auth_home():
    return {
        "data" : "auth home"
    }

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    inputs = {
        "username": form_data.username,
        "password": form_data.password
    }
    print(inputs)
    return {
        "access_token": form_data.username,
        "token_type": "bearer"
        }


@router.get("/currentuser")
def get_currentuser(token: str = Depends(oauth2_scheme)):
    return {
        "token": token
    }