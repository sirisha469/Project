from app.config import settings
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, oauth2
from app.database import SessionLocal, get_db
from app.utils import hash


router = APIRouter(
  prefix="/signup",
  tags=['Sign Up']
)

@router.get("/")
def get(db: Session = Depends(get_db)):
  return {"msg":"Hi sign up"}

@router.post("/", response_model=schemas.signupRes, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.signupReq, db: Session = Depends(get_db)):
  #adding value to password

  pwd_value = user.password + settings.extra_value_to_password
  user.password =  pwd_value

  # hashing password
  hashed_pwd = hash(user.password)
  user.password = hashed_pwd

  new_user = models.Signup(**user.model_dump())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user