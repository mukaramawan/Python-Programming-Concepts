# pip install passlib
# pip install bcrypt==4.0.1
# pip install python-multipart
from typing_extensions import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import session_local
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class createUSerRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(user: createUSerRequest, db: db_dependency):
    user = Users(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=bcrypt_context.hash(user.password),
        role=user.role,
        is_active=True
    )
    db.add(user)
    db.commit()

def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

@router.post("/auth/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Incorrect username or password"
    return "Authentication successful"
