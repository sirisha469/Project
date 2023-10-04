from app.config import settings
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .. import schemas, models
from app.database import SessionLocal, get_db
from app.utils import hash


router = APIRouter(
  prefix="/signup",
  tags=['Sign Up']
)

@router.get("/")
def get(db: Session = Depends(get_db)):
  return {"msg":"Hi sign up"}

@router.post("/", response_model=schemas.signupRes)
def create_user(user: schemas.signupReq, db: Session = Depends(get_db)):
  #adding value to password
  pwd_value = user.password + settings.extra_value_to_password
  user.password =  pwd_value

  # hashing password
  for i in range(0,3):
    hashed_pwd = hash(user.password)
    user.password = hashed_pwd

  new_user = models.Signup(**user.model_dump())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user